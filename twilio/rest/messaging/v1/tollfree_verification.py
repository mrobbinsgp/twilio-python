"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Messaging
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


class TollfreeVerificationList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the TollfreeVerificationList
        :param Version version: Version that contains the resource
        
        :returns: twilio.messaging.v1.tollfree_verification..TollfreeVerificationList
        :rtype: twilio.messaging.v1.tollfree_verification..TollfreeVerificationList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Tollfree/Verifications'.format(**self._solution)


    
    
    
    
    def stream(self, tollfree_phone_number_sid=values.unset, status=values.unset, limit=None, page_size=None):
        """
        Streams TollfreeVerificationInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str tollfree_phone_number_sid: The SID of the Phone Number associated with the Tollfree Verification.
        :param TollfreeVerificationStatus status: The compliance status of the Tollfree Verification record.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.messaging.v1.tollfree_verification.TollfreeVerificationInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            tollfree_phone_number_sid=tollfree_phone_number_sid,
            status=status,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, tollfree_phone_number_sid=values.unset, status=values.unset, limit=None, page_size=None):
        """
        Lists TollfreeVerificationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str tollfree_phone_number_sid: The SID of the Phone Number associated with the Tollfree Verification.
        :param TollfreeVerificationStatus status: The compliance status of the Tollfree Verification record.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.messaging.v1.tollfree_verification.TollfreeVerificationInstance]
        """
        return list(self.stream(
            tollfree_phone_number_sid=tollfree_phone_number_sid,
            status=status,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, tollfree_phone_number_sid=values.unset, status=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of TollfreeVerificationInstance records from the API.
        Request is executed immediately
        
        :param str tollfree_phone_number_sid: The SID of the Phone Number associated with the Tollfree Verification.
        :param TollfreeVerificationStatus status: The compliance status of the Tollfree Verification record.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of TollfreeVerificationInstance
        :rtype: twilio.rest.messaging.v1.tollfree_verification.TollfreeVerificationPage
        """
        data = values.of({ 
            'TollfreePhoneNumberSid': tollfree_phone_number_sid,
            'Status': status,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return TollfreeVerificationPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of TollfreeVerificationInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of TollfreeVerificationInstance
        :rtype: twilio.rest.messaging.v1.tollfree_verification.TollfreeVerificationPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return TollfreeVerificationPage(self._version, response, self._solution)


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.TollfreeVerificationList>'








class TollfreeVerificationPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the TollfreeVerificationPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.messaging.v1.tollfree_verification.TollfreeVerificationPage
        :rtype: twilio.rest.messaging.v1.tollfree_verification.TollfreeVerificationPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of TollfreeVerificationInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.messaging.v1.tollfree_verification.TollfreeVerificationInstance
        :rtype: twilio.rest.messaging.v1.tollfree_verification.TollfreeVerificationInstance
        """
        return TollfreeVerificationInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.TollfreeVerificationPage>'





class TollfreeVerificationContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'sid': sid,  }
        self._uri = '/Tollfree/Verifications/${sid}'
        
    
    def fetch(self):
        
        """
        Fetch the TollfreeVerificationInstance

        :returns: The fetched TollfreeVerificationInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return TollfreeVerificationInstance(self._version, payload, sid=self._solution['sid'], )
        

        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return TollfreeVerificationInstance(self._version, payload, sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.TollfreeVerificationContext>'



class TollfreeVerificationInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'customer_profile_sid' : payload.get('customer_profile_sid'),
            'trust_product_sid' : payload.get('trust_product_sid'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'regulated_item_sid' : payload.get('regulated_item_sid'),
            'business_name' : payload.get('business_name'),
            'business_street_address' : payload.get('business_street_address'),
            'business_street_address2' : payload.get('business_street_address2'),
            'business_city' : payload.get('business_city'),
            'business_state_province_region' : payload.get('business_state_province_region'),
            'business_postal_code' : payload.get('business_postal_code'),
            'business_country' : payload.get('business_country'),
            'business_website' : payload.get('business_website'),
            'business_contact_first_name' : payload.get('business_contact_first_name'),
            'business_contact_last_name' : payload.get('business_contact_last_name'),
            'business_contact_email' : payload.get('business_contact_email'),
            'business_contact_phone' : payload.get('business_contact_phone'),
            'notification_email' : payload.get('notification_email'),
            'use_case_categories' : payload.get('use_case_categories'),
            'use_case_summary' : payload.get('use_case_summary'),
            'production_message_sample' : payload.get('production_message_sample'),
            'opt_in_image_urls' : payload.get('opt_in_image_urls'),
            'opt_in_type' : payload.get('opt_in_type'),
            'message_volume' : payload.get('message_volume'),
            'additional_information' : payload.get('additional_information'),
            'tollfree_phone_number_sid' : payload.get('tollfree_phone_number_sid'),
            'status' : payload.get('status'),
            'url' : payload.get('url'),
            'resource_links' : payload.get('resource_links'),
            'external_reference_id' : payload.get('external_reference_id'),
        }

        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = TollfreeVerificationContext(
                self._version,
                sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Messaging.V1.TollfreeVerificationInstance {}>'.format(context)



