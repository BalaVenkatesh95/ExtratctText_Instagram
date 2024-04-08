"""
 Test case file with all required test cases to execute
"""
import time

from ExtractText_functions import ExtractClass
import pytest



url = "https://www.instagram.com/guviofficial/"
#Creating Instance of SauceDemoClass to utilise its methods / functions
extract = ExtractClass(url)

# Test case to navigate to URL
def test_navigate_url():
   testing_url = "https://www.instagram.com/guviofficial/"
   assert extract.fetch_url() == testing_url
print("Landed on login page")

# Test to extract text
def test_extract_text():
   extract.extract_text()


#Test Case to quit / shutdown browser
def test_shutdown():
   extract.shutdown()
