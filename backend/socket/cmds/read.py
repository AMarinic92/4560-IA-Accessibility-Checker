
import requests

class Read:
    def __init__(self) -> None:
        pass

    # read_web_page
    # returns web page as string
    def read_web_page(self,webpage):
        req = requests.get(webpage)
        if req.ok:
            return req.content