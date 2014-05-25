**PyDomainr**
==============
PyDomainr is a python wrapper for the domai.nr JSON API.

###Installation:
```python
pip install https://github.com/itsnauman/PyDomainr/archive/1.0.tar.gz
```

###Usage:
####1. Check For Availability Of Domain:
The URL of the domain is passed in the construct
```python
from pydomainr import PyDomainr
dom = PyDomainr("naumanahm.ad")
print dom.is_available
```

####2. Get Whois URL:
This will return the Whois URL of the domain
```python
from pydomainr import PyDomainr
dom = PyDomainr("naumanahm.ad")
print dom.whois_url
```
####3. Get A List Of Available Domains
This method will return the list of domains available
```python
from pydomainr import PyDomainr
dom = PyDomainr("naumanahm.ad")
for each_domain in dom.available_domains():
      print each_domain
````

####4. Get A list Of Domains That Are Taken
A List of taken lists are returned
```python
from pydomainr import PyDomainr
dom = PyDomainr("naumanahm.ad")
for each_domain in dom.taken_domains():
      print each_domain
````
