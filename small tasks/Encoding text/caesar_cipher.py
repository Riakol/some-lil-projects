class Caesar_Cipher:
    def __init__(self, text, mode, language):
        self.text = text
        self.mode = mode
        self.language = language

    def encoding(self):
        def choose_language(lang, sym, shift=14):
            if lang == 'ru':
                if 'А' <= sym <= 'Я':
                    return chr(((ord(sym) + shift - ord('А')) % 32) + ord('А'))
                elif 'а' <= sym <= 'я':
                    return chr(((ord(sym) + shift - ord('а')) % 32) + ord('а'))
                else:
                    # here is the letter ё
                    return sym
            elif lang == 'en':
                if 'A' <= sym <= 'Z':
                    return chr(((ord(sym) + shift - ord('A')) % 26) + ord('A'))
                elif 'a' <= sym <= 'z':
                    return chr(((ord(sym) + shift - ord('a')) % 26) + ord('a'))

        def shift(sym, shift=14):
            if self.mode.startswith('e'):
                return choose_language(self.language, sym, shift)
            elif self.mode.startswith('d'):
                return choose_language(self.language, sym, -shift)

        try:
            translated = map(lambda x: shift(x) if x.isalpha() else x, self.text)
            return ''.join(translated)
        except TypeError:
            raise ValueError(f'The letters entered are not part of the {self.language} language')


def get_choice(prompt, options):
    while True:
        response = input(prompt).lower()
        if response in options:
            return response
        print(f'Please enter one of the following options: {", ".join(options)}')


mode = get_choice('Do you want to (e)ncrypt or (d)ecrypt? ', ['e', 'd'])
language = get_choice('What kind of language do you prefer: (Rus)sian or (Eng)lish? ', ['ru', 'en'])

message = input('Enter the message\n> ')

print(Caesar_Cipher(message, mode, language).encoding())
