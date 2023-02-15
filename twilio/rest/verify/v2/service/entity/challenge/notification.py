"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Verify
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



class NotificationList(ListResource):

    def __init__(self, version: Version, service_sid: str, identity: str, challenge_sid: str):
        """
        Initialize the NotificationList
        :param Version version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Service.
        :param identity: Customer unique identity for the Entity owner of the Challenge. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.
        :param challenge_sid: The unique SID identifier of the Challenge.
        
        :returns: twilio.verify.v2.notification..NotificationList
        :rtype: twilio.verify.v2.notification..NotificationList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'identity': identity, 'challenge_sid': challenge_sid,  }
        self._uri = '/Services/${service_sid}/Entities/${identity}/Challenges/${challenge_sid}/Notifications'.format(**self._solution)


    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.NotificationList>'



class NotificationInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str, identity: str, challenge_sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'service_sid' : payload.get('service_sid'),
            'entity_sid' : payload.get('entity_sid'),
            'identity' : payload.get('identity'),
            'challenge_sid' : payload.get('challenge_sid'),
            'priority' : payload.get('priority'),
            'ttl' : payload.get('ttl'),
            'date_created' : payload.get('date_created'),
        }

        self._context = None
        self._solution = {
            'service_sid': service_sid or self._properties['service_sid'],'identity': identity or self._properties['identity'],'challenge_sid': challenge_sid or self._properties['challenge_sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = NotificationContext(
                self._version,
                service_sid=self._solution['service_sid'],identity=self._solution['identity'],challenge_sid=self._solution['challenge_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.NotificationInstance {}>'.format(context)



