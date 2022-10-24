from colorama import init, Fore, Back, Style
# colorama convert those ANSI sequences to also work on Windows
from termcolor import colored
init()


# original text 
print('Hello, world!')
print(Fore.RED + 'Hello, world!')  # print in red using colorama

print(colored('Hello, world!', 'green'))
print(colored('Hello, world!', 'red'))
print(colored('Hello, world!', 'yellow'))
print(colored('Hello, world!', 'blue'))

a = [1,2,3]
b = a
a = [4,5,6]