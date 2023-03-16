r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Conversations
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Optional
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class AddressConfigurationList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the AddressConfigurationList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.conversations.v1.address_configuration.AddressConfigurationList
        :rtype: twilio.rest.conversations.v1.address_configuration.AddressConfigurationList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = "/Configuration/Addresses".format(**self._solution)

    def create(
        self,
        type,
        address,
        friendly_name=values.unset,
        auto_creation_enabled=values.unset,
        auto_creation_type=values.unset,
        auto_creation_conversation_service_sid=values.unset,
        auto_creation_webhook_url=values.unset,
        auto_creation_webhook_method=values.unset,
        auto_creation_webhook_filters=values.unset,
        auto_creation_studio_flow_sid=values.unset,
        auto_creation_studio_retry_count=values.unset,
    ):
        """
        Create the AddressConfigurationInstance

        :param AddressConfigurationInstance.Type type:
        :param str address: The unique address to be configured. The address can be a whatsapp address or phone number
        :param str friendly_name: The human-readable name of this configuration, limited to 256 characters. Optional.
        :param bool auto_creation_enabled: Enable/Disable auto-creating conversations for messages to this address
        :param AddressConfigurationInstance.AutoCreationType auto_creation_type:
        :param str auto_creation_conversation_service_sid: Conversation Service for the auto-created conversation. If not set, the conversation is created in the default service.
        :param str auto_creation_webhook_url: For type `webhook`, the url for the webhook request.
        :param AddressConfigurationInstance.Method auto_creation_webhook_method:
        :param list[str] auto_creation_webhook_filters: The list of events, firing webhook event for this Conversation. Values can be any of the following: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationStateUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`, `onDeliveryUpdated`
        :param str auto_creation_studio_flow_sid: For type `studio`, the studio flow SID where the webhook should be sent to.
        :param int auto_creation_studio_retry_count: For type `studio`, number of times to retry the webhook request

        :returns: The created AddressConfigurationInstance
        :rtype: twilio.rest.conversations.v1.address_configuration.AddressConfigurationInstance
        """
        data = values.of(
            {
                "Type": type,
                "Address": address,
                "FriendlyName": friendly_name,
                "AutoCreation.Enabled": auto_creation_enabled,
                "AutoCreation.Type": auto_creation_type,
                "AutoCreation.ConversationServiceSid": auto_creation_conversation_service_sid,
                "AutoCreation.WebhookUrl": auto_creation_webhook_url,
                "AutoCreation.WebhookMethod": auto_creation_webhook_method,
                "AutoCreation.WebhookFilters": serialize.map(
                    auto_creation_webhook_filters, lambda e: e
                ),
                "AutoCreation.StudioFlowSid": auto_creation_studio_flow_sid,
                "AutoCreation.StudioRetryCount": auto_creation_studio_retry_count,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AddressConfigurationInstance(self._version, payload)

    async def create_async(
        self,
        type,
        address,
        friendly_name=values.unset,
        auto_creation_enabled=values.unset,
        auto_creation_type=values.unset,
        auto_creation_conversation_service_sid=values.unset,
        auto_creation_webhook_url=values.unset,
        auto_creation_webhook_method=values.unset,
        auto_creation_webhook_filters=values.unset,
        auto_creation_studio_flow_sid=values.unset,
        auto_creation_studio_retry_count=values.unset,
    ):
        """
        Asynchronously create the AddressConfigurationInstance

        :param AddressConfigurationInstance.Type type:
        :param str address: The unique address to be configured. The address can be a whatsapp address or phone number
        :param str friendly_name: The human-readable name of this configuration, limited to 256 characters. Optional.
        :param bool auto_creation_enabled: Enable/Disable auto-creating conversations for messages to this address
        :param AddressConfigurationInstance.AutoCreationType auto_creation_type:
        :param str auto_creation_conversation_service_sid: Conversation Service for the auto-created conversation. If not set, the conversation is created in the default service.
        :param str auto_creation_webhook_url: For type `webhook`, the url for the webhook request.
        :param AddressConfigurationInstance.Method auto_creation_webhook_method:
        :param list[str] auto_creation_webhook_filters: The list of events, firing webhook event for this Conversation. Values can be any of the following: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationStateUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`, `onDeliveryUpdated`
        :param str auto_creation_studio_flow_sid: For type `studio`, the studio flow SID where the webhook should be sent to.
        :param int auto_creation_studio_retry_count: For type `studio`, number of times to retry the webhook request

        :returns: The created AddressConfigurationInstance
        :rtype: twilio.rest.conversations.v1.address_configuration.AddressConfigurationInstance
        """
        data = values.of(
            {
                "Type": type,
                "Address": address,
                "FriendlyName": friendly_name,
                "AutoCreation.Enabled": auto_creation_enabled,
                "AutoCreation.Type": auto_creation_type,
                "AutoCreation.ConversationServiceSid": auto_creation_conversation_service_sid,
                "AutoCreation.WebhookUrl": auto_creation_webhook_url,
                "AutoCreation.WebhookMethod": auto_creation_webhook_method,
                "AutoCreation.WebhookFilters": serialize.map(
                    auto_creation_webhook_filters, lambda e: e
                ),
                "AutoCreation.StudioFlowSid": auto_creation_studio_flow_sid,
                "AutoCreation.StudioRetryCount": auto_creation_studio_retry_count,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AddressConfigurationInstance(self._version, payload)

    def stream(self, type=values.unset, limit=None, page_size=None):
        """
        Streams AddressConfigurationInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str type: Filter the address configurations by its type. This value can be one of: `whatsapp`, `sms`.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.conversations.v1.address_configuration.AddressConfigurationInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(type=type, page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(self, type=values.unset, limit=None, page_size=None):
        """
        Asynchronously streams AddressConfigurationInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str type: Filter the address configurations by its type. This value can be one of: `whatsapp`, `sms`.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.conversations.v1.address_configuration.AddressConfigurationInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(type=type, page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, type=values.unset, limit=None, page_size=None):
        """
        Lists AddressConfigurationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str type: Filter the address configurations by its type. This value can be one of: `whatsapp`, `sms`.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.conversations.v1.address_configuration.AddressConfigurationInstance]
        """
        return list(
            self.stream(
                type=type,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, type=values.unset, limit=None, page_size=None):
        """
        Asynchronously lists AddressConfigurationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str type: Filter the address configurations by its type. This value can be one of: `whatsapp`, `sms`.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.conversations.v1.address_configuration.AddressConfigurationInstance]
        """
        return list(
            await self.stream_async(
                type=type,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        type=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Retrieve a single page of AddressConfigurationInstance records from the API.
        Request is executed immediately

        :param str type: Filter the address configurations by its type. This value can be one of: `whatsapp`, `sms`.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AddressConfigurationInstance
        :rtype: twilio.rest.conversations.v1.address_configuration.AddressConfigurationPage
        """
        data = values.of(
            {
                "Type": type,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return AddressConfigurationPage(self._version, response, self._solution)

    async def page_async(
        self,
        type=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Asynchronously retrieve a single page of AddressConfigurationInstance records from the API.
        Request is executed immediately

        :param str type: Filter the address configurations by its type. This value can be one of: `whatsapp`, `sms`.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AddressConfigurationInstance
        :rtype: twilio.rest.conversations.v1.address_configuration.AddressConfigurationPage
        """
        data = values.of(
            {
                "Type": type,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return AddressConfigurationPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of AddressConfigurationInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AddressConfigurationInstance
        :rtype: twilio.rest.conversations.v1.address_configuration.AddressConfigurationPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return AddressConfigurationPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of AddressConfigurationInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AddressConfigurationInstance
        :rtype: twilio.rest.conversations.v1.address_configuration.AddressConfigurationPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return AddressConfigurationPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a AddressConfigurationContext

        :param sid: The SID of the Address Configuration resource. This value can be either the `sid` or the `address` of the configuration

        :returns: twilio.rest.conversations.v1.address_configuration.AddressConfigurationContext
        :rtype: twilio.rest.conversations.v1.address_configuration.AddressConfigurationContext
        """
        return AddressConfigurationContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a AddressConfigurationContext

        :param sid: The SID of the Address Configuration resource. This value can be either the `sid` or the `address` of the configuration

        :returns: twilio.rest.conversations.v1.address_configuration.AddressConfigurationContext
        :rtype: twilio.rest.conversations.v1.address_configuration.AddressConfigurationContext
        """
        return AddressConfigurationContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Conversations.V1.AddressConfigurationList>"


class AddressConfigurationPage(Page):
    def __init__(self, version, response, solution):
        """
        Initialize the AddressConfigurationPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.conversations.v1.address_configuration.AddressConfigurationPage
        :rtype: twilio.rest.conversations.v1.address_configuration.AddressConfigurationPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AddressConfigurationInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.conversations.v1.address_configuration.AddressConfigurationInstance
        :rtype: twilio.rest.conversations.v1.address_configuration.AddressConfigurationInstance
        """
        return AddressConfigurationInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Conversations.V1.AddressConfigurationPage>"


class AddressConfigurationInstance(InstanceResource):
    def __init__(self, version, payload, sid: Optional[str] = None):
        """
        Initialize the AddressConfigurationInstance

        :returns: twilio.rest.conversations.v1.address_configuration.AddressConfigurationInstance
        :rtype: twilio.rest.conversations.v1.address_configuration.AddressConfigurationInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "account_sid": payload.get("account_sid"),
            "type": payload.get("type"),
            "address": payload.get("address"),
            "friendly_name": payload.get("friendly_name"),
            "auto_creation": payload.get("auto_creation"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "url": payload.get("url"),
        }

        self._context = None
        self._solution = {
            "sid": sid or self._properties["sid"],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AddressConfigurationContext for this AddressConfigurationInstance
        :rtype: twilio.rest.conversations.v1.address_configuration.AddressConfigurationContext
        """
        if self._context is None:
            self._context = AddressConfigurationContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def account_sid(self):
        """
        :returns: The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) the address belongs to
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def type(self):
        """
        :returns: Type of Address, value can be `whatsapp` or `sms`.
        :rtype: str
        """
        return self._properties["type"]

    @property
    def address(self):
        """
        :returns: The unique address to be configured. The address can be a whatsapp address or phone number
        :rtype: str
        """
        return self._properties["address"]

    @property
    def friendly_name(self):
        """
        :returns: The human-readable name of this configuration, limited to 256 characters. Optional.
        :rtype: str
        """
        return self._properties["friendly_name"]

    @property
    def auto_creation(self):
        """
        :returns: Auto Creation configuration for the address.
        :rtype: dict
        """
        return self._properties["auto_creation"]

    @property
    def date_created(self):
        """
        :returns: The date that this resource was created.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def date_updated(self):
        """
        :returns: The date that this resource was last updated.
        :rtype: datetime
        """
        return self._properties["date_updated"]

    @property
    def url(self):
        """
        :returns: An absolute API resource URL for this address configuration.
        :rtype: str
        """
        return self._properties["url"]

    def delete(self):
        """
        Deletes the AddressConfigurationInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the AddressConfigurationInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()

    def fetch(self):
        """
        Fetch the AddressConfigurationInstance


        :returns: The fetched AddressConfigurationInstance
        :rtype: twilio.rest.conversations.v1.address_configuration.AddressConfigurationInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the AddressConfigurationInstance


        :returns: The fetched AddressConfigurationInstance
        :rtype: twilio.rest.conversations.v1.address_configuration.AddressConfigurationInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        friendly_name=values.unset,
        auto_creation_enabled=values.unset,
        auto_creation_type=values.unset,
        auto_creation_conversation_service_sid=values.unset,
        auto_creation_webhook_url=values.unset,
        auto_creation_webhook_method=values.unset,
        auto_creation_webhook_filters=values.unset,
        auto_creation_studio_flow_sid=values.unset,
        auto_creation_studio_retry_count=values.unset,
    ):
        """
        Update the AddressConfigurationInstance

        :param str friendly_name: The human-readable name of this configuration, limited to 256 characters. Optional.
        :param bool auto_creation_enabled: Enable/Disable auto-creating conversations for messages to this address
        :param AddressConfigurationInstance.AutoCreationType auto_creation_type:
        :param str auto_creation_conversation_service_sid: Conversation Service for the auto-created conversation. If not set, the conversation is created in the default service.
        :param str auto_creation_webhook_url: For type `webhook`, the url for the webhook request.
        :param AddressConfigurationInstance.Method auto_creation_webhook_method:
        :param list[str] auto_creation_webhook_filters: The list of events, firing webhook event for this Conversation. Values can be any of the following: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationStateUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`, `onDeliveryUpdated`
        :param str auto_creation_studio_flow_sid: For type `studio`, the studio flow SID where the webhook should be sent to.
        :param int auto_creation_studio_retry_count: For type `studio`, number of times to retry the webhook request

        :returns: The updated AddressConfigurationInstance
        :rtype: twilio.rest.conversations.v1.address_configuration.AddressConfigurationInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            auto_creation_enabled=auto_creation_enabled,
            auto_creation_type=auto_creation_type,
            auto_creation_conversation_service_sid=auto_creation_conversation_service_sid,
            auto_creation_webhook_url=auto_creation_webhook_url,
            auto_creation_webhook_method=auto_creation_webhook_method,
            auto_creation_webhook_filters=auto_creation_webhook_filters,
            auto_creation_studio_flow_sid=auto_creation_studio_flow_sid,
            auto_creation_studio_retry_count=auto_creation_studio_retry_count,
        )

    async def update_async(
        self,
        friendly_name=values.unset,
        auto_creation_enabled=values.unset,
        auto_creation_type=values.unset,
        auto_creation_conversation_service_sid=values.unset,
        auto_creation_webhook_url=values.unset,
        auto_creation_webhook_method=values.unset,
        auto_creation_webhook_filters=values.unset,
        auto_creation_studio_flow_sid=values.unset,
        auto_creation_studio_retry_count=values.unset,
    ):
        """
        Asynchronous coroutine to update the AddressConfigurationInstance

        :param str friendly_name: The human-readable name of this configuration, limited to 256 characters. Optional.
        :param bool auto_creation_enabled: Enable/Disable auto-creating conversations for messages to this address
        :param AddressConfigurationInstance.AutoCreationType auto_creation_type:
        :param str auto_creation_conversation_service_sid: Conversation Service for the auto-created conversation. If not set, the conversation is created in the default service.
        :param str auto_creation_webhook_url: For type `webhook`, the url for the webhook request.
        :param AddressConfigurationInstance.Method auto_creation_webhook_method:
        :param list[str] auto_creation_webhook_filters: The list of events, firing webhook event for this Conversation. Values can be any of the following: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationStateUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`, `onDeliveryUpdated`
        :param str auto_creation_studio_flow_sid: For type `studio`, the studio flow SID where the webhook should be sent to.
        :param int auto_creation_studio_retry_count: For type `studio`, number of times to retry the webhook request

        :returns: The updated AddressConfigurationInstance
        :rtype: twilio.rest.conversations.v1.address_configuration.AddressConfigurationInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
            auto_creation_enabled=auto_creation_enabled,
            auto_creation_type=auto_creation_type,
            auto_creation_conversation_service_sid=auto_creation_conversation_service_sid,
            auto_creation_webhook_url=auto_creation_webhook_url,
            auto_creation_webhook_method=auto_creation_webhook_method,
            auto_creation_webhook_filters=auto_creation_webhook_filters,
            auto_creation_studio_flow_sid=auto_creation_studio_flow_sid,
            auto_creation_studio_retry_count=auto_creation_studio_retry_count,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Conversations.V1.AddressConfigurationInstance {}>".format(
            context
        )


class AddressConfigurationContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the AddressConfigurationContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the Address Configuration resource. This value can be either the `sid` or the `address` of the configuration

        :returns: twilio.rest.conversations.v1.address_configuration.AddressConfigurationContext
        :rtype: twilio.rest.conversations.v1.address_configuration.AddressConfigurationContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Configuration/Addresses/{sid}".format(**self._solution)

    def delete(self):
        """
        Deletes the AddressConfigurationInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the AddressConfigurationInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self):
        """
        Fetch the AddressConfigurationInstance


        :returns: The fetched AddressConfigurationInstance
        :rtype: twilio.rest.conversations.v1.address_configuration.AddressConfigurationInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return AddressConfigurationInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the AddressConfigurationInstance


        :returns: The fetched AddressConfigurationInstance
        :rtype: twilio.rest.conversations.v1.address_configuration.AddressConfigurationInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return AddressConfigurationInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        friendly_name=values.unset,
        auto_creation_enabled=values.unset,
        auto_creation_type=values.unset,
        auto_creation_conversation_service_sid=values.unset,
        auto_creation_webhook_url=values.unset,
        auto_creation_webhook_method=values.unset,
        auto_creation_webhook_filters=values.unset,
        auto_creation_studio_flow_sid=values.unset,
        auto_creation_studio_retry_count=values.unset,
    ):
        """
        Update the AddressConfigurationInstance

        :param str friendly_name: The human-readable name of this configuration, limited to 256 characters. Optional.
        :param bool auto_creation_enabled: Enable/Disable auto-creating conversations for messages to this address
        :param AddressConfigurationInstance.AutoCreationType auto_creation_type:
        :param str auto_creation_conversation_service_sid: Conversation Service for the auto-created conversation. If not set, the conversation is created in the default service.
        :param str auto_creation_webhook_url: For type `webhook`, the url for the webhook request.
        :param AddressConfigurationInstance.Method auto_creation_webhook_method:
        :param list[str] auto_creation_webhook_filters: The list of events, firing webhook event for this Conversation. Values can be any of the following: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationStateUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`, `onDeliveryUpdated`
        :param str auto_creation_studio_flow_sid: For type `studio`, the studio flow SID where the webhook should be sent to.
        :param int auto_creation_studio_retry_count: For type `studio`, number of times to retry the webhook request

        :returns: The updated AddressConfigurationInstance
        :rtype: twilio.rest.conversations.v1.address_configuration.AddressConfigurationInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "AutoCreation.Enabled": auto_creation_enabled,
                "AutoCreation.Type": auto_creation_type,
                "AutoCreation.ConversationServiceSid": auto_creation_conversation_service_sid,
                "AutoCreation.WebhookUrl": auto_creation_webhook_url,
                "AutoCreation.WebhookMethod": auto_creation_webhook_method,
                "AutoCreation.WebhookFilters": serialize.map(
                    auto_creation_webhook_filters, lambda e: e
                ),
                "AutoCreation.StudioFlowSid": auto_creation_studio_flow_sid,
                "AutoCreation.StudioRetryCount": auto_creation_studio_retry_count,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AddressConfigurationInstance(
            self._version, payload, sid=self._solution["sid"]
        )

    async def update_async(
        self,
        friendly_name=values.unset,
        auto_creation_enabled=values.unset,
        auto_creation_type=values.unset,
        auto_creation_conversation_service_sid=values.unset,
        auto_creation_webhook_url=values.unset,
        auto_creation_webhook_method=values.unset,
        auto_creation_webhook_filters=values.unset,
        auto_creation_studio_flow_sid=values.unset,
        auto_creation_studio_retry_count=values.unset,
    ):
        """
        Asynchronous coroutine to update the AddressConfigurationInstance

        :param str friendly_name: The human-readable name of this configuration, limited to 256 characters. Optional.
        :param bool auto_creation_enabled: Enable/Disable auto-creating conversations for messages to this address
        :param AddressConfigurationInstance.AutoCreationType auto_creation_type:
        :param str auto_creation_conversation_service_sid: Conversation Service for the auto-created conversation. If not set, the conversation is created in the default service.
        :param str auto_creation_webhook_url: For type `webhook`, the url for the webhook request.
        :param AddressConfigurationInstance.Method auto_creation_webhook_method:
        :param list[str] auto_creation_webhook_filters: The list of events, firing webhook event for this Conversation. Values can be any of the following: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationStateUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`, `onDeliveryUpdated`
        :param str auto_creation_studio_flow_sid: For type `studio`, the studio flow SID where the webhook should be sent to.
        :param int auto_creation_studio_retry_count: For type `studio`, number of times to retry the webhook request

        :returns: The updated AddressConfigurationInstance
        :rtype: twilio.rest.conversations.v1.address_configuration.AddressConfigurationInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "AutoCreation.Enabled": auto_creation_enabled,
                "AutoCreation.Type": auto_creation_type,
                "AutoCreation.ConversationServiceSid": auto_creation_conversation_service_sid,
                "AutoCreation.WebhookUrl": auto_creation_webhook_url,
                "AutoCreation.WebhookMethod": auto_creation_webhook_method,
                "AutoCreation.WebhookFilters": serialize.map(
                    auto_creation_webhook_filters, lambda e: e
                ),
                "AutoCreation.StudioFlowSid": auto_creation_studio_flow_sid,
                "AutoCreation.StudioRetryCount": auto_creation_studio_retry_count,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AddressConfigurationInstance(
            self._version, payload, sid=self._solution["sid"]
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Conversations.V1.AddressConfigurationContext {}>".format(
            context
        )
