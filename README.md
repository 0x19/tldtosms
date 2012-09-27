### Welcome to TLD to SMS
TLD to SMS is a python package designed to help you with being notified on new TLD as soon as TLD becomes public. How plugin notifies you is by sending SMS message to your mobile phone or any other number that you provide.

#### Requirements

- You need to have [TelAPI account](http://telapi.com)
- You must install package ( obviously lol ) Python 2.6+

#### By GitHub clone

```shell
$ cd ~
$ git clone https://github.com/0x19/tldtosms.git
$ cd tldtosms
$ python setup.py install
```

#### By PIP

```shell
$ not available for now - will register it soon
```

### Step by step installation

**1.) Run the package installation**

You can choose one of the approaches defined above.  

**2.) navigate yourself to examples**

You can find them at [TLD to SMS Examples](https://github.com/0x19/tldtosms/tree/master/examples)

**3.) Open `run_on_demand.py` example and modify following code**

```python
tts_connect = Connect(
    telapi_account_sid = 'account_sid',
    telapi_auth_token  = 'auth_token',
    from_address       = 'from_e164_number',
    to_address         = 'to_e164_number',
    cache_file         = '/full/path/to/tldtosms_cache.dat'
)
```

- `telapi_account_sid` : Can be found at [TelAPI Dashboard](https://telapi.com/dashboard)
- `telapi_auth_token`  : Can be found at [TelAPI Dashboard](https://telapi.com/dashboard)
- `from_address`       : You need to own [TelAPI Number](https://www.telapi.com/numbers/)
- `to_address`         : Your mobile phone number in E.164 format e.g. +1 555 555 5555
- `cache_file`         : Just path to `.dat` file where we can cache stuff out

**4.) Save the example `run_on_demand.py` and run it**
It's pretty easy to run the file now. Just do:

```shell
python run_on_demand.py
```

**And that's it :) For more details about usage please wait for me or contact me by:**

### Need more info?
Create new [Github ticket](https://github.com/0x19/tldtosms/issues) and I'll make sure it gets solved ASAP!

### Contact
You can always reach me at few places :)

**E-mail:**   nevio.vesic@gmail.com - 
**Facebook:** https://www.facebook.com/noxten - 
**Linkedin:** http://www.linkedin.com/in/neviovesic - 
**Twitter:**  https://twitter.com/vesicnevio