'''
SOLID Design Principles
The 5 that represent SOLID are the most crucial ones a software developer should know.

Open Closed Principle
    A class / Function should be open for extension, and closed for modification
'''

## Wrong way of writing code Example

class StorageLocker():
    '''
    This class represents a storage locker and provides methods for authentication and file upload.
    '''

    def authenticate(self, client):
        '''
        Authenticates the client against the specified cloud platform.

        Parameters:
        - client (str): The name of the cloud platform to authenticate against.

        Returns:
        - str: The authenticated client name.
        '''
        if client == "aws":
            # some code to authenticate against aws
            pass
        elif client == "azure":
            # some code to authenticate against azure
            pass
        ## Issue when we add any issue cloud platform
        ## modifying existing code instead of extension violates open closed principle
        elif client == "gcp":
            # some code to authenticate against gcp
            pass
        return client


    def upload(self, client, filename):
        '''
        Uploads a file to the specified cloud platform.

        Parameters:
        - client (str): The name of the cloud platform to upload the file to.
        - filename (str): The name of the file to upload.

        Returns:
        - None
        '''
        if client == "aws":
            # some code to upload a file to aws
            pass
        elif client == "azure":
            # some code to upload a file to azure
            pass


##### Follow open closed principle

from abc import ABC, abstractmethod

class Auth(ABC):
    '''
    Abstract base class for authentication.
    '''

    @abstractmethod
    def authenticate(self):
        '''
        Abstract method to authenticate the client.

        Returns:
        - str: The authenticated client name.
        '''
        pass


class Uploader(ABC):
    '''
    Abstract base class for file upload.
    '''

    @abstractmethod
    def upload_file(self):
        '''
        Abstract method to upload a file.

        Returns:
        - str: The status code of the upload.
        '''
        pass


class Aws(Auth, Uploader):
    '''
    Class representing authentication and file upload for AWS.
    '''

    def authenticate(self):
        '''
        Authenticates the client against AWS.

        Returns:
        - str: The authenticated client name.
        '''
        # some logic to authenticate
        return "auth_client"

    def upload_file(self, filename):
        '''
        Uploads a file to AWS.

        Parameters:
        - filename (str): The name of the file to upload.

        Returns:
        - str: The status code of the upload.
        '''
        # some logic to upload
        return "status_code"


class Azure(Auth, Uploader):
    '''
    Class representing authentication and file upload for Azure.
    '''

    def authenticate(self):
        '''
        Authenticates the client against Azure.

        Returns:
        - str: The authenticated client name.
        '''
        # some logic to authenticate
        return "auth_client"

    def upload_file(self, filename):
        '''
        Uploads a file to Azure.

        Parameters:
        - filename (str): The name of the file to upload.

        Returns:
        - str: The status code of the upload.
        '''
        # some logic to upload
        return "status_code"


class Gcp(Auth, Uploader):
    '''
    Class representing authentication and file upload for GCP.
    '''

    def authenticate(self):
        '''
        Authenticates the client against GCP.

        Returns:
        - str: The authenticated client name.
        '''
        # some logic to authenticate
        return "auth_client"

    def upload_file(self, filename):
        '''
        Uploads a file to GCP.

        Parameters:
        - filename (str): The name of the file to upload.

        Returns:
        - str: The status code of the upload.
        '''
        # some logic to upload
        return "status_code"

