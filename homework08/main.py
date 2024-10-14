# Написать программу на Python, которая проверяет вводимый пользователем пароль на сложность:
# — не менее 8 символов
# — наличие прописных и строчных букв
# — наличие цифр
# и переводит его в хэш-значение.
import re
import hashlib

def lengthMoreEight(string) :
    return len(string) >= 8

def hasSmallBigLetters(string) :
    smallLetterPattern = re.compile(".*[a-z].*")
    bigLetterPattern = re.compile(".*[A-Z].*")
    return smallLetterPattern.match(string) != None and bigLetterPattern.match(string) != None

def hasDigits(string) :
    pattern = re.compile(".*[0-9].*")
    return pattern.match(string) != None

def prompt(message) :
    print(message)
    return input()

pass_str = prompt("Введите пароль: ")

if (not lengthMoreEight(pass_str)) :
    exit("Длина пароля менее 8 символов!")

if (not hasSmallBigLetters(pass_str)) :
    exit("Пароль должен содержать строчные и заглавные буквы!")

if (not hasDigits(pass_str)) :
    exit("Пароль должен содержать цифры!")

print(hashlib.md5(pass_str.encode('utf8')).hexdigest())