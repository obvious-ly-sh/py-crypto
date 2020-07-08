from random import randint, choice


class Crypto():

    def __init__(self):
        self.chars = "aezriuytpofqdskhjgmlvcxwnbAEZRITUYPODFQSJKGHMLVCWXNB123456789"
        self.patterns = "@.$+=-*/;?,:!%'&~_[](){}\\§\"`|#²"

    def encrypt(self, clear_content: str, key: str, salt: int = 0) -> str:
        encrypted_content = ""
        key_index = 0

        for content_char in clear_content:
            if (key_index == len(key)):
                key_index = 0
            encrypted_content += str(ord(content_char) + salt +
                                     ord(key[key_index]) + salt) + choice(self.patterns)
            if (randint(0, 1) == 1):
                last = 0
                if (randint(0, 1) == 1):
                    choice(self.patterns)
                    last = 1
                if (randint(0, 1) == 1 and last == 0):
                    choice(self.patterns)
                    last = 0
                if (randint(0, 1) == 1 and last == 1):
                    choice(self.patterns)
                    last = 0
            key_index += 1

        return encrypted_content

    def decrypt(self, encrypted_content: str, key: str, salt: int = 0) -> (str, list):
        clear_content = ""
        token = ""
        tokens = []
        for char in encrypted_content:
            if (char in self.patterns):
                tokens.append(int(token))
                token = ""
            else:
                token += char

        key_index = 0
        for token in tokens:
            if (key_index == len(key)):
                key_index = 0
            clear_content += chr(token - salt - ord(key[key_index]) - salt)
            key_index += 1

        return (clear_content, tokens)

    def gen_key(self, length: int) -> str:
        key = ""
        for _ in range(length):
            key += choice(self.chars + self.patterns)
        return key
