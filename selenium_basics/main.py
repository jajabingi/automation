import os
import webbrowser
from selenium import webdriver

os.environ['PATH'] += r"C:/selenium_drivers"
driver = webdriver.Chrome()


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')

