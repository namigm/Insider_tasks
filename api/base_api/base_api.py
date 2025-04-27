import requests


class BaseApi:

    def __init__(self, base_url, version, endpoint):
        self.base_url = base_url
        self.version = version
        self.endpoint = endpoint

    def get_method(self, params, headers=None):
        response = requests.get(url=f"{self.base_url}/{self.version}/{self.endpoint}/{params}",
                                headers=headers)
        print(response.request.url)
        return response

    def post_method(self, body, headers=None):
        response = requests.post(url=f"{self.base_url}/{self.version}/{self.endpoint}",
                                 headers=headers,
                                 json=body)
        return response

    def put_method(self, body, headers=None):
        response = requests.put(url=f"{self.base_url}/{self.version}/{self.endpoint}",
                                headers=headers,
                                json=body)
        return response

    def delete_method(self, params, headers=None):
        response = requests.delete(url=f"{self.base_url}/{self.version}/{self.endpoint}/{params}",
                                   headers=headers)
        print(response.request.url)
        return response
