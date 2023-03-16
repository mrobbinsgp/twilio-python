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


from typing import Optional
from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.preview.deployed_devices.fleet.certificate import CertificateList
from twilio.rest.preview.deployed_devices.fleet.deployment import DeploymentList
from twilio.rest.preview.deployed_devices.fleet.device import DeviceList
from twilio.rest.preview.deployed_devices.fleet.key import KeyList


class FleetList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the FleetList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.preview.deployed_devices.fleet.FleetList
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = "/Fleets".format(**self._solution)

    def create(self, friendly_name=values.unset):
        """
        Create the FleetInstance

        :param str friendly_name: Provides a human readable descriptive text for this Fleet, up to 256 characters long.

        :returns: The created FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return FleetInstance(self._version, payload)

    async def create_async(self, friendly_name=values.unset):
        """
        Asynchronously create the FleetInstance

        :param str friendly_name: Provides a human readable descriptive text for this Fleet, up to 256 characters long.

        :returns: The created FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return FleetInstance(self._version, payload)

    def stream(self, limit=None, page_size=None):
        """
        Streams FleetInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.deployed_devices.fleet.FleetInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronously streams FleetInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.deployed_devices.fleet.FleetInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, limit=None, page_size=None):
        """
        Lists FleetInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.deployed_devices.fleet.FleetInstance]
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronously lists FleetInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.deployed_devices.fleet.FleetInstance]
        """
        return list(
            await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Retrieve a single page of FleetInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetPage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return FleetPage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Asynchronously retrieve a single page of FleetInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetPage
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
        return FleetPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of FleetInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return FleetPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of FleetInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return FleetPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a FleetContext

        :param sid: Provides a 34 character string that uniquely identifies the requested Fleet resource.

        :returns: twilio.rest.preview.deployed_devices.fleet.FleetContext
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetContext
        """
        return FleetContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a FleetContext

        :param sid: Provides a 34 character string that uniquely identifies the requested Fleet resource.

        :returns: twilio.rest.preview.deployed_devices.fleet.FleetContext
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetContext
        """
        return FleetContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Preview.DeployedDevices.FleetList>"


class FleetPage(Page):
    def __init__(self, version, response, solution):
        """
        Initialize the FleetPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.deployed_devices.fleet.FleetPage
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of FleetInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.deployed_devices.fleet.FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetInstance
        """
        return FleetInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Preview.DeployedDevices.FleetPage>"


class FleetInstance(InstanceResource):
    def __init__(self, version, payload, sid: Optional[str] = None):
        """
        Initialize the FleetInstance

        :returns: twilio.rest.preview.deployed_devices.fleet.FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "url": payload.get("url"),
            "unique_name": payload.get("unique_name"),
            "friendly_name": payload.get("friendly_name"),
            "account_sid": payload.get("account_sid"),
            "default_deployment_sid": payload.get("default_deployment_sid"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "links": payload.get("links"),
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

        :returns: FleetContext for this FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetContext
        """
        if self._context is None:
            self._context = FleetContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: Contains a 34 character string that uniquely identifies this Fleet resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def url(self):
        """
        :returns: Contains an absolute URL for this Fleet resource.
        :rtype: str
        """
        return self._properties["url"]

    @property
    def unique_name(self):
        """
        :returns: Contains a unique and addressable name of this Fleet, e.g. 'default', up to 128 characters long.
        :rtype: str
        """
        return self._properties["unique_name"]

    @property
    def friendly_name(self):
        """
        :returns: Contains a human readable descriptive text for this Fleet, up to 256 characters long.
        :rtype: str
        """
        return self._properties["friendly_name"]

    @property
    def account_sid(self):
        """
        :returns: Speicifies the unique string identifier of the Account responsible for this Fleet.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def default_deployment_sid(self):
        """
        :returns: Contains the string identifier of the automatically provisioned default Deployment of this Fleet.
        :rtype: str
        """
        return self._properties["default_deployment_sid"]

    @property
    def date_created(self):
        """
        :returns: Specifies the date this Fleet was created, given in UTC ISO 8601 format.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def date_updated(self):
        """
        :returns: Specifies the date this Fleet was last updated, given in UTC ISO 8601 format.
        :rtype: datetime
        """
        return self._properties["date_updated"]

    @property
    def links(self):
        """
        :returns: Contains a dictionary of URL links to nested resources of this Fleet.
        :rtype: dict
        """
        return self._properties["links"]

    def delete(self):
        """
        Deletes the FleetInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the FleetInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()

    def fetch(self):
        """
        Fetch the FleetInstance


        :returns: The fetched FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the FleetInstance


        :returns: The fetched FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetInstance
        """
        return await self._proxy.fetch_async()

    def update(self, friendly_name=values.unset, default_deployment_sid=values.unset):
        """
        Update the FleetInstance

        :param str friendly_name: Provides a human readable descriptive text for this Fleet, up to 256 characters long.
        :param str default_deployment_sid: Provides a string identifier of a Deployment that is going to be used as a default one for this Fleet.

        :returns: The updated FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            default_deployment_sid=default_deployment_sid,
        )

    async def update_async(
        self, friendly_name=values.unset, default_deployment_sid=values.unset
    ):
        """
        Asynchronous coroutine to update the FleetInstance

        :param str friendly_name: Provides a human readable descriptive text for this Fleet, up to 256 characters long.
        :param str default_deployment_sid: Provides a string identifier of a Deployment that is going to be used as a default one for this Fleet.

        :returns: The updated FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
            default_deployment_sid=default_deployment_sid,
        )

    @property
    def certificates(self):
        """
        Access the certificates

        :returns: twilio.rest.preview.deployed_devices.fleet.CertificateList
        :rtype: twilio.rest.preview.deployed_devices.fleet.CertificateList
        """
        return self._proxy.certificates

    @property
    def deployments(self):
        """
        Access the deployments

        :returns: twilio.rest.preview.deployed_devices.fleet.DeploymentList
        :rtype: twilio.rest.preview.deployed_devices.fleet.DeploymentList
        """
        return self._proxy.deployments

    @property
    def devices(self):
        """
        Access the devices

        :returns: twilio.rest.preview.deployed_devices.fleet.DeviceList
        :rtype: twilio.rest.preview.deployed_devices.fleet.DeviceList
        """
        return self._proxy.devices

    @property
    def keys(self):
        """
        Access the keys

        :returns: twilio.rest.preview.deployed_devices.fleet.KeyList
        :rtype: twilio.rest.preview.deployed_devices.fleet.KeyList
        """
        return self._proxy.keys

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.DeployedDevices.FleetInstance {}>".format(context)


class FleetContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the FleetContext

        :param Version version: Version that contains the resource
        :param sid: Provides a 34 character string that uniquely identifies the requested Fleet resource.

        :returns: twilio.rest.preview.deployed_devices.fleet.FleetContext
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Fleets/{sid}".format(**self._solution)

        self._certificates = None
        self._deployments = None
        self._devices = None
        self._keys = None

    def delete(self):
        """
        Deletes the FleetInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the FleetInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self):
        """
        Fetch the FleetInstance


        :returns: The fetched FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return FleetInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the FleetInstance


        :returns: The fetched FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return FleetInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(self, friendly_name=values.unset, default_deployment_sid=values.unset):
        """
        Update the FleetInstance

        :param str friendly_name: Provides a human readable descriptive text for this Fleet, up to 256 characters long.
        :param str default_deployment_sid: Provides a string identifier of a Deployment that is going to be used as a default one for this Fleet.

        :returns: The updated FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "DefaultDeploymentSid": default_deployment_sid,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return FleetInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self, friendly_name=values.unset, default_deployment_sid=values.unset
    ):
        """
        Asynchronous coroutine to update the FleetInstance

        :param str friendly_name: Provides a human readable descriptive text for this Fleet, up to 256 characters long.
        :param str default_deployment_sid: Provides a string identifier of a Deployment that is going to be used as a default one for this Fleet.

        :returns: The updated FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "DefaultDeploymentSid": default_deployment_sid,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return FleetInstance(self._version, payload, sid=self._solution["sid"])

    @property
    def certificates(self):
        """
        Access the certificates

        :returns: twilio.rest.preview.deployed_devices.fleet.CertificateList
        :rtype: twilio.rest.preview.deployed_devices.fleet.CertificateList
        """
        if self._certificates is None:
            self._certificates = CertificateList(
                self._version,
                self._solution["sid"],
            )
        return self._certificates

    @property
    def deployments(self):
        """
        Access the deployments

        :returns: twilio.rest.preview.deployed_devices.fleet.DeploymentList
        :rtype: twilio.rest.preview.deployed_devices.fleet.DeploymentList
        """
        if self._deployments is None:
            self._deployments = DeploymentList(
                self._version,
                self._solution["sid"],
            )
        return self._deployments

    @property
    def devices(self):
        """
        Access the devices

        :returns: twilio.rest.preview.deployed_devices.fleet.DeviceList
        :rtype: twilio.rest.preview.deployed_devices.fleet.DeviceList
        """
        if self._devices is None:
            self._devices = DeviceList(
                self._version,
                self._solution["sid"],
            )
        return self._devices

    @property
    def keys(self):
        """
        Access the keys

        :returns: twilio.rest.preview.deployed_devices.fleet.KeyList
        :rtype: twilio.rest.preview.deployed_devices.fleet.KeyList
        """
        if self._keys is None:
            self._keys = KeyList(
                self._version,
                self._solution["sid"],
            )
        return self._keys

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.DeployedDevices.FleetContext {}>".format(context)
