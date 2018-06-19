import bcrypt
import jwt


def hash_password(password):
    return bcrypt.hashpw(password, bcrypt.gensalt())


def is_correct_password(password, hashed):
    return bcrypt.hashpw(password, hashed) == hashed


def encode_jwt(self, payload, secret, algorithm='HS256'):
    return jwt.encode(payload, secret, algorithm)


def decode_jwt(self, payload, secret, algorithm='HS256'):
    return jwt.encode(payload, secret, algorithm)
