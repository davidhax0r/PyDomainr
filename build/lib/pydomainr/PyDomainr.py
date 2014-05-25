import requests


class PyDomainr(object):

    def __init__(self, domain):
        """
        Prepare the API urls
        """
        self.DOMAIN = domain
        self.SEARCH = "https://domai.nr/api/json/search?q=" + self.DOMAIN
        self.INFO = "https://domai.nr/api/json/info?q=" + self.DOMAIN

    def _api_search(self):
        """
        Private method
        Store the response from the search endpoint in json_response
        """
        self.response = requests.get(self.SEARCH)
        self.json_response = self.response.json()
        return self.json_response

    def _api_info(self):
        """
        Private method
        Store the response from the info endpoint in the json_response variable
        """
        self.response = requests.get(self.INFO)
        self.json_response = self.response.json()
        return self.json_response

    @property
    def is_available(self):
        """
        Returns a booleon statement about the availability of domain
        """
        self.json_response = self._api_search()
        self.available = self.json_response['results'][0]['availability']
        if self.available == 'taken':
            return False
        elif self.available == 'available':
            return False
        else:
            #Other return types are tld or maybe
            return self.available

    @property
    def whois_url(self):
        """
        Return the Whois URL of the domain
        """
        return self._api_info()['whois_url']

    @property
    def registrar(self):
        """
        Returns the registrar's UnboundLocalError
        """
        return self._api_info()['registrars'][0]['registrar']

    @property
    def registrar_name(self):
        """
        Returns the registrars name
        """
        return self._api_info()['registrars'][0]['name']

    @property
    def register_url(self):
        return self._api_info()['registrars'][0]['register_url']

    @property
    def iana_url(self):
        return self._api_info()['tld']['iana_url']

    @property
    def domain_idna(self):
        return self._api_info()['tld']['domain_idna']

    @property
    def subdomain(self):
        return self._api_info()['subdomain']

    @property
    def domain(self):
        return self._api_info()['domain']

    @property
    def www_url(self):
        return self._api_info()['www_url']
