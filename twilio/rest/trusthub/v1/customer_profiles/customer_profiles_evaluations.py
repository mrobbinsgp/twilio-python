"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Trusthub
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

from twilio.base.page import Page




class CustomerProfilesEvaluationsContext(InstanceContext):
    def __init__(self, version: V1, customer_profile_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super(CustomerProfilesEvaluationsContextList, self).__init__(version)

        # Path Solution
        self._solution = { customer_profile_sid, sid,  }
        self._uri = '/CustomerProfiles/${customer_profile_sid}/Evaluations/${sid}'
        
        
        def fetch(self):
            
            """
            Fetch the CustomerProfilesEvaluationsInstance

            :returns: The fetched CustomerProfilesEvaluationsInstance
            #TODO: add rtype docs
            """
            payload = self._version.fetch(method='GET', uri=self._uri, )
            return CustomerProfilesEvaluationsInstance(
                self._version,
                payload,
                customer_profile_sidsid=self._solution['customer_profile_sid''sid'],
            )
            
            
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.CustomerProfilesEvaluationsContext>'



class CustomerProfilesEvaluationsInstance(InstanceResource):
    def __init__(self, version, payload, customer_profile_sid: str, sid: str):
        super(CustomerProfilesEvaluationsInstance, self).__init__(version)
        self._properties = { 
            'sid' = payload.get('sid'),
            'account_sid' = payload.get('account_sid'),
            'policy_sid' = payload.get('policy_sid'),
            'customer_profile_sid' = payload.get('customer_profile_sid'),
            'status' = payload.get('status'),
            'results' = payload.get('results'),
            'date_created' = payload.get('date_created'),
            'url' = payload.get('url'),
        }

        self._context = None
        self._solution = {
            'customer_profile_sid': customer_profile_sid or self._properties['customer_profile_sid']'sid': sid or self._properties['sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = CustomerProfilesEvaluationsContext(
                self._version,
                customer_profile_sid=self._solution['customer_profile_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.CustomerProfilesEvaluationsInstance {}>'.format(context)



class CustomerProfilesEvaluationsListInstance(ListResource):
    def __init__(self, version: V1, customer_profile_sid: str):
        # TODO: needs autogenerated docs
        super(CustomerProfilesEvaluationsListInstanceList, self).__init__(version)

        # Path Solution
        self._solution = { customer_profile_sid,  }
        self._uri = '/CustomerProfiles/${customer_profile_sid}/Evaluations'
        
        
        def create(self, body):
            data = values.of({
                'body': body,
            })

            payload = self._version.create(method='post', uri=self._uri, data=data, )

            return CustomerProfilesEvaluationsInstance(self._version, payload, customer_profile_sid=self._solution['customer_profile_sid'])
            
        
        def page(self, page_size):
            
            data = values.of({
                'page_size': page_size,
            })

            payload = self._version.create(method='get', uri=self._uri, data=data, )

            return CustomerProfilesEvaluationsPage(self._version, payload, customer_profile_sid=self._solution['customer_profile_sid'])
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.CustomerProfilesEvaluationsListInstance>'

