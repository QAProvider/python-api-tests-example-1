# How to write a first API test with Python + Pytest + Allure

**library** is a package that sends API request and has all the stuff for Allure report

**test_github.py** is a file with 2 tests: test_success, test_failed

## How to use ##

Being in the folder containing tests folder run pytests:

$ pytest --alluredir=allure_results

Serve results with Allure:

$ allure server allure_results/ 

## Full description ##

https://qaprovider.com/discussion/show/api-testing-with-python-pytest-allure/79
