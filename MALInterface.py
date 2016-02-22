import requests
from requests.auth import HTTPBasicAuth

class malInterface(object):

    prefix_url = "http://myanimelist.net/api/anime/search.xml?q="

    def __init__(self, username, password):
        self.auth = HTTPBasicAuth(username, password) #user authentication

    def get_show_data(self, show):
        #format show name
        show = show.replace(" ", "+")
        show = show.lower()
        #request url
        url = self.prefix_url + show
        r = requests.get(url, auth=self.auth)
        return r.text

if __name__ == "__main__":
    interface = malInterface('malInvestigation', 'griffithdidnothingwrong10')
    print interface.get_show_data("Bleach")