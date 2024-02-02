r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Proxy
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class InteractionInstance(InstanceResource):
    class ResourceStatus(object):
        ACCEPTED = "accepted"
        ANSWERED = "answered"
        BUSY = "busy"
        CANCELED = "canceled"
        COMPLETED = "completed"
        DELETED = "deleted"
        DELIVERED = "delivered"
        DELIVERY_UNKNOWN = "delivery-unknown"
        FAILED = "failed"
        IN_PROGRESS = "in-progress"
        INITIATED = "initiated"
        NO_ANSWER = "no-answer"
        QUEUED = "queued"
        RECEIVED = "received"
        RECEIVING = "receiving"
        RINGING = "ringing"
        SCHEDULED = "scheduled"
        SENDING = "sending"
        SENT = "sent"
        UNDELIVERED = "undelivered"
        UNKNOWN = "unknown"

    class Type(object):
        MESSAGE = "message"
        VOICE = "voice"
        UNKNOWN = "unknown"

    """
    :ivar sid: The unique string that we created to identify the Interaction resource.
    :ivar session_sid: The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) resource.
    :ivar service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Interaction resource.
    :ivar data: A JSON string that includes the message body of message interactions (e.g. `{\"body\": \"hello\"}`) or the call duration (when available) of a call (e.g. `{\"duration\": \"5\"}`).
    :ivar type: 
    :ivar inbound_participant_sid: The SID of the inbound [Participant](https://www.twilio.com/docs/proxy/api/participant) resource.
    :ivar inbound_resource_sid: The SID of the inbound resource; either the [Call](https://www.twilio.com/docs/voice/api/call-resource) or [Message](https://www.twilio.com/docs/sms/api/message.
    :ivar inbound_resource_status: 
    :ivar inbound_resource_type: The inbound resource type. Can be [Call](https://www.twilio.com/docs/voice/api/call-resource) or [Message](https://www.twilio.com/docs/sms/api/message-resource).
    :ivar inbound_resource_url: The URL of the Twilio inbound resource
    :ivar outbound_participant_sid: The SID of the outbound [Participant](https://www.twilio.com/docs/proxy/api/participant)).
    :ivar outbound_resource_sid: The SID of the outbound resource; either the [Call](https://www.twilio.com/docs/voice/api/call-resource) or [Message](https://www.twilio.com/docs/sms/api/message-resource).
    :ivar outbound_resource_status: 
    :ivar outbound_resource_type: The outbound resource type. Can be: [Call](https://www.twilio.com/docs/voice/api/call-resource) or [Message](https://www.twilio.com/docs/sms/api/message-resource).
    :ivar outbound_resource_url: The URL of the Twilio outbound resource.
    :ivar date_created: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the Interaction was created.
    :ivar date_updated: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the resource was last updated.
    :ivar url: The absolute URL of the Interaction resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        service_sid: str,
        session_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.session_sid: Optional[str] = payload.get("session_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.data: Optional[str] = payload.get("data")
        self.type: Optional["InteractionInstance.Type"] = payload.get("type")
        self.inbound_participant_sid: Optional[str] = payload.get(
            "inbound_participant_sid"
        )
        self.inbound_resource_sid: Optional[str] = payload.get("inbound_resource_sid")
        self.inbound_resource_status: Optional["InteractionInstance.ResourceStatus"] = (
            payload.get("inbound_resource_status")
        )
        self.inbound_resource_type: Optional[str] = payload.get("inbound_resource_type")
        self.inbound_resource_url: Optional[str] = payload.get("inbound_resource_url")
        self.outbound_participant_sid: Optional[str] = payload.get(
            "outbound_participant_sid"
        )
        self.outbound_resource_sid: Optional[str] = payload.get("outbound_resource_sid")
        self.outbound_resource_status: Optional[
            "InteractionInstance.ResourceStatus"
        ] = payload.get("outbound_resource_status")
        self.outbound_resource_type: Optional[str] = payload.get(
            "outbound_resource_type"
        )
        self.outbound_resource_url: Optional[str] = payload.get("outbound_resource_url")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "service_sid": service_sid,
            "session_sid": session_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[InteractionContext] = None

    @property
    def _proxy(self) -> "InteractionContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: InteractionContext for this InteractionInstance
        """
        if self._context is None:
            self._context = InteractionContext(
                self._version,
                service_sid=self._solution["service_sid"],
                session_sid=self._solution["session_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the InteractionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the InteractionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "InteractionInstance":
        """
        Fetch the InteractionInstance


        :returns: The fetched InteractionInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "InteractionInstance":
        """
        Asynchronous coroutine to fetch the InteractionInstance


        :returns: The fetched InteractionInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Proxy.V1.InteractionInstance {}>".format(context)


class InteractionContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, session_sid: str, sid: str):
        """
        Initialize the InteractionContext

        :param version: Version that contains the resource
        :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to fetch.
        :param session_sid: The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resource to fetch.
        :param sid: The Twilio-provided string that uniquely identifies the Interaction resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "session_sid": session_sid,
            "sid": sid,
        }
        self._uri = (
            "/Services/{service_sid}/Sessions/{session_sid}/Interactions/{sid}".format(
                **self._solution
            )
        )

    def delete(self) -> bool:
        """
        Deletes the InteractionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the InteractionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> InteractionInstance:
        """
        Fetch the InteractionInstance


        :returns: The fetched InteractionInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return InteractionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            session_sid=self._solution["session_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> InteractionInstance:
        """
        Asynchronous coroutine to fetch the InteractionInstance


        :returns: The fetched InteractionInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return InteractionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            session_sid=self._solution["session_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Proxy.V1.InteractionContext {}>".format(context)


class InteractionPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> InteractionInstance:
        """
        Build an instance of InteractionInstance

        :param payload: Payload response from the API
        """
        return InteractionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            session_sid=self._solution["session_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Proxy.V1.InteractionPage>"


class InteractionList(ListResource):
    def __init__(self, version: Version, service_sid: str, session_sid: str):
        """
        Initialize the InteractionList

        :param version: Version that contains the resource
        :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) to read the resources from.
        :param session_sid: The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) to read the resources from.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "session_sid": session_sid,
        }
        self._uri = (
            "/Services/{service_sid}/Sessions/{session_sid}/Interactions".format(
                **self._solution
            )
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[InteractionInstance]:
        """
        Streams InteractionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[InteractionInstance]:
        """
        Asynchronously streams InteractionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[InteractionInstance]:
        """
        Lists InteractionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[InteractionInstance]:
        """
        Asynchronously lists InteractionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> InteractionPage:
        """
        Retrieve a single page of InteractionInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of InteractionInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return InteractionPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> InteractionPage:
        """
        Asynchronously retrieve a single page of InteractionInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of InteractionInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return InteractionPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> InteractionPage:
        """
        Retrieve a specific page of InteractionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of InteractionInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return InteractionPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> InteractionPage:
        """
        Asynchronously retrieve a specific page of InteractionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of InteractionInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return InteractionPage(self._version, response, self._solution)

    def get(self, sid: str) -> InteractionContext:
        """
        Constructs a InteractionContext

        :param sid: The Twilio-provided string that uniquely identifies the Interaction resource to fetch.
        """
        return InteractionContext(
            self._version,
            service_sid=self._solution["service_sid"],
            session_sid=self._solution["session_sid"],
            sid=sid,
        )

    def __call__(self, sid: str) -> InteractionContext:
        """
        Constructs a InteractionContext

        :param sid: The Twilio-provided string that uniquely identifies the Interaction resource to fetch.
        """
        return InteractionContext(
            self._version,
            service_sid=self._solution["service_sid"],
            session_sid=self._solution["session_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Proxy.V1.InteractionList>"
