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
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class NetworkList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the NetworkList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.supersim.v1.network.NetworkList
        :rtype: twilio.rest.supersim.v1.network.NetworkList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = "/Networks".format(**self._solution)

    def stream(
        self,
        iso_country=values.unset,
        mcc=values.unset,
        mnc=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Streams NetworkInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str iso_country: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Network resources to read.
        :param str mcc: The 'mobile country code' of a country. Network resources with this `mcc` in their `identifiers` will be read.
        :param str mnc: The 'mobile network code' of a mobile operator network. Network resources with this `mnc` in their `identifiers` will be read.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.network.NetworkInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            iso_country=iso_country, mcc=mcc, mnc=mnc, page_size=limits["page_size"]
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        iso_country=values.unset,
        mcc=values.unset,
        mnc=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Asynchronously streams NetworkInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str iso_country: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Network resources to read.
        :param str mcc: The 'mobile country code' of a country. Network resources with this `mcc` in their `identifiers` will be read.
        :param str mnc: The 'mobile network code' of a mobile operator network. Network resources with this `mnc` in their `identifiers` will be read.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.network.NetworkInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            iso_country=iso_country, mcc=mcc, mnc=mnc, page_size=limits["page_size"]
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        iso_country=values.unset,
        mcc=values.unset,
        mnc=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Lists NetworkInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str iso_country: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Network resources to read.
        :param str mcc: The 'mobile country code' of a country. Network resources with this `mcc` in their `identifiers` will be read.
        :param str mnc: The 'mobile network code' of a mobile operator network. Network resources with this `mnc` in their `identifiers` will be read.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.network.NetworkInstance]
        """
        return list(
            self.stream(
                iso_country=iso_country,
                mcc=mcc,
                mnc=mnc,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        iso_country=values.unset,
        mcc=values.unset,
        mnc=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Asynchronously lists NetworkInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str iso_country: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Network resources to read.
        :param str mcc: The 'mobile country code' of a country. Network resources with this `mcc` in their `identifiers` will be read.
        :param str mnc: The 'mobile network code' of a mobile operator network. Network resources with this `mnc` in their `identifiers` will be read.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.network.NetworkInstance]
        """
        return list(
            await self.stream_async(
                iso_country=iso_country,
                mcc=mcc,
                mnc=mnc,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        iso_country=values.unset,
        mcc=values.unset,
        mnc=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Retrieve a single page of NetworkInstance records from the API.
        Request is executed immediately

        :param str iso_country: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Network resources to read.
        :param str mcc: The 'mobile country code' of a country. Network resources with this `mcc` in their `identifiers` will be read.
        :param str mnc: The 'mobile network code' of a mobile operator network. Network resources with this `mnc` in their `identifiers` will be read.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of NetworkInstance
        :rtype: twilio.rest.supersim.v1.network.NetworkPage
        """
        data = values.of(
            {
                "IsoCountry": iso_country,
                "Mcc": mcc,
                "Mnc": mnc,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return NetworkPage(self._version, response, self._solution)

    async def page_async(
        self,
        iso_country=values.unset,
        mcc=values.unset,
        mnc=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Asynchronously retrieve a single page of NetworkInstance records from the API.
        Request is executed immediately

        :param str iso_country: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Network resources to read.
        :param str mcc: The 'mobile country code' of a country. Network resources with this `mcc` in their `identifiers` will be read.
        :param str mnc: The 'mobile network code' of a mobile operator network. Network resources with this `mnc` in their `identifiers` will be read.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of NetworkInstance
        :rtype: twilio.rest.supersim.v1.network.NetworkPage
        """
        data = values.of(
            {
                "IsoCountry": iso_country,
                "Mcc": mcc,
                "Mnc": mnc,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return NetworkPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of NetworkInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of NetworkInstance
        :rtype: twilio.rest.supersim.v1.network.NetworkPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return NetworkPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of NetworkInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of NetworkInstance
        :rtype: twilio.rest.supersim.v1.network.NetworkPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return NetworkPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a NetworkContext

        :param sid: The SID of the Network resource to fetch.

        :returns: twilio.rest.supersim.v1.network.NetworkContext
        :rtype: twilio.rest.supersim.v1.network.NetworkContext
        """
        return NetworkContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a NetworkContext

        :param sid: The SID of the Network resource to fetch.

        :returns: twilio.rest.supersim.v1.network.NetworkContext
        :rtype: twilio.rest.supersim.v1.network.NetworkContext
        """
        return NetworkContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Supersim.V1.NetworkList>"


class NetworkPage(Page):
    def __init__(self, version, response, solution):
        """
        Initialize the NetworkPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.supersim.v1.network.NetworkPage
        :rtype: twilio.rest.supersim.v1.network.NetworkPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of NetworkInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.supersim.v1.network.NetworkInstance
        :rtype: twilio.rest.supersim.v1.network.NetworkInstance
        """
        return NetworkInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Supersim.V1.NetworkPage>"


class NetworkInstance(InstanceResource):
    def __init__(self, version, payload, sid: Optional[str] = None):
        """
        Initialize the NetworkInstance

        :returns: twilio.rest.supersim.v1.network.NetworkInstance
        :rtype: twilio.rest.supersim.v1.network.NetworkInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "friendly_name": payload.get("friendly_name"),
            "url": payload.get("url"),
            "iso_country": payload.get("iso_country"),
            "identifiers": payload.get("identifiers"),
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

        :returns: NetworkContext for this NetworkInstance
        :rtype: twilio.rest.supersim.v1.network.NetworkContext
        """
        if self._context is None:
            self._context = NetworkContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Network resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def friendly_name(self):
        """
        :returns: A human readable identifier of this resource.
        :rtype: str
        """
        return self._properties["friendly_name"]

    @property
    def url(self):
        """
        :returns: The absolute URL of the Network resource.
        :rtype: str
        """
        return self._properties["url"]

    @property
    def iso_country(self):
        """
        :returns: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Network resource.
        :rtype: str
        """
        return self._properties["iso_country"]

    @property
    def identifiers(self):
        """
        :returns: Array of objects identifying the [MCC-MNCs](https://en.wikipedia.org/wiki/Mobile_country_code) that are included in the Network resource.
        :rtype: list[object]
        """
        return self._properties["identifiers"]

    def fetch(self):
        """
        Fetch the NetworkInstance


        :returns: The fetched NetworkInstance
        :rtype: twilio.rest.supersim.v1.network.NetworkInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the NetworkInstance


        :returns: The fetched NetworkInstance
        :rtype: twilio.rest.supersim.v1.network.NetworkInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Supersim.V1.NetworkInstance {}>".format(context)


class NetworkContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the NetworkContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the Network resource to fetch.

        :returns: twilio.rest.supersim.v1.network.NetworkContext
        :rtype: twilio.rest.supersim.v1.network.NetworkContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Networks/{sid}".format(**self._solution)

    def fetch(self):
        """
        Fetch the NetworkInstance


        :returns: The fetched NetworkInstance
        :rtype: twilio.rest.supersim.v1.network.NetworkInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return NetworkInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the NetworkInstance


        :returns: The fetched NetworkInstance
        :rtype: twilio.rest.supersim.v1.network.NetworkInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return NetworkInstance(
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
        return "<Twilio.Supersim.V1.NetworkContext {}>".format(context)
