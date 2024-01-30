import os
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt
from passlib.context import CryptContext
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
JWT_REFRESH_SECRET_KEY = os.getenv('JWT_REFRESH_SECRET_KEY')
REFRESH_TOKEN_EXPIRE_MINUTES = os.getenv('REFRESH_TOKEN_EXPIRE_MINUTES')


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    """
    Generates a hashed password using the bcrypt algorithm.
    
    :param password: The password to hash.
    :type password: str
    :return: The hashed password.
    :rtype: str
    
    """
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    """
    Verifies a password against a hashed password.
    
    :param password: The password to verify.
    :type password: str
    :param hashed_pass: The hashed password to compare against.
    :type hashed_pass: str
    :return: True if the password matches the hashed password, False otherwise.
    :rtype: bool
    
    """
    return password_context.verify(password, hashed_pass)

def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    """
    Creates an access token for the given subject.
    
    :param subject: The subject to create the access token for.
    :type subject: Union[str, Any]
    :param expires_delta: The number of minutes before the access token expires.
    :type expires_delta: int
    :return: The access token.
    :rtype: str
    
    """
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt

def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    """
    Creates a refresh token for the given subject.
    
    :param subject: The subject to create the refresh token for.
    :type subject: Union[str, Any]
    :param expires_delta: The number of minutes before the refresh token expires.
    :type expires_delta: int
    :return: The refresh token.
    :rtype: str
    
    """
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt