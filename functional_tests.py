# Avoid Linting

""".

This module is going
to avoid linting crap

"""

from selenium import webdriver


BROWSER = webdriver.Firefox()
BROWSER.get('http://localhost:8000')

assert 'Django' in BROWSER.title
