# Пароль пользователя должен отвечать следующим требованиям:
# Длина пароля должна быть не менее 8 и не более 14 символов.
# Пароль должен состоять из букв латинского алфавита (A-z), арабских цифр (0-9) и специальных символов, приведенных в п. 4 данных требований.
# Буквенная часть пароля должна содержать как строчные, так и прописные (заглавные) буквы.
# Пароль должен содержать не менее одного из следующих символов:
# ( . , : ; ? ! * + % - < > @ [ ] { } / \ _ {} $ # ).

import random as rd
import string

class Password:
    def __init__(self) -> None:
        self._special_characters = '(.,:;?!*+%-<>@[]/\_}{$#)'
        self._base_symbols = [string.ascii_uppercase, string.ascii_lowercase, string.digits, self._special_characters]
        self._user_password = ''.join(map(lambda x: rd.choice(x), self._base_symbols))

    def password_generation(self) -> None:
        for _ in range(rd.randrange(4, 11)):
            self._user_password += rd.choice(rd.choice(self._base_symbols))
        self._user_password = ''.join(rd.sample(self._user_password, len(self._user_password)))

    def is_valid_password(self) -> bool:
        if len(self._user_password) not in range(8, 15):
            return False
        
        elif not any([sym.isupper() for sym in self._user_password]) or not any([sym.islower() for sym in self._user_password]):
            return False
        
        elif not any([sym for sym in self._user_password if sym in self._special_characters]):
            return False
        else:
            return True
    
    def get_password(self) -> str:
        if not self.is_valid_password():
            raise ValueError('password does not match the criteria')
        return self._user_password


password = Password()
password.password_generation()

print(f'Your password is: {password.get_password()}')

