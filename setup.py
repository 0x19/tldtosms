from distutils.core import setup
import os
from tldtosms import VERSION

setup(
    name                = "tldtosms",
    version             = VERSION,
    description         = "",
    author              = "Nevio Vesic",
    author_email        = "nevio.vesic@gmail.com",
    url                 = "https://github.com/0x19/tldtosms/",
    keywords            = ["telapi", "sms", "telephony", "python", "top-level", "tld", "sld", "domains", "whois"],
    install_requires    = ["requests", "telapi", "difflib"],
    packages            = ['tldtosms', 'tldtosms.sync', 'tldtosms.exceptions', 'tldtosms.settings'],
    package_data        = {'tldtosms': ['data/*.dat', 'data/*.json']},
    classifiers         = [
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Telephony",
    	"Topic :: Domains :: Top Level Domains",
    	"Topic :: Domains :: Whois"
    ],
    long_description    = """This library interacts with the TelAPI service. It allows you to send yourself new sms each time new tld is available on world wide web. Check out http://telapi.com for free credits.""",
)
