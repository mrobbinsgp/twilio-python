"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Sync
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

from twilio.rest.sync_list.sync_list_item import SyncListItemListInstancefrom twilio.rest.sync_list.sync_list_permission import SyncListPermissionListInstance


class SyncListContext(InstanceContext):
    def __init__(self, version: V1, service_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super(SyncListContextList, self).__init__(version)

        # Path Solution
        self._solution = { service_sid, sid,  }
        self._uri = '/Services/${service_sid}/Lists/${sid}'
        
        self._sync_list_items = None
        self._sync_list_permissions = None
        
        def delete(self):
            
            
            """
            Deletes the SyncListInstance

            :returns: True if delete succeeds, False otherwise
            :rtype: bool
            """
            return self._version.delete(method='DELETE', uri=self._uri, )
        
        def fetch(self):
            
            """
            Fetch the SyncListInstance

            :returns: The fetched SyncListInstance
            #TODO: add rtype docs
            """
            payload = self._version.fetch(method='GET', uri=self._uri, )
            return SyncListInstance(
                self._version,
                payload,
                service_sidsid=self._solution['service_sid''sid'],
            )
            
            
        
        def update(self, body):
            data = values.of({
                'body': body,
            })

            payload = self._version.update(method='post', uri=self._uri, data=data, )

            return SyncListInstance(self._version, payload, service_sid=self._solution['service_sid'], sid=self._solution['sid'], )
            
            
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.SyncListContext>'



class SyncListInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str, sid: str):
        super(SyncListInstance, self).__init__(version)
        self._properties = { 
            'sid' = payload.get('sid'),
            'unique_name' = payload.get('unique_name'),
            'account_sid' = payload.get('account_sid'),
            'service_sid' = payload.get('service_sid'),
            'url' = payload.get('url'),
            'links' = payload.get('links'),
            'revision' = payload.get('revision'),
            'date_expires' = payload.get('date_expires'),
            'date_created' = payload.get('date_created'),
            'date_updated' = payload.get('date_updated'),
            'created_by' = payload.get('created_by'),
        }

        self._context = None
        self._solution = {
            'service_sid': service_sid or self._properties['service_sid']'sid': sid or self._properties['sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = SyncListContext(
                self._version,
                service_sid=self._solution['service_sid'],sid=self._solution['sid'],
            )
        return self._context

    @property
    def sync_list_items(self):
        return self._proxy.sync_list_items
    @property
    def sync_list_permissions(self):
        return self._proxy.sync_list_permissions
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.SyncListInstance {}>'.format(context)



class SyncListListInstance(ListResource):
    def __init__(self, version: V1, service_sid: str):
        # TODO: needs autogenerated docs
        super(SyncListListInstanceList, self).__init__(version)

        # Path Solution
        self._solution = { service_sid,  }
        self._uri = '/Services/${service_sid}/Lists'
        
        
        def create(self, body):
            data = values.of({
                'body': body,
            })

            payload = self._version.create(method='post', uri=self._uri, data=data, )

            return SyncListInstance(self._version, payload, service_sid=self._solution['service_sid'])
            
        
        def page(self, page_size):
            
            data = values.of({
                'page_size': page_size,
            })

            payload = self._version.create(method='get', uri=self._uri, data=data, )

            return SyncListPage(self._version, payload, service_sid=self._solution['service_sid'])
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.SyncListListInstance>'

