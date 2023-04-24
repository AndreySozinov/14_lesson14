import pytest


@pytest.fixture()
def my_project():
    m1 = MyProject()
    m1.user_generator('users.json')
    return m1


def test_enter(my_project):
    assert my_project.enter('John', '5') == User('John', '5', 2)


def test_add_user(my_project):
    assert my_project.add_user('Pyotr', '455', 3) == User('Pyotr', '455', 3)
    

if __name__ == '__main__':
    pytest.main(['-v'])


class User:
    def __init__(self, name: str, user_id: str, access_level: int):
        self.name = name
        self.user_id = user_id
        self.access_level = access_level

    def __str__(self):
        return f'User name: {self.name}; id: {self.user_id}; access level: {self.access_level}'

    def __eq__(self, other):
        return self.user_id == other.user_id and self.name == other.name

    def __hash__(self):
        return hash((self.name, self.user_id))


class MyBaseException(Exception):
    pass


class LevelError(MyBaseException):
    def __init__(self, value, value2):
        self.value = value
        self.value2 = value2

    def __str__(self):
        return f'Level Error: your level {self.value} is lesser than required - {self.value2}'


class AccessError(MyBaseException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Access Error: no user with name {self.value}'


class MyProject:
    users_set = set()
    MY_LEVEL = 3

    def user_generator(self, json_file_path: str) -> set[User]:
        import json
        with open(json_file_path, 'r') as f:
            json_file = json.load(f)
            for level in json_file:
                for key, value in json_file[level].items():
                    self.users_set.add(User(value, key, level))
        return self.users_set

    def enter(self, user_name, user_id) -> User:
        for user in self.users_set:
            if User(user_name, user_id, 0) == user:
                user_access_level = int(user.access_level)
                return User(user_name, user_id, user_access_level)
        raise AccessError(user_name)

    def add_user(self, name, user_id, access_level) -> User:
        if access_level >= self.MY_LEVEL:
            u1 = User(name, user_id, access_level)
            self.users_set.add(u1)
            return u1
        raise LevelError(access_level, self.MY_LEVEL)
