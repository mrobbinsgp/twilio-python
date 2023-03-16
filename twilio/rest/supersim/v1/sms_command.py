r"""
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


from typing import Optional
from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class SmsCommandList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the SmsCommandList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.supersim.v1.sms_command.SmsCommandList
        :rtype: twilio.rest.supersim.v1.sms_command.SmsCommandList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = "/SmsCommands".format(**self._solution)

    def create(
        self, sim, payload, callback_method=values.unset, callback_url=values.unset
    ):
        """
        Create the SmsCommandInstance

        :param str sim: The `sid` or `unique_name` of the [SIM](https://www.twilio.com/docs/iot/supersim/api/sim-resource) to send the SMS Command to.
        :param str payload: The message body of the SMS Command.
        :param str callback_method: The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is POST.
        :param str callback_url: The URL we should call using the `callback_method` after we have sent the command.

        :returns: The created SmsCommandInstance
        :rtype: twilio.rest.supersim.v1.sms_command.SmsCommandInstance
        """
        data = values.of(
            {
                "Sim": sim,
                "Payload": payload,
                "CallbackMethod": callback_method,
                "CallbackUrl": callback_url,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SmsCommandInstance(self._version, payload)

    async def create_async(
        self, sim, payload, callback_method=values.unset, callback_url=values.unset
    ):
        """
        Asynchronously create the SmsCommandInstance

        :param str sim: The `sid` or `unique_name` of the [SIM](https://www.twilio.com/docs/iot/supersim/api/sim-resource) to send the SMS Command to.
        :param str payload: The message body of the SMS Command.
        :param str callback_method: The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is POST.
        :param str callback_url: The URL we should call using the `callback_method` after we have sent the command.

        :returns: The created SmsCommandInstance
        :rtype: twilio.rest.supersim.v1.sms_command.SmsCommandInstance
        """
        data = values.of(
            {
                "Sim": sim,
                "Payload": payload,
                "CallbackMethod": callback_method,
                "CallbackUrl": callback_url,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SmsCommandInstance(self._version, payload)

    def stream(
        self,
        sim=values.unset,
        status=values.unset,
        direction=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Streams SmsCommandInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str sim: The SID or unique name of the Sim resource that SMS Command was sent to or from.
        :param SmsCommandInstance.Status status: The status of the SMS Command. Can be: `queued`, `sent`, `delivered`, `received` or `failed`. See the [SMS Command Status Values](https://www.twilio.com/docs/iot/supersim/api/smscommand-resource#status-values) for a description of each.
        :param SmsCommandInstance.Direction direction: The direction of the SMS Command. Can be `to_sim` or `from_sim`. The value of `to_sim` is synonymous with the term `mobile terminated`, and `from_sim` is synonymous with the term `mobile originated`.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.sms_command.SmsCommandInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            sim=sim, status=status, direction=direction, page_size=limits["page_size"]
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        sim=values.unset,
        status=values.unset,
        direction=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Asynchronously streams SmsCommandInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str sim: The SID or unique name of the Sim resource that SMS Command was sent to or from.
        :param SmsCommandInstance.Status status: The status of the SMS Command. Can be: `queued`, `sent`, `delivered`, `received` or `failed`. See the [SMS Command Status Values](https://www.twilio.com/docs/iot/supersim/api/smscommand-resource#status-values) for a description of each.
        :param SmsCommandInstance.Direction direction: The direction of the SMS Command. Can be `to_sim` or `from_sim`. The value of `to_sim` is synonymous with the term `mobile terminated`, and `from_sim` is synonymous with the term `mobile originated`.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.sms_command.SmsCommandInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            sim=sim, status=status, direction=direction, page_size=limits["page_size"]
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        sim=values.unset,
        status=values.unset,
        direction=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Lists SmsCommandInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str sim: The SID or unique name of the Sim resource that SMS Command was sent to or from.
        :param SmsCommandInstance.Status status: The status of the SMS Command. Can be: `queued`, `sent`, `delivered`, `received` or `failed`. See the [SMS Command Status Values](https://www.twilio.com/docs/iot/supersim/api/smscommand-resource#status-values) for a description of each.
        :param SmsCommandInstance.Direction direction: The direction of the SMS Command. Can be `to_sim` or `from_sim`. The value of `to_sim` is synonymous with the term `mobile terminated`, and `from_sim` is synonymous with the term `mobile originated`.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.sms_command.SmsCommandInstance]
        """
        return list(
            self.stream(
                sim=sim,
                status=status,
                direction=direction,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        sim=values.unset,
        status=values.unset,
        direction=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Asynchronously lists SmsCommandInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str sim: The SID or unique name of the Sim resource that SMS Command was sent to or from.
        :param SmsCommandInstance.Status status: The status of the SMS Command. Can be: `queued`, `sent`, `delivered`, `received` or `failed`. See the [SMS Command Status Values](https://www.twilio.com/docs/iot/supersim/api/smscommand-resource#status-values) for a description of each.
        :param SmsCommandInstance.Direction direction: The direction of the SMS Command. Can be `to_sim` or `from_sim`. The value of `to_sim` is synonymous with the term `mobile terminated`, and `from_sim` is synonymous with the term `mobile originated`.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.sms_command.SmsCommandInstance]
        """
        return list(
            await self.stream_async(
                sim=sim,
                status=status,
                direction=direction,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        sim=values.unset,
        status=values.unset,
        direction=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Retrieve a single page of SmsCommandInstance records from the API.
        Request is executed immediately

        :param str sim: The SID or unique name of the Sim resource that SMS Command was sent to or from.
        :param SmsCommandInstance.Status status: The status of the SMS Command. Can be: `queued`, `sent`, `delivered`, `received` or `failed`. See the [SMS Command Status Values](https://www.twilio.com/docs/iot/supersim/api/smscommand-resource#status-values) for a description of each.
        :param SmsCommandInstance.Direction direction: The direction of the SMS Command. Can be `to_sim` or `from_sim`. The value of `to_sim` is synonymous with the term `mobile terminated`, and `from_sim` is synonymous with the term `mobile originated`.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SmsCommandInstance
        :rtype: twilio.rest.supersim.v1.sms_command.SmsCommandPage
        """
        data = values.of(
            {
                "Sim": sim,
                "Status": status,
                "Direction": direction,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return SmsCommandPage(self._version, response, self._solution)

    async def page_async(
        self,
        sim=values.unset,
        status=values.unset,
        direction=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Asynchronously retrieve a single page of SmsCommandInstance records from the API.
        Request is executed immediately

        :param str sim: The SID or unique name of the Sim resource that SMS Command was sent to or from.
        :param SmsCommandInstance.Status status: The status of the SMS Command. Can be: `queued`, `sent`, `delivered`, `received` or `failed`. See the [SMS Command Status Values](https://www.twilio.com/docs/iot/supersim/api/smscommand-resource#status-values) for a description of each.
        :param SmsCommandInstance.Direction direction: The direction of the SMS Command. Can be `to_sim` or `from_sim`. The value of `to_sim` is synonymous with the term `mobile terminated`, and `from_sim` is synonymous with the term `mobile originated`.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SmsCommandInstance
        :rtype: twilio.rest.supersim.v1.sms_command.SmsCommandPage
        """
        data = values.of(
            {
                "Sim": sim,
                "Status": status,
                "Direction": direction,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return SmsCommandPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SmsCommandInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SmsCommandInstance
        :rtype: twilio.rest.supersim.v1.sms_command.SmsCommandPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return SmsCommandPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of SmsCommandInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SmsCommandInstance
        :rtype: twilio.rest.supersim.v1.sms_command.SmsCommandPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return SmsCommandPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a SmsCommandContext

        :param sid: The SID of the SMS Command resource to fetch.

        :returns: twilio.rest.supersim.v1.sms_command.SmsCommandContext
        :rtype: twilio.rest.supersim.v1.sms_command.SmsCommandContext
        """
        return SmsCommandContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a SmsCommandContext

        :param sid: The SID of the SMS Command resource to fetch.

        :returns: twilio.rest.supersim.v1.sms_command.SmsCommandContext
        :rtype: twilio.rest.supersim.v1.sms_command.SmsCommandContext
        """
        return SmsCommandContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Supersim.V1.SmsCommandList>"


class SmsCommandPage(Page):
    def __init__(self, version, response, solution):
        """
        Initialize the SmsCommandPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.supersim.v1.sms_command.SmsCommandPage
        :rtype: twilio.rest.supersim.v1.sms_command.SmsCommandPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SmsCommandInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.supersim.v1.sms_command.SmsCommandInstance
        :rtype: twilio.rest.supersim.v1.sms_command.SmsCommandInstance
        """
        return SmsCommandInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Supersim.V1.SmsCommandPage>"


class SmsCommandInstance(InstanceResource):
    class Direction(object):
        TO_SIM = "to_sim"
        FROM_SIM = "from_sim"

    class Status(object):
        QUEUED = "queued"
        SENT = "sent"
        DELIVERED = "delivered"
        RECEIVED = "received"
        FAILED = "failed"

    def __init__(self, version, payload, sid: Optional[str] = None):
        """
        Initialize the SmsCommandInstance

        :returns: twilio.rest.supersim.v1.sms_command.SmsCommandInstance
        :rtype: twilio.rest.supersim.v1.sms_command.SmsCommandInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "account_sid": payload.get("account_sid"),
            "sim_sid": payload.get("sim_sid"),
            "payload": payload.get("payload"),
            "status": payload.get("status"),
            "direction": payload.get("direction"),
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

        :returns: SmsCommandContext for this SmsCommandInstance
        :rtype: twilio.rest.supersim.v1.sms_command.SmsCommandContext
        """
        if self._context is None:
            self._context = SmsCommandContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the SMS Command resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SMS Command resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def sim_sid(self):
        """
        :returns: The SID of the [SIM](https://www.twilio.com/docs/iot/supersim/api/sim-resource) that this SMS Command was sent to or from.
        :rtype: str
        """
        return self._properties["sim_sid"]

    @property
    def payload(self):
        """
        :returns: The message body of the SMS Command sent to or from the SIM. For text mode messages, this can be up to 160 characters.
        :rtype: str
        """
        return self._properties["payload"]

    @property
    def status(self):
        """
        :returns:
        :rtype: SmsCommandInstance.Status
        """
        return self._properties["status"]

    @property
    def direction(self):
        """
        :returns:
        :rtype: SmsCommandInstance.Direction
        """
        return self._properties["direction"]

    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_updated"]

    @property
    def url(self):
        """
        :returns: The absolute URL of the SMS Command resource.
        :rtype: str
        """
        return self._properties["url"]

    def fetch(self):
        """
        Fetch the SmsCommandInstance


        :returns: The fetched SmsCommandInstance
        :rtype: twilio.rest.supersim.v1.sms_command.SmsCommandInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the SmsCommandInstance


        :returns: The fetched SmsCommandInstance
        :rtype: twilio.rest.supersim.v1.sms_command.SmsCommandInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Supersim.V1.SmsCommandInstance {}>".format(context)


class SmsCommandContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the SmsCommandContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the SMS Command resource to fetch.

        :returns: twilio.rest.supersim.v1.sms_command.SmsCommandContext
        :rtype: twilio.rest.supersim.v1.sms_command.SmsCommandContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/SmsCommands/{sid}".format(**self._solution)

    def fetch(self):
        """
        Fetch the SmsCommandInstance


        :returns: The fetched SmsCommandInstance
        :rtype: twilio.rest.supersim.v1.sms_command.SmsCommandInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return SmsCommandInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the SmsCommandInstance


        :returns: The fetched SmsCommandInstance
        :rtype: twilio.rest.supersim.v1.sms_command.SmsCommandInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return SmsCommandInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Supersim.V1.SmsCommandContext {}>".format(context)
