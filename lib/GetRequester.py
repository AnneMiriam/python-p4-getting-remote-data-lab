import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        # !👇🏻 this way also passed the tests
        # json_list = []
        # lists = json.loads(self.get_response_body())
        # for list in lists:
        #     json_list.append(list)
        # return json_list
        return json.loads(self.get_response_body())