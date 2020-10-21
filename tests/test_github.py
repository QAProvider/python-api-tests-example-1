from library import request
import allure

def test_success():
    with allure.step('users/:username'):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

        response = request.send_request('GET', "https://api.github.com/users/qaprovider", headers)
        assert response.status_code == 200
        response_body = response.json()
        assert response_body["login"] == 'QAProvider'
        assert response_body["id"] == 55697246

def test_failed():
    with allure.step('users/:username'):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

        response = request.send_request('GET', "https://api.github.com/users/qaprovider", headers)
        assert response.status_code == 200
        response_body = response.json()
        assert response_body["login"] == 'WRONG_USERNAME'