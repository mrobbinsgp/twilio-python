"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Supersim
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
from twilio.rest.supersim.v1.sim.billing_periods import BillingPeriodList
from twilio.rest.supersim.v1.sim.sim_ip_addresses import SimIpAddressList


class SimList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the SimList
        :param Version version: Version that contains the resource
        
        :returns: twilio.supersim.v1.sim..SimList
        :rtype: twilio.supersim.v1.sim..SimList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Sims'.format(**self._solution)


    
    
    
    
    def stream(self, status=values.unset, fleet=values.unset, iccid=values.unset, limit=None, page_size=None):
        """
        Streams SimInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param SimStatus status: The status of the Sim resources to read. Can be `new`, `ready`, `active`, `inactive`, or `scheduled`.
        :param str fleet: The SID or unique name of the Fleet to which a list of Sims are assigned.
        :param str iccid: The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) associated with a Super SIM to filter the list by. Passing this parameter will always return a list containing zero or one SIMs.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.sim.SimInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            status=status,
            fleet=fleet,
            iccid=iccid,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, status=values.unset, fleet=values.unset, iccid=values.unset, limit=None, page_size=None):
        """
        Lists SimInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param SimStatus status: The status of the Sim resources to read. Can be `new`, `ready`, `active`, `inactive`, or `scheduled`.
        :param str fleet: The SID or unique name of the Fleet to which a list of Sims are assigned.
        :param str iccid: The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) associated with a Super SIM to filter the list by. Passing this parameter will always return a list containing zero or one SIMs.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.sim.SimInstance]
        """
        return list(self.stream(
            status=status,
            fleet=fleet,
            iccid=iccid,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, status=values.unset, fleet=values.unset, iccid=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of SimInstance records from the API.
        Request is executed immediately
        
        :param SimStatus status: The status of the Sim resources to read. Can be `new`, `ready`, `active`, `inactive`, or `scheduled`.
        :param str fleet: The SID or unique name of the Fleet to which a list of Sims are assigned.
        :param str iccid: The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) associated with a Super SIM to filter the list by. Passing this parameter will always return a list containing zero or one SIMs.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SimInstance
        :rtype: twilio.rest.supersim.v1.sim.SimPage
        """
        data = values.of({ 
            'Status': status,
            'Fleet': fleet,
            'Iccid': iccid,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return SimPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SimInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SimInstance
        :rtype: twilio.rest.supersim.v1.sim.SimPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return SimPage(self._version, response, self._solution)


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.SimList>'








class SimPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the SimPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.supersim.v1.sim.SimPage
        :rtype: twilio.rest.supersim.v1.sim.SimPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SimInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.supersim.v1.sim.SimInstance
        :rtype: twilio.rest.supersim.v1.sim.SimInstance
        """
        return SimInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.SimPage>'





class SimContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'sid': sid,  }
        self._uri = '/Sims/${sid}'
        
        self._billing_periods = None
        self._sim_ip_addresses = None
    
    def fetch(self):
        
        """
        Fetch the SimInstance

        :returns: The fetched SimInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return SimInstance(self._version, payload, sid=self._solution['sid'], )
        

        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return SimInstance(self._version, payload, sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.SimContext>'



class SimInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'unique_name' : payload.get('unique_name'),
            'account_sid' : payload.get('account_sid'),
            'iccid' : payload.get('iccid'),
            'status' : payload.get('status'),
            'fleet_sid' : payload.get('fleet_sid'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = SimContext(
                self._version,
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def billing_periods(self):
        return self._proxy.billing_periods
    @property
    def sim_ip_addresses(self):
        return self._proxy.sim_ip_addresses
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Supersim.V1.SimInstance {}>'.format(context)



