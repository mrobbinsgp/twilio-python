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
from twilio.base.page import Page
from twilio.rest.verify.v2.entity.challenges import ChallengeList
from twilio.rest.verify.v2.entity.factors import FactorList
from twilio.rest.verify.v2.entity.new_factors import NewFactorList


class EntityList(ListResource):

    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the EntityList
        :param Version version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Service.
        
        :returns: twilio.verify.v2.entity..EntityList
        :rtype: twilio.verify.v2.entity..EntityList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid,  }
        self._uri = '/Services/${service_sid}/Entities'.format(**self._solution)


    
    
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams EntityInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.verify.v2.entity.EntityInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists EntityInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.verify.v2.entity.EntityInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of EntityInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of EntityInstance
        :rtype: twilio.rest.verify.v2.entity.EntityPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return EntityPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of EntityInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of EntityInstance
        :rtype: twilio.rest.verify.v2.entity.EntityPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return EntityPage(self._version, response, self._solution)


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.EntityList>'








class EntityPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the EntityPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.verify.v2.entity.EntityPage
        :rtype: twilio.rest.verify.v2.entity.EntityPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of EntityInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.verify.v2.entity.EntityInstance
        :rtype: twilio.rest.verify.v2.entity.EntityInstance
        """
        return EntityInstance(self._version, payload, service_sid=self._solution['service_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.EntityPage>'





class EntityContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, identity: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'identity': identity,  }
        self._uri = '/Services/${service_sid}/Entities/${identity}'
        
        self._challenges = None
        self._factors = None
        self._new_factors = None
    
    def delete(self):
        
        

        """
        Deletes the EntityInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the EntityInstance

        :returns: The fetched EntityInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return EntityInstance(self._version, payload, service_sid=self._solution['service_sid'], identity=self._solution['identity'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.EntityContext>'



class EntityInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str, identity: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'identity' : payload.get('identity'),
            'account_sid' : payload.get('account_sid'),
            'service_sid' : payload.get('service_sid'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'service_sid': service_sid or self._properties['service_sid'],'identity': identity or self._properties['identity'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = EntityContext(
                self._version,
                service_sid=self._solution['service_sid'],identity=self._solution['identity'],
            )
        return self._context

    @property
    def challenges(self):
        return self._proxy.challenges
    @property
    def factors(self):
        return self._proxy.factors
    @property
    def new_factors(self):
        return self._proxy.new_factors
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.EntityInstance {}>'.format(context)



