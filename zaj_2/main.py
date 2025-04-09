class UserNotFoundError(Exception):
    def __init__(self, message="User not found"):
        self.message = message
        super().__init__(self.message)

class WrongPasswordError(Exception):
    def __init__(self, message="Incorrect password"):
        self.message = message
        super().__init__(self.message)

class UserAuth:
    def __init__(self, user_data):
        self.user_data = user_data


    def login(self, username, password):
        if username not in self.user_data:
            raise UserNotFoundError(f"User '{username}' not found.")

        if self.user_data[username] != password:
            raise WrongPasswordError("Incorrect password.")

        if username in self.user_data and self.user_data[username] == password:
            print("Login successful")
            return


auth = UserAuth({"admin": "1234", "user": "abcd"})

try:
    auth.login("admin", "1234") # Sukces
    auth.login("unknown", "pass") # Powinien rzucić UserNotFoundError
except Exception as e:
    print(f"Błąd: {e}")

try:
    auth.login("admin", "1234")  # Sukces
    auth.login("user", "wrongpass")  # Powinien rzucić WrongPasswordError
except Exception as e:
    print(f"Błąd: {e}")

