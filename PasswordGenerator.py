import string
import random


class PasswordGenerator:
    upper_case_chars = string.ascii_uppercase
    lower_case_chars = string.ascii_lowercase
    digits = string.digits
    punctuations = string.punctuation

    def __init__(self):
        self.include_upper_chars = True
        self.include_lower_case_chars = True
        self.include_digits = True
        self.include_punctuations = True
        self.length = 10
        self.__password = ''

    def user_preferences(self):
        self.length = int(input("Enter the desired length of the password: "))
        self.include_upper_chars = input(
            "Include uppercase letters? (y/n): ").lower() == 'y'
        self.include_lower_case_chars = input(
            "Include lowercase letters? (y/n): ").lower() == 'y'
        self.include_digits = input("Include digits? (y/n): ").lower() == 'y'
        self.include_punctuations = input(
            "Include special characters? (y/n): ").lower() == 'y'

    def __preference_characters(self):
        chars = ''
        if self.include_lower_case_chars:
            chars += self.lower_case_chars
        if self.include_upper_chars:
            chars += self.upper_case_chars
        if self.include_digits:
            chars += self.digits
        if self.punctuations:
            chars += self.punctuations
        return chars

    def generate_password(self):
        self.__password = ''.join(random.choice(self.__preference_characters())
                                  for _ in range(self.length))

    def get_password(self):
        return self.__password

    def __repr__(self):
        return self.__password
