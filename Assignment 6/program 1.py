class Password_manager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        return self.old_passwords[-1] 

    def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)

    def is_correct(self, password):
        return password == self.get_password()


password = Password_manager()
password.set_password("1234")
password.set_password("abcd")

print(password.get_password())  
print(password.is_correct("abcd")) 
print(password.is_correct("1234"))  