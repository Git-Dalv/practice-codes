from enum import Enum, auto
from functools import wraps


class Permission(Enum):
    READ = auto()
    WRITE = auto()
    DELETE = auto()
    EDIT = auto()
    ADMIN = auto()


roles_permission = {
    'guest': {Permission.READ},
    'editor': {Permission.READ, Permission.WRITE, Permission.EDIT},
    'moderator': {Permission.READ, Permission.WRITE, Permission.EDIT, Permission.DELETE},
    'admin': {p for p in Permission}
}


class User:
    def __init__(self, username: str, roles: list[str]):
        self.username = username
        self.roles = roles

    @property
    def permissions(self) -> set[Permission]:
        perms = set()
        for role in self.roles:
            perms.update(roles_permission.get(role, set()))
        return perms


def require_permission(permission: Permission):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if permission in self._user.permissions:
                return func(self, *args, **kwargs)
            else:
                raise PermissionError(f"User {self._user.username} lacks permission '{permission.name}'")

        return wrapper

    return decorator


def singleton(cls):
    _instances = {}

    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return get_instance


@singleton
class Connect:

    def __init__(self, user: User, url: str):
        if 'admin' not in user.roles:
            raise PermissionError(f"User {user.username} lacks permission")
        self._user = user
        self._connection = False
        self.connection(url)

    @property
    def permissions(self):
        return self._user.permissions

    @require_permission(Permission.ADMIN)
    def connection(self, url: str):
        if self._connection is True:
            print("Already connected!")
            return
        print(f"{self._user.username} try to connect to {url}")
        self._connection = True
        print(f'Connection Status: {self._connection}')


user_a = User('admin', ['admin'])
user_g = User('guest', ['guest'])

try:
    con1 = Connect(user_g, "a52s25", )
except Exception:
    print("error")

con = Connect(user_a, 'a152ff4')
