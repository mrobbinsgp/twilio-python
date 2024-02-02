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

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.conversations.v1.service.conversation.message.delivery_receipt import (
    DeliveryReceiptList,
)


class MessageInstance(InstanceResource):
    class OrderType(object):
        ASC = "asc"
        DESC = "desc"

    class WebhookEnabledType(object):
        TRUE = "true"
        FALSE = "false"

    """
    :ivar account_sid: The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this message.
    :ivar chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    :ivar conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
    :ivar sid: A 34 character string that uniquely identifies this resource.
    :ivar index: The index of the message within the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource).
    :ivar author: The channel specific identifier of the message's author. Defaults to `system`.
    :ivar body: The content of the message, can be up to 1,600 characters long.
    :ivar media: An array of objects that describe the Message's media, if the message contains media. Each object contains these fields: `content_type` with the MIME type of the media, `filename` with the name of the media, `sid` with the SID of the Media resource, and `size` with the media object's file size in bytes. If the Message has no media, this value is `null`.
    :ivar attributes: A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \"{}\" will be returned.
    :ivar participant_sid: The unique ID of messages's author participant. Null in case of `system` sent message.
    :ivar date_created: The date that this resource was created.
    :ivar date_updated: The date that this resource was last updated. `null` if the message has not been edited.
    :ivar delivery: An object that contains the summary of delivery statuses for the message to non-chat participants.
    :ivar url: An absolute API resource URL for this message.
    :ivar links: Contains an absolute API resource URL to access the delivery & read receipts of this message.
    :ivar content_sid: The unique ID of the multi-channel [Rich Content](https://www.twilio.com/docs/content-api) template.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        chat_service_sid: str,
        conversation_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.chat_service_sid: Optional[str] = payload.get("chat_service_sid")
        self.conversation_sid: Optional[str] = payload.get("conversation_sid")
        self.sid: Optional[str] = payload.get("sid")
        self.index: Optional[int] = deserialize.integer(payload.get("index"))
        self.author: Optional[str] = payload.get("author")
        self.body: Optional[str] = payload.get("body")
        self.media: Optional[List[object]] = payload.get("media")
        self.attributes: Optional[str] = payload.get("attributes")
        self.participant_sid: Optional[str] = payload.get("participant_sid")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.delivery: Optional[Dict[str, object]] = payload.get("delivery")
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")
        self.content_sid: Optional[str] = payload.get("content_sid")

        self._solution = {
            "chat_service_sid": chat_service_sid,
            "conversation_sid": conversation_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[MessageContext] = None

    @property
    def _proxy(self) -> "MessageContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: MessageContext for this MessageInstance
        """
        if self._context is None:
            self._context = MessageContext(
                self._version,
                chat_service_sid=self._solution["chat_service_sid"],
                conversation_sid=self._solution["conversation_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(
        self,
        x_twilio_webhook_enabled: Union[
            "MessageInstance.WebhookEnabledType", object
        ] = values.unset,
    ) -> bool:
        """
        Deletes the MessageInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
        )

    async def delete_async(
        self,
        x_twilio_webhook_enabled: Union[
            "MessageInstance.WebhookEnabledType", object
        ] = values.unset,
    ) -> bool:
        """
        Asynchronous coroutine that deletes the MessageInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
        )

    def fetch(self) -> "MessageInstance":
        """
        Fetch the MessageInstance


        :returns: The fetched MessageInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "MessageInstance":
        """
        Asynchronous coroutine to fetch the MessageInstance


        :returns: The fetched MessageInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        x_twilio_webhook_enabled: Union[
            "MessageInstance.WebhookEnabledType", object
        ] = values.unset,
        author: Union[str, object] = values.unset,
        body: Union[str, object] = values.unset,
        date_created: Union[datetime, object] = values.unset,
        date_updated: Union[datetime, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        subject: Union[str, object] = values.unset,
    ) -> "MessageInstance":
        """
        Update the MessageInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param author: The channel specific identifier of the message's author. Defaults to `system`.
        :param body: The content of the message, can be up to 1,600 characters long.
        :param date_created: The date that this resource was created.
        :param date_updated: The date that this resource was last updated. `null` if the message has not been edited.
        :param attributes: A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
        :param subject: The subject of the message, can be up to 256 characters long.

        :returns: The updated MessageInstance
        """
        return self._proxy.update(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            author=author,
            body=body,
            date_created=date_created,
            date_updated=date_updated,
            attributes=attributes,
            subject=subject,
        )

    async def update_async(
        self,
        x_twilio_webhook_enabled: Union[
            "MessageInstance.WebhookEnabledType", object
        ] = values.unset,
        author: Union[str, object] = values.unset,
        body: Union[str, object] = values.unset,
        date_created: Union[datetime, object] = values.unset,
        date_updated: Union[datetime, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        subject: Union[str, object] = values.unset,
    ) -> "MessageInstance":
        """
        Asynchronous coroutine to update the MessageInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param author: The channel specific identifier of the message's author. Defaults to `system`.
        :param body: The content of the message, can be up to 1,600 characters long.
        :param date_created: The date that this resource was created.
        :param date_updated: The date that this resource was last updated. `null` if the message has not been edited.
        :param attributes: A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
        :param subject: The subject of the message, can be up to 256 characters long.

        :returns: The updated MessageInstance
        """
        return await self._proxy.update_async(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            author=author,
            body=body,
            date_created=date_created,
            date_updated=date_updated,
            attributes=attributes,
            subject=subject,
        )

    @property
    def delivery_receipts(self) -> DeliveryReceiptList:
        """
        Access the delivery_receipts
        """
        return self._proxy.delivery_receipts

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Conversations.V1.MessageInstance {}>".format(context)


class MessageContext(InstanceContext):
    def __init__(
        self, version: Version, chat_service_sid: str, conversation_sid: str, sid: str
    ):
        """
        Initialize the MessageContext

        :param version: Version that contains the resource
        :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
        :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
        :param sid: A 34 character string that uniquely identifies this resource.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "chat_service_sid": chat_service_sid,
            "conversation_sid": conversation_sid,
            "sid": sid,
        }
        self._uri = "/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{sid}".format(
            **self._solution
        )

        self._delivery_receipts: Optional[DeliveryReceiptList] = None

    def delete(
        self,
        x_twilio_webhook_enabled: Union[
            "MessageInstance.WebhookEnabledType", object
        ] = values.unset,
    ) -> bool:
        """
        Deletes the MessageInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        headers = values.of(
            {
                "X-Twilio-Webhook-Enabled": x_twilio_webhook_enabled,
            }
        )

        return self._version.delete(method="DELETE", uri=self._uri, headers=headers)

    async def delete_async(
        self,
        x_twilio_webhook_enabled: Union[
            "MessageInstance.WebhookEnabledType", object
        ] = values.unset,
    ) -> bool:
        """
        Asynchronous coroutine that deletes the MessageInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        headers = values.of(
            {
                "X-Twilio-Webhook-Enabled": x_twilio_webhook_enabled,
            }
        )

        return await self._version.delete_async(
            method="DELETE", uri=self._uri, headers=headers
        )

    def fetch(self) -> MessageInstance:
        """
        Fetch the MessageInstance


        :returns: The fetched MessageInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return MessageInstance(
            self._version,
            payload,
            chat_service_sid=self._solution["chat_service_sid"],
            conversation_sid=self._solution["conversation_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> MessageInstance:
        """
        Asynchronous coroutine to fetch the MessageInstance


        :returns: The fetched MessageInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return MessageInstance(
            self._version,
            payload,
            chat_service_sid=self._solution["chat_service_sid"],
            conversation_sid=self._solution["conversation_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        x_twilio_webhook_enabled: Union[
            "MessageInstance.WebhookEnabledType", object
        ] = values.unset,
        author: Union[str, object] = values.unset,
        body: Union[str, object] = values.unset,
        date_created: Union[datetime, object] = values.unset,
        date_updated: Union[datetime, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        subject: Union[str, object] = values.unset,
    ) -> MessageInstance:
        """
        Update the MessageInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param author: The channel specific identifier of the message's author. Defaults to `system`.
        :param body: The content of the message, can be up to 1,600 characters long.
        :param date_created: The date that this resource was created.
        :param date_updated: The date that this resource was last updated. `null` if the message has not been edited.
        :param attributes: A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
        :param subject: The subject of the message, can be up to 256 characters long.

        :returns: The updated MessageInstance
        """
        data = values.of(
            {
                "Author": author,
                "Body": body,
                "DateCreated": serialize.iso8601_datetime(date_created),
                "DateUpdated": serialize.iso8601_datetime(date_updated),
                "Attributes": attributes,
                "Subject": subject,
            }
        )
        headers = values.of(
            {
                "X-Twilio-Webhook-Enabled": x_twilio_webhook_enabled,
            }
        )

        payload = self._version.update(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return MessageInstance(
            self._version,
            payload,
            chat_service_sid=self._solution["chat_service_sid"],
            conversation_sid=self._solution["conversation_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        x_twilio_webhook_enabled: Union[
            "MessageInstance.WebhookEnabledType", object
        ] = values.unset,
        author: Union[str, object] = values.unset,
        body: Union[str, object] = values.unset,
        date_created: Union[datetime, object] = values.unset,
        date_updated: Union[datetime, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        subject: Union[str, object] = values.unset,
    ) -> MessageInstance:
        """
        Asynchronous coroutine to update the MessageInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param author: The channel specific identifier of the message's author. Defaults to `system`.
        :param body: The content of the message, can be up to 1,600 characters long.
        :param date_created: The date that this resource was created.
        :param date_updated: The date that this resource was last updated. `null` if the message has not been edited.
        :param attributes: A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
        :param subject: The subject of the message, can be up to 256 characters long.

        :returns: The updated MessageInstance
        """
        data = values.of(
            {
                "Author": author,
                "Body": body,
                "DateCreated": serialize.iso8601_datetime(date_created),
                "DateUpdated": serialize.iso8601_datetime(date_updated),
                "Attributes": attributes,
                "Subject": subject,
            }
        )
        headers = values.of(
            {
                "X-Twilio-Webhook-Enabled": x_twilio_webhook_enabled,
            }
        )

        payload = await self._version.update_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return MessageInstance(
            self._version,
            payload,
            chat_service_sid=self._solution["chat_service_sid"],
            conversation_sid=self._solution["conversation_sid"],
            sid=self._solution["sid"],
        )

    @property
    def delivery_receipts(self) -> DeliveryReceiptList:
        """
        Access the delivery_receipts
        """
        if self._delivery_receipts is None:
            self._delivery_receipts = DeliveryReceiptList(
                self._version,
                self._solution["chat_service_sid"],
                self._solution["conversation_sid"],
                self._solution["sid"],
            )
        return self._delivery_receipts

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Conversations.V1.MessageContext {}>".format(context)


class MessagePage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> MessageInstance:
        """
        Build an instance of MessageInstance

        :param payload: Payload response from the API
        """
        return MessageInstance(
            self._version,
            payload,
            chat_service_sid=self._solution["chat_service_sid"],
            conversation_sid=self._solution["conversation_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Conversations.V1.MessagePage>"


class MessageList(ListResource):
    def __init__(self, version: Version, chat_service_sid: str, conversation_sid: str):
        """
        Initialize the MessageList

        :param version: Version that contains the resource
        :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
        :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for messages.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "chat_service_sid": chat_service_sid,
            "conversation_sid": conversation_sid,
        }
        self._uri = "/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages".format(
            **self._solution
        )

    def create(
        self,
        x_twilio_webhook_enabled: Union[
            "MessageInstance.WebhookEnabledType", object
        ] = values.unset,
        author: Union[str, object] = values.unset,
        body: Union[str, object] = values.unset,
        date_created: Union[datetime, object] = values.unset,
        date_updated: Union[datetime, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        media_sid: Union[str, object] = values.unset,
        content_sid: Union[str, object] = values.unset,
        content_variables: Union[str, object] = values.unset,
        subject: Union[str, object] = values.unset,
    ) -> MessageInstance:
        """
        Create the MessageInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param author: The channel specific identifier of the message's author. Defaults to `system`.
        :param body: The content of the message, can be up to 1,600 characters long.
        :param date_created: The date that this resource was created.
        :param date_updated: The date that this resource was last updated. `null` if the message has not been edited.
        :param attributes: A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
        :param media_sid: The Media SID to be attached to the new Message.
        :param content_sid: The unique ID of the multi-channel [Rich Content](https://www.twilio.com/docs/content-api) template, required for template-generated messages.  **Note** that if this field is set, `Body` and `MediaSid` parameters are ignored.
        :param content_variables: A structurally valid JSON string that contains values to resolve Rich Content template variables.
        :param subject: The subject of the message, can be up to 256 characters long.

        :returns: The created MessageInstance
        """
        data = values.of(
            {
                "Author": author,
                "Body": body,
                "DateCreated": serialize.iso8601_datetime(date_created),
                "DateUpdated": serialize.iso8601_datetime(date_updated),
                "Attributes": attributes,
                "MediaSid": media_sid,
                "ContentSid": content_sid,
                "ContentVariables": content_variables,
                "Subject": subject,
            }
        )
        headers = values.of(
            {
                "X-Twilio-Webhook-Enabled": x_twilio_webhook_enabled,
            }
        )
        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return MessageInstance(
            self._version,
            payload,
            chat_service_sid=self._solution["chat_service_sid"],
            conversation_sid=self._solution["conversation_sid"],
        )

    async def create_async(
        self,
        x_twilio_webhook_enabled: Union[
            "MessageInstance.WebhookEnabledType", object
        ] = values.unset,
        author: Union[str, object] = values.unset,
        body: Union[str, object] = values.unset,
        date_created: Union[datetime, object] = values.unset,
        date_updated: Union[datetime, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        media_sid: Union[str, object] = values.unset,
        content_sid: Union[str, object] = values.unset,
        content_variables: Union[str, object] = values.unset,
        subject: Union[str, object] = values.unset,
    ) -> MessageInstance:
        """
        Asynchronously create the MessageInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param author: The channel specific identifier of the message's author. Defaults to `system`.
        :param body: The content of the message, can be up to 1,600 characters long.
        :param date_created: The date that this resource was created.
        :param date_updated: The date that this resource was last updated. `null` if the message has not been edited.
        :param attributes: A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
        :param media_sid: The Media SID to be attached to the new Message.
        :param content_sid: The unique ID of the multi-channel [Rich Content](https://www.twilio.com/docs/content-api) template, required for template-generated messages.  **Note** that if this field is set, `Body` and `MediaSid` parameters are ignored.
        :param content_variables: A structurally valid JSON string that contains values to resolve Rich Content template variables.
        :param subject: The subject of the message, can be up to 256 characters long.

        :returns: The created MessageInstance
        """
        data = values.of(
            {
                "Author": author,
                "Body": body,
                "DateCreated": serialize.iso8601_datetime(date_created),
                "DateUpdated": serialize.iso8601_datetime(date_updated),
                "Attributes": attributes,
                "MediaSid": media_sid,
                "ContentSid": content_sid,
                "ContentVariables": content_variables,
                "Subject": subject,
            }
        )
        headers = values.of(
            {
                "X-Twilio-Webhook-Enabled": x_twilio_webhook_enabled,
            }
        )
        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return MessageInstance(
            self._version,
            payload,
            chat_service_sid=self._solution["chat_service_sid"],
            conversation_sid=self._solution["conversation_sid"],
        )

    def stream(
        self,
        order: Union["MessageInstance.OrderType", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[MessageInstance]:
        """
        Streams MessageInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;MessageInstance.OrderType&quot; order: The sort order of the returned messages. Can be: `asc` (ascending) or `desc` (descending), with `asc` as the default.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(order=order, page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        order: Union["MessageInstance.OrderType", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[MessageInstance]:
        """
        Asynchronously streams MessageInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;MessageInstance.OrderType&quot; order: The sort order of the returned messages. Can be: `asc` (ascending) or `desc` (descending), with `asc` as the default.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(order=order, page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        order: Union["MessageInstance.OrderType", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[MessageInstance]:
        """
        Lists MessageInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;MessageInstance.OrderType&quot; order: The sort order of the returned messages. Can be: `asc` (ascending) or `desc` (descending), with `asc` as the default.
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
                order=order,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        order: Union["MessageInstance.OrderType", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[MessageInstance]:
        """
        Asynchronously lists MessageInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;MessageInstance.OrderType&quot; order: The sort order of the returned messages. Can be: `asc` (ascending) or `desc` (descending), with `asc` as the default.
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
                order=order,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        order: Union["MessageInstance.OrderType", object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> MessagePage:
        """
        Retrieve a single page of MessageInstance records from the API.
        Request is executed immediately

        :param order: The sort order of the returned messages. Can be: `asc` (ascending) or `desc` (descending), with `asc` as the default.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of MessageInstance
        """
        data = values.of(
            {
                "Order": order,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return MessagePage(self._version, response, self._solution)

    async def page_async(
        self,
        order: Union["MessageInstance.OrderType", object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> MessagePage:
        """
        Asynchronously retrieve a single page of MessageInstance records from the API.
        Request is executed immediately

        :param order: The sort order of the returned messages. Can be: `asc` (ascending) or `desc` (descending), with `asc` as the default.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of MessageInstance
        """
        data = values.of(
            {
                "Order": order,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return MessagePage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> MessagePage:
        """
        Retrieve a specific page of MessageInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of MessageInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return MessagePage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> MessagePage:
        """
        Asynchronously retrieve a specific page of MessageInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of MessageInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return MessagePage(self._version, response, self._solution)

    def get(self, sid: str) -> MessageContext:
        """
        Constructs a MessageContext

        :param sid: A 34 character string that uniquely identifies this resource.
        """
        return MessageContext(
            self._version,
            chat_service_sid=self._solution["chat_service_sid"],
            conversation_sid=self._solution["conversation_sid"],
            sid=sid,
        )

    def __call__(self, sid: str) -> MessageContext:
        """
        Constructs a MessageContext

        :param sid: A 34 character string that uniquely identifies this resource.
        """
        return MessageContext(
            self._version,
            chat_service_sid=self._solution["chat_service_sid"],
            conversation_sid=self._solution["conversation_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Conversations.V1.MessageList>"
