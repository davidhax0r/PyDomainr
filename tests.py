from pydomainr import PyDomainr
dom = PyDomainr("naumanahmad.com")
for i in dom.taken_domains():
    print i
