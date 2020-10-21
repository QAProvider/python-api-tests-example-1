import requests
import pytest
import allure

@allure.step('REQUEST')
def send_request(method, url, headers = {}):
    if method == 'GET':
        response = requests.get(url, headers=headers)
        allure.attach(response.content, 'RESPONSE', allure.attachment_type.JSON)
        return response

    raise Exception('Method not found: ' + method)