r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Preview
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class InstalledAddOnExtensionInstance(InstanceResource):
    """
    :ivar sid: The unique string that we created to identify the InstalledAddOn Extension resource.
    :ivar installed_add_on_sid: The SID of the InstalledAddOn resource to which this extension applies.
    :ivar friendly_name: The string that you assigned to describe the resource.
    :ivar product_name: The name of the Product this Extension is used within.
    :ivar unique_name: An application-defined string that uniquely identifies the resource.
    :ivar enabled: Whether the Extension will be invoked.
    :ivar url: The absolute URL of the resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        installed_add_on_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.installed_add_on_sid: Optional[str] = payload.get("installed_add_on_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.product_name: Optional[str] = payload.get("product_name")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.enabled: Optional[bool] = payload.get("enabled")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "installed_add_on_sid": installed_add_on_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[InstalledAddOnExtensionContext] = None

    @property
    def _proxy(self) -> "InstalledAddOnExtensionContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: InstalledAddOnExtensionContext for this InstalledAddOnExtensionInstance
        """
        if self._context is None:
            self._context = InstalledAddOnExtensionContext(
                self._version,
                installed_add_on_sid=self._solution["installed_add_on_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "InstalledAddOnExtensionInstance":
        """
        Fetch the InstalledAddOnExtensionInstance


        :returns: The fetched InstalledAddOnExtensionInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "InstalledAddOnExtensionInstance":
        """
        Asynchronous coroutine to fetch the InstalledAddOnExtensionInstance


        :returns: The fetched InstalledAddOnExtensionInstance
        """
        return await self._proxy.fetch_async()

    def update(self, enabled: bool) -> "InstalledAddOnExtensionInstance":
        """
        Update the InstalledAddOnExtensionInstance

        :param enabled: Whether the Extension should be invoked.

        :returns: The updated InstalledAddOnExtensionInstance
        """
        return self._proxy.update(
            enabled=enabled,
        )

    async def update_async(self, enabled: bool) -> "InstalledAddOnExtensionInstance":
        """
        Asynchronous coroutine to update the InstalledAddOnExtensionInstance

        :param enabled: Whether the Extension should be invoked.

        :returns: The updated InstalledAddOnExtensionInstance
        """
        return await self._proxy.update_async(
            enabled=enabled,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Marketplace.InstalledAddOnExtensionInstance {}>".format(
            context
        )


class InstalledAddOnExtensionContext(InstanceContext):
    def __init__(self, version: Version, installed_add_on_sid: str, sid: str):
        """
        Initialize the InstalledAddOnExtensionContext

        :param version: Version that contains the resource
        :param installed_add_on_sid: The SID of the InstalledAddOn resource with the extension to update.
        :param sid: The SID of the InstalledAddOn Extension resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "installed_add_on_sid": installed_add_on_sid,
            "sid": sid,
        }
        self._uri = "/InstalledAddOns/{installed_add_on_sid}/Extensions/{sid}".format(
            **self._solution
        )

    def fetch(self) -> InstalledAddOnExtensionInstance:
        """
        Fetch the InstalledAddOnExtensionInstance


        :returns: The fetched InstalledAddOnExtensionInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return InstalledAddOnExtensionInstance(
            self._version,
            payload,
            installed_add_on_sid=self._solution["installed_add_on_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> InstalledAddOnExtensionInstance:
        """
        Asynchronous coroutine to fetch the InstalledAddOnExtensionInstance


        :returns: The fetched InstalledAddOnExtensionInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return InstalledAddOnExtensionInstance(
            self._version,
            payload,
            installed_add_on_sid=self._solution["installed_add_on_sid"],
            sid=self._solution["sid"],
        )

    def update(self, enabled: bool) -> InstalledAddOnExtensionInstance:
        """
        Update the InstalledAddOnExtensionInstance

        :param enabled: Whether the Extension should be invoked.

        :returns: The updated InstalledAddOnExtensionInstance
        """
        data = values.of(
            {
                "Enabled": enabled,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return InstalledAddOnExtensionInstance(
            self._version,
            payload,
            installed_add_on_sid=self._solution["installed_add_on_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(self, enabled: bool) -> InstalledAddOnExtensionInstance:
        """
        Asynchronous coroutine to update the InstalledAddOnExtensionInstance

        :param enabled: Whether the Extension should be invoked.

        :returns: The updated InstalledAddOnExtensionInstance
        """
        data = values.of(
            {
                "Enabled": enabled,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return InstalledAddOnExtensionInstance(
            self._version,
            payload,
            installed_add_on_sid=self._solution["installed_add_on_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Marketplace.InstalledAddOnExtensionContext {}>".format(
            context
        )


class InstalledAddOnExtensionPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> InstalledAddOnExtensionInstance:
        """
        Build an instance of InstalledAddOnExtensionInstance

        :param payload: Payload response from the API
        """
        return InstalledAddOnExtensionInstance(
            self._version,
            payload,
            installed_add_on_sid=self._solution["installed_add_on_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Marketplace.InstalledAddOnExtensionPage>"


class InstalledAddOnExtensionList(ListResource):
    def __init__(self, version: Version, installed_add_on_sid: str):
        """
        Initialize the InstalledAddOnExtensionList

        :param version: Version that contains the resource
        :param installed_add_on_sid: The SID of the InstalledAddOn resource with the extensions to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "installed_add_on_sid": installed_add_on_sid,
        }
        self._uri = "/InstalledAddOns/{installed_add_on_sid}/Extensions".format(
            **self._solution
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[InstalledAddOnExtensionInstance]:
        """
        Streams InstalledAddOnExtensionInstance records from the API as a generator stream.
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
    ) -> AsyncIterator[InstalledAddOnExtensionInstance]:
        """
        Asynchronously streams InstalledAddOnExtensionInstance records from the API as a generator stream.
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
    ) -> List[InstalledAddOnExtensionInstance]:
        """
        Lists InstalledAddOnExtensionInstance records from the API as a list.
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
    ) -> List[InstalledAddOnExtensionInstance]:
        """
        Asynchronously lists InstalledAddOnExtensionInstance records from the API as a list.
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
    ) -> InstalledAddOnExtensionPage:
        """
        Retrieve a single page of InstalledAddOnExtensionInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of InstalledAddOnExtensionInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return InstalledAddOnExtensionPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> InstalledAddOnExtensionPage:
        """
        Asynchronously retrieve a single page of InstalledAddOnExtensionInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of InstalledAddOnExtensionInstance
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
        return InstalledAddOnExtensionPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> InstalledAddOnExtensionPage:
        """
        Retrieve a specific page of InstalledAddOnExtensionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of InstalledAddOnExtensionInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return InstalledAddOnExtensionPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> InstalledAddOnExtensionPage:
        """
        Asynchronously retrieve a specific page of InstalledAddOnExtensionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of InstalledAddOnExtensionInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return InstalledAddOnExtensionPage(self._version, response, self._solution)

    def get(self, sid: str) -> InstalledAddOnExtensionContext:
        """
        Constructs a InstalledAddOnExtensionContext

        :param sid: The SID of the InstalledAddOn Extension resource to update.
        """
        return InstalledAddOnExtensionContext(
            self._version,
            installed_add_on_sid=self._solution["installed_add_on_sid"],
            sid=sid,
        )

    def __call__(self, sid: str) -> InstalledAddOnExtensionContext:
        """
        Constructs a InstalledAddOnExtensionContext

        :param sid: The SID of the InstalledAddOn Extension resource to update.
        """
        return InstalledAddOnExtensionContext(
            self._version,
            installed_add_on_sid=self._solution["installed_add_on_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Marketplace.InstalledAddOnExtensionList>"
