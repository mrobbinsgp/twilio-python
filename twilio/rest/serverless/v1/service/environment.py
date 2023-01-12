"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Serverless
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

from twilio.rest.environment.deployment import DeploymentListInstancefrom twilio.rest.environment.log import LogListInstancefrom twilio.rest.environment.variable import VariableListInstance


class EnvironmentContext(InstanceContext):
    def __init__(self, version: V1, service_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super(EnvironmentContextList, self).__init__(version)

        # Path Solution
        self._solution = { service_sid, sid,  }
        self._uri = '/Services/${service_sid}/Environments/${sid}'
        
        self._deployments = None
        self._logs = None
        self._variables = None
        
        def delete(self):
            
            
            """
            Deletes the EnvironmentInstance

            :returns: True if delete succeeds, False otherwise
            :rtype: bool
            """
            return self._version.delete(method='DELETE', uri=self._uri, )
        
        def fetch(self):
            
            """
            Fetch the EnvironmentInstance

            :returns: The fetched EnvironmentInstance
            #TODO: add rtype docs
            """
            payload = self._version.fetch(method='GET', uri=self._uri, )
            return EnvironmentInstance(
                self._version,
                payload,
                service_sidsid=self._solution['service_sid''sid'],
            )
            
            
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.EnvironmentContext>'



class EnvironmentInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str, sid: str):
        super(EnvironmentInstance, self).__init__(version)
        self._properties = { 
            'sid' = payload.get('sid'),
            'account_sid' = payload.get('account_sid'),
            'service_sid' = payload.get('service_sid'),
            'build_sid' = payload.get('build_sid'),
            'unique_name' = payload.get('unique_name'),
            'domain_suffix' = payload.get('domain_suffix'),
            'domain_name' = payload.get('domain_name'),
            'date_created' = payload.get('date_created'),
            'date_updated' = payload.get('date_updated'),
            'url' = payload.get('url'),
            'links' = payload.get('links'),
        }

        self._context = None
        self._solution = {
            'service_sid': service_sid or self._properties['service_sid']'sid': sid or self._properties['sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = EnvironmentContext(
                self._version,
                service_sid=self._solution['service_sid'],sid=self._solution['sid'],
            )
        return self._context

    @property
    def deployments(self):
        return self._proxy.deployments
    @property
    def logs(self):
        return self._proxy.logs
    @property
    def variables(self):
        return self._proxy.variables
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.EnvironmentInstance {}>'.format(context)



class EnvironmentListInstance(ListResource):
    def __init__(self, version: V1, service_sid: str):
        # TODO: needs autogenerated docs
        super(EnvironmentListInstanceList, self).__init__(version)

        # Path Solution
        self._solution = { service_sid,  }
        self._uri = '/Services/${service_sid}/Environments'
        
        
        def create(self, body):
            data = values.of({
                'body': body,
            })

            payload = self._version.create(method='post', uri=self._uri, data=data, )

            return EnvironmentInstance(self._version, payload, service_sid=self._solution['service_sid'])
            
        
        def page(self, page_size):
            
            data = values.of({
                'page_size': page_size,
            })

            payload = self._version.create(method='get', uri=self._uri, data=data, )

            return EnvironmentPage(self._version, payload, service_sid=self._solution['service_sid'])
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.EnvironmentListInstance>'

