import logging
import re
import functools

class memoized(object):
   '''Decorator. Caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned 
   (not reevaluated).
   '''
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      try:
         return self.cache[args]
      except KeyError:
         value = self.func(*args)
         self.cache[args] = value
         return value
      except TypeError:
         # uncachable -- for instance, passing a list as an argument.
         # Better to not cache than to blow up entirely.
         return self.func(*args)
   def __repr__(self):
      '''Return the function's docstring.'''
      return self.func.__doc__
   def __get__(self, obj, objtype):
      '''Support instance methods.'''
      return functools.partial(self.__call__, obj)


phone_number_filter = re.compile('[^\+0-9]')

@memoized
def filter_e164(phone_number):

     if not phone_number:
         return ''

     phone_number = phone_number.strip()

     if '@' in phone_number:
         logging.debug('This is a SIP address')
         return phone_number

     phone_number = phone_number_filter.sub('', phone_number)

     logging.debug('Cleaned number: %s', phone_number)

     if re.match('^\+[1-9][0-9]{5,20}$', phone_number):
         logging.debug('Number is good to go')
         return phone_number
     elif re.match('^1[2-9][0-9]{9}$', phone_number):
         logging.debug('Adding a +')
         return '+' + phone_number
     elif re.match('^[2-9][0-9]{9}$', phone_number):
         logging.debug('Adding a +1')
         return '+1' + phone_number
     elif re.match('^011[2-9][0-9]{5,20}$', phone_number):
         logging.debug('US -> Int\'l (011)')
         return re.sub('^011', '', phone_number)
     elif re.match('^[2-9][0-9]{5,20}$', phone_number):
         logging.debug('Int\'l. Adding a +')
         return '+' + phone_number
     else:
         return ''

@memoized
def validate_e164(phone_number):
    return filter_e164(phone_number) != ''