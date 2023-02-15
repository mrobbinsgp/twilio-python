"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Oauth
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class TokenList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the TokenList
        :param Version version: Version that contains the resource
        
        :returns: twilio.oauth.v1.token..TokenList
        :rtype: twilio.oauth.v1.token..TokenList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/token'.format(**self._solution)


    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Oauth.V1.TokenList>'



class TokenInstance(InstanceResource):
    def __init__(self, version, payload):
        super().__init__(version)
        self._properties = { 
            'access_token' : payload.get('access_token'),
            'refresh_token' : payload.get('refresh_token'),
            'id_token' : payload.get('id_token'),
            'refresh_token_expires_at' : payload.get('refresh_token_expires_at'),
            'access_token_expires_at' : payload.get('access_token_expires_at'),
        }

        self._context = None
        self._solution = {
            
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = TokenContext(
                self._version,
                
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Oauth.V1.TokenInstance {}>'.format(context)



