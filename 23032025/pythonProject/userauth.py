import usernotfoundexception
import wrongpassworderror
class UserAuth:
    def __init__(self, credentials):
        self.credentials = credentials

    def login(self, username, password):
        if username in self.credentials.keys():
            if password == self.credentials[username]:
                return print("login successful")
            else:
                raise wrongpassworderror.WrongPasswordError("Wrong password!")
        else:
            raise usernotfoundexception.UserNotFound("User not found!")
