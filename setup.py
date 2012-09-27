import os
from   setuptools import setup
from   tldtosms   import constants

setup(
    name                = "tldtosms",
    version             = constants.PACKAGE_VERSION,
    description         = "Notify yourself by SMS when new TLD becomes available",
    author              = "Nevio Vesic",
    author_email        = "nevio.vesic@gmail.com",
    license             = "MIT",
    url                 = "http://0x19.github.com/tldtosms/",
    keywords            = ["telapi", "sms", "telephony", "python", "tld", "domains", "whois"],
    install_requires    = ["requests", "telapi"],
    packages            = ['tldtosms', 'tldtosms.sync', 'tldtosms.exceptions'],
    classifiers         = [
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Telephony",
        "Topic :: Internet",
        "Topic :: System :: Networking",
        "Topic :: Internet :: WWW/HTTP"
    ],
    long_description    = """This library interacts with the TelAPI service. It allows you to send yourself new sms each time new tld is available on world wide web. Check out http://telapi.com for free credits.""",
)
