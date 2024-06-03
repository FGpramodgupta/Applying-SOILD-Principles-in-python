'''
SOLID Design Principles
The 5 that represent SOLID are the most crucial ones a software developer should know.

Interface Segregation Principle
    Interfaces should be granularity split and be as small as possible
'''

##bad Example

class MobileDevice():
    '''
    Represents a generic mobile device.
    '''

    def voice(self):
        '''
        Raises a NotImplementedError.
        '''
        raise NotImplementedError

    def text(self):
        '''
        Raises a NotImplementedError.
        '''
        raise NotImplementedError

    def camera(self):
        '''
        Raises a NotImplementedError.
        '''
        raise NotImplementedError


class BestMobileDeviceEver(MobileDevice):
    '''
    Represents the best mobile device ever.
    '''

    def voice(self):
        '''
        Implements the voice capability.
        '''
        pass

    def text(self):
        '''
        Implements the text capability.
        '''
        pass

    def camera(self):
        '''
        Implements the camera capability.
        '''
        pass


class OldSchoolMobileDevice (MobileDevice):
    '''
    Represents an old school mobile device.
    '''

    def voice(self):
        '''
        Implements the voice capability.
        '''
        pass

    def text(self):
        '''
        Implements the text capability.
        '''
        pass

    def camera(self):
        '''
        Raises a NotImplementedError.
        This violates the Interface Segregation Principle.
        '''
        raise NotImplementedError


## Solution to comply with interface segregation code

from abc import ABC, abstractmethod

class Phone (ABC):
    '''
    Represents a phone.
    '''

    @abstractmethod
    def voice(self):
        '''
        Abstract method for voice capability.
        '''
        pass


class Text(ABC):
    '''
    Represents a text messaging capability.
    '''

    @abstractmethod
    def text_message(self): 
        '''
        Abstract method for text capability.
        '''
        pass

class Camera (ABC):
    '''
    Represents a camera capability.
    '''

    @abstractmethod
    def photo(self): 
        '''
        Abstract method for photo capability.
        '''
        pass


class BestMobilePhoneEver(Phone, Text, Camera):
    '''
    Represents the best mobile phone ever.
    '''

    def voice(self):
        '''
        Implements the voice capability.
        '''
        pass

    def text_message(self):
        '''
        Implements the text capability.
        '''
        pass

    def photo(self):
        '''
        Implements the photo capability.
        '''
        pass


class OldSchoolMobilePhoneEver(Phone, Text):
    '''
    Represents an old school mobile phone.
    '''

    def voice(self):
        '''
        Implements the voice capability.
        '''
        pass

    def text_message(self):
        '''
        Implements the text capability.
        '''
        pass


class Pager (Text):
    '''
    Represents a pager.
    '''

    def text_message(self):
        '''
        Implements the text capability.
        '''
        pass
