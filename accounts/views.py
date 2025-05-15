from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
from .models import CustomUser
from .serializers import UserSerializer
from django.contrib.auth import authenticate
import jwt
from datetime import datetime, timedelta
from django.conf import settings
import re
from supabase import create_client, Client
from enviroment import config
import requests

# Initialize Supabase client
supabase_url = config["SUPABASE_URL"]
supabase_key = config["SUPABASE_KEY"]
supabase: Client = create_client(supabase_url, supabase_key)

print(dir(supabase.auth))

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def __verify_login(username, password):
    user = authenticate(username=username, password=password)
    if user is None:
        # Log the failed authentication attempt for debugging
        print(f"Authentication failed for username: {username}. Check if the user exists and the password is correct.")
    else:
        print(f"Authentication successful for username: {username}")
    return user is not None

ERROR_MESSAGES = {
    "missing_credentials": "Username and password are required.",
}

@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')  # Cambiado de 'username' a 'email'
    password = request.data.get('password')
    print(email)
    print(password)
    if not email or not password:
        return Response({"error": ERROR_MESSAGES["missing_credentials"]}, status=status.HTTP_400_BAD_REQUEST)
    if not password:
        return Response({"error": "Password is required and cannot be empty."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        user = CustomUser.objects.get(email=email)  # Buscar usuario por email
    except CustomUser.DoesNotExist:
        return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    if __verify_login(user.username, password):  # Autenticar usando el username del usuario
        access_token = __generate_jwt_token(user)
        refresh_token = __generate_refresh_token(user)
        user_data = UserSerializer(user).data

        return Response({
            "message": "Login successful.",
            "tokens": {
                "access": access_token,
                "refresh": refresh_token
            },
            "user": user_data
        }, status=status.HTTP_200_OK)
    return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

def __generate_refresh_token(user):
    """
    Genera un refresh token JWT para el usuario autenticado.
    """
    payload = {
        'user_id': user.id,
        'type': 'refresh',
        'exp': datetime.utcnow() + timedelta(days=7),  # Expira en 7 días
        'iat': datetime.utcnow(),  # Fecha de emisión
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token

def __verify_regex_password(password):
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'  # Minimum 8 characters, at least one letter and one number
    return re.match(pattern, password) is not None

@api_view(['POST'])
def supabase_register_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if not email or not password:
        return Response({"error": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)
    
    response = supabase.auth.sign_up(email=email, password=password)
    if response.get('error'):
        return Response({"error": response['error']['message']}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def supabase_login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if not email or not password:
        return Response({"error": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)
    
    response = supabase.auth.sign_in_with_password(email=email, password=password)
    if response.get('error'):
        return Response({"error": response['error']['message']}, status=status.HTTP_401_UNAUTHORIZED)
    return Response({"message": "Login successful.", "session": response['data']}, status=status.HTTP_200_OK)

@api_view(['POST'])
def supabase_oauth_login(request):
    provider = request.data.get('provider')  # Ejemplo: 'google', 'github', etc.
    if not provider:
        return Response({"error": "El proveedor es obligatorio."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        response = supabase.auth.sign_in_with_oauth({"provider": provider})
        response_dict = vars(response)
        print(response_dict)
        # Aquí puedes manejar la redirección a la URL de autorización del proveedor
        # Por ejemplo, redirigir al usuario a la URL de autorización de Google
        # response contiene la URL de autorización
        # Puedes devolver la URL al cliente para que el usuario pueda iniciar sesión
        # o manejar la redirección en el frontend
        # En este caso, simplemente devolvemos la URL para que el cliente pueda redirigir al usuario
        # res_to_redirect = requests.get(response_dict['url'])
        # res_dict = res_to_redirect.json()
        # # Aquí puedes manejar la respuesta de la redirección
        # print(res_dict.get('code'))
        # if res_dict.get('code') != 200:
        #     return Response({"error": res_dict.get('error_code'), "message": res_dict.get('msg'), 
        #                      "code": res_dict.get('code')}, status=status.HTTP_400_BAD_REQUEST)
        
        
        return Response({"message": "Inicio de sesión OAuth exitoso.", "url": response_dict.get('url')}, status=status.HTTP_200_OK)
    except Exception as e:
        # Manejo de errores inesperados
        return Response({"error": f"Error inesperado: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def __generate_jwt_token(user):
    """
    Genera un token JWT para el usuario autenticado.
    Incluye información sobre el rol del usuario (admin o normal) y el ID del usuario.
    """
    payload = {
        'id': user.id,  # Agregar el ID del usuario al payload
        'user_id': user.id,
        'username': user.username,
        'role': 'admin' if user.is_staff else 'user',  # Determina el rol del usuario
        'exp': datetime.utcnow() + timedelta(hours=24),  # Expira en 24 horas
        'iat': datetime.utcnow(),  # Fecha de emisión
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token

@api_view(['POST'])
def refresh_token(request):
    """
    Genera un nuevo access token utilizando un refresh token válido.
    """
    refresh_token = request.data.get('refresh_token')
    if not refresh_token:
        return Response({"error": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Decodificar el refresh token
        payload = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=['HS256'])
        
        # Verificar si el token es de tipo "refresh"
        if payload.get('type') != 'refresh':
            return Response({"error": "Invalid token type."}, status=status.HTTP_400_BAD_REQUEST)

        # Obtener el usuario asociado al token
        user_id = payload.get('user_id')
        user = CustomUser.objects.get(id=user_id)

        # Generar un nuevo access token
        access_token = __generate_access_token(user)

        return Response({"access_token": access_token}, status=status.HTTP_200_OK)
    except jwt.ExpiredSignatureError:
        return Response({"error": "Refresh token has expired."}, status=status.HTTP_401_UNAUTHORIZED)
    except jwt.InvalidTokenError:
        return Response({"error": "Invalid refresh token."}, status=status.HTTP_401_UNAUTHORIZED)
    except CustomUser.DoesNotExist:
        return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_user(request, username):
    try:
        user = CustomUser.objects.get(username=username)
    except CustomUser.DoesNotExist:
        return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


