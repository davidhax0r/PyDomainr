**PyDomainr**
==============
PyDomainr is a python wrapper for the domai.nr JSON API.

###Installation:
```python
pip install https://github.com/itsnauman/PyDomainr/archive/0.1.tar.gz
```

###Usage:
####1 Check For Availability Of Domain:
The URL of the domain is passed in the construct
```python
from pydomainr import PyDomainr
dom = PyDomainr("google.com")
print dom.is_available
```

####2 Get Whois URL:
This will return the Whois URL of the domain
```python
from pydomainr import PyDomainr
dom = PyDomainr("google.com")
print dom.whois_url
```
