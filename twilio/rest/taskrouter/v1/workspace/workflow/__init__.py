"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Taskrouter
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
from twilio.rest.taskrouter.v1.workflow.cumulative_statistics import WorkflowCumulativeStatisticsList
from twilio.rest.taskrouter.v1.workflow.real_time_statistics import WorkflowRealTimeStatisticsList
from twilio.rest.taskrouter.v1.workflow.statistics import WorkflowStatisticsList


class WorkflowList(ListResource):

    def __init__(self, version: Version, workspace_sid: str):
        """
        Initialize the WorkflowList
        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the Workflow to read.
        
        :returns: twilio.taskrouter.v1.workflow..WorkflowList
        :rtype: twilio.taskrouter.v1.workflow..WorkflowList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'workspace_sid': workspace_sid,  }
        self._uri = '/Workspaces/${workspace_sid}/Workflows'.format(**self._solution)


    
    
    
    
    
    def stream(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Streams WorkflowInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str friendly_name: The `friendly_name` of the Workflow resources to read.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.taskrouter.v1.workflow.WorkflowInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            friendly_name=friendly_name,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Lists WorkflowInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str friendly_name: The `friendly_name` of the Workflow resources to read.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.taskrouter.v1.workflow.WorkflowInstance]
        """
        return list(self.stream(
            friendly_name=friendly_name,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, friendly_name=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of WorkflowInstance records from the API.
        Request is executed immediately
        
        :param str friendly_name: The `friendly_name` of the Workflow resources to read.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of WorkflowInstance
        :rtype: twilio.rest.taskrouter.v1.workflow.WorkflowPage
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return WorkflowPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of WorkflowInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of WorkflowInstance
        :rtype: twilio.rest.taskrouter.v1.workflow.WorkflowPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return WorkflowPage(self._version, response, self._solution)


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkflowList>'










class WorkflowPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the WorkflowPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.taskrouter.v1.workflow.WorkflowPage
        :rtype: twilio.rest.taskrouter.v1.workflow.WorkflowPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of WorkflowInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.taskrouter.v1.workflow.WorkflowInstance
        :rtype: twilio.rest.taskrouter.v1.workflow.WorkflowInstance
        """
        return WorkflowInstance(self._version, payload, workspace_sid=self._solution['workspace_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkflowPage>'





class WorkflowContext(InstanceContext):
    def __init__(self, version: Version, workspace_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'workspace_sid': workspace_sid, 'sid': sid,  }
        self._uri = '/Workspaces/${workspace_sid}/Workflows/${sid}'
        
        self._cumulative_statistics = None
        self._real_time_statistics = None
        self._statistics = None
    
    def delete(self):
        
        

        """
        Deletes the WorkflowInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the WorkflowInstance

        :returns: The fetched WorkflowInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return WorkflowInstance(self._version, payload, workspace_sid=self._solution['workspace_sid'], sid=self._solution['sid'], )
        

        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return WorkflowInstance(self._version, payload, workspace_sid=self._solution['workspace_sid'], sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkflowContext>'



class WorkflowInstance(InstanceResource):
    def __init__(self, version, payload, workspace_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'assignment_callback_url' : payload.get('assignment_callback_url'),
            'configuration' : payload.get('configuration'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'document_content_type' : payload.get('document_content_type'),
            'fallback_assignment_callback_url' : payload.get('fallback_assignment_callback_url'),
            'friendly_name' : payload.get('friendly_name'),
            'sid' : payload.get('sid'),
            'task_reservation_timeout' : payload.get('task_reservation_timeout'),
            'workspace_sid' : payload.get('workspace_sid'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'workspace_sid': workspace_sid or self._properties['workspace_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = WorkflowContext(
                self._version,
                workspace_sid=self._solution['workspace_sid'],sid=self._solution['sid'],
            )
        return self._context

    @property
    def cumulative_statistics(self):
        return self._proxy.cumulative_statistics
    @property
    def real_time_statistics(self):
        return self._proxy.real_time_statistics
    @property
    def statistics(self):
        return self._proxy.statistics
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkflowInstance {}>'.format(context)



