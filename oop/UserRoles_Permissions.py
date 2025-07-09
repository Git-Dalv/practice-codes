from __future__ import annotations
from datetime import datetime


class PermissionsSet:
    def __init__(self, permissions: list[str]):
        self.permissions = set(permissions)

    def has_permission(self, permission: str) -> bool:
        return permission in self.permissions

    def add_permission(self, permission: str) -> None:
        self.permissions.add(permission)

    def remove_permission(self, permission: str) -> None:
        self.permissions.remove(permission)


class FriendsList:
    def __init__(self):
        self.friends: list[User] = []

    def __str__(self):
        friends_str = ""
        for i, friend in enumerate(self.friends):
            friends_str += f"{i}) {str(friend)}\n"
        return friends_str

    def add_to_list(self, u: User):
        self.friends.append(u)

    def remove_from_list(self, u: User):
        if u in self.friends:
            self.friends.remove(u)
        else:
            raise Exception("User is not a friend")

    def has_friend(self, u: User) -> bool:
        return u in self.friends


class Letter:
    def __init__(self, from_name: str, to_name: str, text: str):
        self.date = datetime.now()
        self._from_name = from_name
        self._to_name = to_name
        self._text = text

    def __str__(self):
        return f"From: {self._from_name}, To: {self._to_name} \t Data: {self.date}\nText:\n\t{self._text}"

    @property
    def from_name(self):
        return self._from_name

    @from_name.setter
    def from_name(self, from_name: str):
        self._from_name = from_name

    @property
    def to_name(self):
        return self._to_name

    @to_name.setter
    def to_name(self, to_name: str):
        self._to_name = to_name

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text: str):
        self._text = text


class Mail:
    def __init__(self):
        self.mail: list[Letter] = []

    def __str__(self):
        mail_str = ""
        for letter in self.mail:
            mail_str += str(letter) + "\n"
        return mail_str

    def add_to_list(self, letter: Letter):
        self.mail.append(letter)


class User:
    def __init__(self, name: str, id: str) -> None:
        self.permissions = PermissionsSet(["Send Message", "Add Friend",
                                           "Remove Friend", "Post Publication"])  # User has-a PermissionsSet
        self.friends = FriendsList()  # User has-a FriendsList
        self.mail = Mail()  # User has-a Mail
        self._name = None
        self._id = None
        self.name = name
        self.id = id

    def __str__(self):
        return f"Name: {self.name}, ID: {self.id}"

    def can(self, action: str) -> bool:
        return self.permissions.has_permission(action)

    def add_friend(self, friend: User):
        self.friends.add_to_list(friend)

    def remove_friend(self, friend: User):
        self.friends.remove_from_list(friend)

    def show_friends(self):
        print(self.friends)

    def send_message(self):
        if not self.can("Send Message"): raise Exception("Can't send message")
        while True:
            num = int(input(f"Enter a number of friend: \n {self.friends}"))
            if num > len(self.friends.friends) or num < 0:
                print("Number out of range")
                continue
            break
        text = str(input(f"Enter your message: "))
        letter = Letter(self.name, self.friends.friends[num].name, text)
        self.friends.friends[num].mail.add_to_list(letter)

    def show_mail(self):
        print(self.mail)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        self._id = id


class Moderator(User): # Moderator is-a User
    def __init__(self, name: str, id: str) -> None:
        super().__init__(name, id)
        new_permissions = {"Remove Post", "Moderate Post",
                           "Mute User"}
        for permission in new_permissions:
            self.permissions.add_permission(permission)


class Admin(Moderator): # Admin is-a Moderator
    def __init__(self, name: str, id: str) -> None:
        super().__init__(name, id)
        new_permissions = {"Ban User", "Assign Moderator"}
        for permission in new_permissions:
            self.permissions.add_permission(permission)

    def take_permission(self, permission: str, user: User) -> None:
        if permission not in user.permissions: raise Exception("Permission does not exist")
        user.permissions.remove_permission(permission)


user = User("Bob", "11111110")
moderator = Moderator("Alice", "00002221")
admin = Admin("Dalv", "00000001")

user.add_friend(moderator)
user.show_friends()
user.send_message()
moderator.show_mail()

print(user.can("Send Message"))
print(moderator.can("Ban User"))
print(admin.can("Send Message"))
