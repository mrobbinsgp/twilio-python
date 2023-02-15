"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Routes
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



class SipDomainList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the SipDomainList
        :param Version version: Version that contains the resource
        
        :returns: twilio.routes.v2.sip_domain..SipDomainList
        :rtype: twilio.routes.v2.sip_domain..SipDomainList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = ''.format(**self._solution)


    
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Routes.V2.SipDomainList>'


class SipDomainContext(InstanceContext):
    def __init__(self, version: Version, sip_domain: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'sip_domain': sip_domain,  }
        self._uri = '/SipDomains/${sip_domain}'
        
    
    def fetch(self):
        
        """
        Fetch the SipDomainInstance

        :returns: The fetched SipDomainInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return SipDomainInstance(self._version, payload, sip_domain=self._solution['sip_domain'], )
        

        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return SipDomainInstance(self._version, payload, sip_domain=self._solution['sip_domain'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Routes.V2.SipDomainContext>'



class SipDomainInstance(InstanceResource):
    def __init__(self, version, payload, sip_domain: str):
        super().__init__(version)
        self._properties = { 
            'sip_domain' : payload.get('sip_domain'),
            'url' : payload.get('url'),
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'friendly_name' : payload.get('friendly_name'),
            'voice_region' : payload.get('voice_region'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
        }

        self._context = None
        self._solution = {
            'sip_domain': sip_domain or self._properties['sip_domain'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = SipDomainContext(
                self._version,
                sip_domain=self._solution['sip_domain'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Routes.V2.SipDomainInstance {}>'.format(context)



