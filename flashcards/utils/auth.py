from functools import wraps
import flask as fl
import bcrypt
import jwt

from flashcards.core.exceptions import UnauthorizedError


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


def encode_jwt(payload, secret):
    return jwt.encode(payload, secret)


def decode_jwt(payload, secret):
    return jwt.decode(payload, secret)


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if fl.g.user is None:
            raise UnauthorizedError('Required login')
        return f(*args, **kwargs)

    return decorated
