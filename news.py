import requests

class ApiNews:
    def __init__(self,name):
        self.name = name
    def source (self) :
        response = request.get(
            "   "
        )
        data = response.json()
        print(data)
