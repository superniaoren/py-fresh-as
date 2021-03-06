##
import datetime as dt

class NonRepr:
    def __init__(self, beatles, click15):
        self.band_britan = beatles
        self.band_native = click15

## add __str__ and __repr__ dunder methods
## BUT, inspecting the object in the console still gives you the object's id
## __str__ is one of python's 'dunder' (double-underscore) methods and 
## gets called when you try to convert an object into a string through the various
## means that are available
class WithStr:
    def __init__(self, beatles, click15):
        self.band_britan = beatles
        self.band_native = click15

    def __str__(self):
        return f'IQIYI: {self.band_native}, my favorite.'

class WithStrRepr:
    def __init__(self, 
                 beatles : str, 
                 click15 : str):
        self.band_britan = beatles
        self.band_native = click15
    
    def __str__(self):
        return f'__str__:: IQIYI: {self.band_native}, my favorite.'

    def __repr__(self):
        return f'__repr__:: YOUKU: {self.band_native}, my favorite.'

class WithRepr:
    def __init__(self, 
                 beatles : str, 
                 click15 : str):
        self.band_britan = beatles
        self.band_native = click15

    # note, here use the !r conversion flag to make sure the output string 
    # use repr(self.band_britan) and repr(self.band_native) instead of str(self.band_britan)
    # and str(self.band_native)
    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'(UK)band({self.band_britan!r}), (CN)band({self.band_native!r}))')
    
if __name__ == '__main__':
    print("string conversion: every class needs a __repr__ : ")

    # only print class name and the id of the object instance 
    # (which is the object's memory address in CPython)
    nonrepr = NonRepr('jude', 'beidaihe')
    print(nonrepr)
    print('-' * 40)

    # with __str__
    withstr = WithStr('nov', 'penglei')
    print(withstr)
    print('-' * 40)

    # with __str__ and __repr__
    withstrrepr = WithStrRepr('stark', 'pangkuan')
    strrepr_list = [withstrrepr]
    print(withstrrepr)
    print(str(withstrrepr))
    # funny, containers like lists and dicts always use the results of __repr__ 
    # to represnet the objects they contain. Even if U call str on the container
    print(str(strrepr_list))  
    print('-' * 40)

    # use built-in function
    print(repr(withstrrepr))
    print(repr(strrepr_list))  
    print('-' * 40)

    # object's __str__ function should be readable. It meant to return a concise textual 
    # representation for human consumption
    # with __repr__, the result should be unambiguous. The resulting string is intended 
    # more as a debugging aid for developers.
    today = dt.date.today()
    print('str(today): ', str(today))
    print('repr(today): ', repr(today))
    print('-' * 40)

    # if U don't add __str__ method, Python automatically falls back on the result of 
    # __repr__ when looking for __str__.
    # so, U are recommended to add at least a __repr__ method to your classes.
    withrepr = WithRepr('Pekings', 'Rhino')
    print(withrepr)
    print('-' * 40)
    
    # python2.x, __str__ return bytes, whereas __unicode__ returns characters
    # str() call __str__, unicode() built-in calls __unicode__ if it exits.
    # e.f. return unicode(self).encode('utf-8')
