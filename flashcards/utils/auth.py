import bcrypt
import jwt


def _to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        return bytes_or_str.encode()
    return bytes_or_str


def generate_hash_password(password):
    password = _to_bytes(password)
    return bcrypt.hashpw(password, bcrypt.gensalt())


def is_correct_password(password, hashed) -> bool:
    password = _to_bytes(password)
    hashed = _to_bytes(hashed)
    try:
        return bcrypt.hashpw(password, hashed) == hashed
    except ValueError as e:
        return False


def encode_jwt(self, payload, secret, algorithm='HS256'):
    return jwt.encode(payload, secret, algorithm)


def decode_jwt(self, payload, secret, algorithm='HS256'):
    return jwt.encode(payload, secret, algorithm)
