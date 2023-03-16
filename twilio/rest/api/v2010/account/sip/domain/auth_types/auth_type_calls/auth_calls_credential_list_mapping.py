r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
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


class AuthCallsCredentialListMappingList(ListResource):
    def __init__(self, version: Version, account_sid: str, domain_sid: str):
        """
        Initialize the AuthCallsCredentialListMappingList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resources to read.
        :param domain_sid: The SID of the SIP domain that contains the resources to read.

        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingList
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "domain_sid": domain_sid,
        }
        self._uri = "/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Calls/CredentialListMappings.json".format(
            **self._solution
        )

    def create(self, credential_list_sid):
        """
        Create the AuthCallsCredentialListMappingInstance

        :param str credential_list_sid: The SID of the CredentialList resource to map to the SIP domain.

        :returns: The created AuthCallsCredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingInstance
        """
        data = values.of(
            {
                "CredentialListSid": credential_list_sid,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AuthCallsCredentialListMappingInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            domain_sid=self._solution["domain_sid"],
        )

    async def create_async(self, credential_list_sid):
        """
        Asynchronously create the AuthCallsCredentialListMappingInstance

        :param str credential_list_sid: The SID of the CredentialList resource to map to the SIP domain.

        :returns: The created AuthCallsCredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingInstance
        """
        data = values.of(
            {
                "CredentialListSid": credential_list_sid,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AuthCallsCredentialListMappingInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            domain_sid=self._solution["domain_sid"],
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams AuthCallsCredentialListMappingInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronously streams AuthCallsCredentialListMappingInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, limit=None, page_size=None):
        """
        Lists AuthCallsCredentialListMappingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingInstance]
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronously lists AuthCallsCredentialListMappingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingInstance]
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
        Retrieve a single page of AuthCallsCredentialListMappingInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AuthCallsCredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingPage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return AuthCallsCredentialListMappingPage(
            self._version, response, self._solution
        )

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Asynchronously retrieve a single page of AuthCallsCredentialListMappingInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AuthCallsCredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingPage
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
        return AuthCallsCredentialListMappingPage(
            self._version, response, self._solution
        )

    def get_page(self, target_url):
        """
        Retrieve a specific page of AuthCallsCredentialListMappingInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AuthCallsCredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return AuthCallsCredentialListMappingPage(
            self._version, response, self._solution
        )

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of AuthCallsCredentialListMappingInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AuthCallsCredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return AuthCallsCredentialListMappingPage(
            self._version, response, self._solution
        )

    def get(self, sid):
        """
        Constructs a AuthCallsCredentialListMappingContext

        :param sid: The Twilio-provided string that uniquely identifies the CredentialListMapping resource to fetch.

        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingContext
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingContext
        """
        return AuthCallsCredentialListMappingContext(
            self._version,
            account_sid=self._solution["account_sid"],
            domain_sid=self._solution["domain_sid"],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a AuthCallsCredentialListMappingContext

        :param sid: The Twilio-provided string that uniquely identifies the CredentialListMapping resource to fetch.

        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingContext
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingContext
        """
        return AuthCallsCredentialListMappingContext(
            self._version,
            account_sid=self._solution["account_sid"],
            domain_sid=self._solution["domain_sid"],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Api.V2010.AuthCallsCredentialListMappingList>"


class AuthCallsCredentialListMappingPage(Page):
    def __init__(self, version, response, solution):
        """
        Initialize the AuthCallsCredentialListMappingPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingPage
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AuthCallsCredentialListMappingInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingInstance
        """
        return AuthCallsCredentialListMappingInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            domain_sid=self._solution["domain_sid"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Api.V2010.AuthCallsCredentialListMappingPage>"


class AuthCallsCredentialListMappingInstance(InstanceResource):
    def __init__(
        self,
        version,
        payload,
        account_sid: str,
        domain_sid: str,
        sid: Optional[str] = None,
    ):
        """
        Initialize the AuthCallsCredentialListMappingInstance

        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "date_created": deserialize.rfc2822_datetime(payload.get("date_created")),
            "date_updated": deserialize.rfc2822_datetime(payload.get("date_updated")),
            "friendly_name": payload.get("friendly_name"),
            "sid": payload.get("sid"),
        }

        self._context = None
        self._solution = {
            "account_sid": account_sid,
            "domain_sid": domain_sid,
            "sid": sid or self._properties["sid"],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AuthCallsCredentialListMappingContext for this AuthCallsCredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingContext
        """
        if self._context is None:
            self._context = AuthCallsCredentialListMappingContext(
                self._version,
                account_sid=self._solution["account_sid"],
                domain_sid=self._solution["domain_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def date_created(self):
        """
        :returns: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties["date_updated"]

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource.
        :rtype: str
        """
        return self._properties["friendly_name"]

    @property
    def sid(self):
        """
        :returns: The unique string that that we created to identify the CredentialListMapping resource.
        :rtype: str
        """
        return self._properties["sid"]

    def delete(self):
        """
        Deletes the AuthCallsCredentialListMappingInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the AuthCallsCredentialListMappingInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()

    def fetch(self):
        """
        Fetch the AuthCallsCredentialListMappingInstance


        :returns: The fetched AuthCallsCredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the AuthCallsCredentialListMappingInstance


        :returns: The fetched AuthCallsCredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.AuthCallsCredentialListMappingInstance {}>".format(
            context
        )


class AuthCallsCredentialListMappingContext(InstanceContext):
    def __init__(self, version: Version, account_sid: str, domain_sid: str, sid: str):
        """
        Initialize the AuthCallsCredentialListMappingContext

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resource to fetch.
        :param domain_sid: The SID of the SIP domain that contains the resource to fetch.
        :param sid: The Twilio-provided string that uniquely identifies the CredentialListMapping resource to fetch.

        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingContext
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "domain_sid": domain_sid,
            "sid": sid,
        }
        self._uri = "/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Calls/CredentialListMappings/{sid}.json".format(
            **self._solution
        )

    def delete(self):
        """
        Deletes the AuthCallsCredentialListMappingInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the AuthCallsCredentialListMappingInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self):
        """
        Fetch the AuthCallsCredentialListMappingInstance


        :returns: The fetched AuthCallsCredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return AuthCallsCredentialListMappingInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            domain_sid=self._solution["domain_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the AuthCallsCredentialListMappingInstance


        :returns: The fetched AuthCallsCredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_type_calls.auth_calls_credential_list_mapping.AuthCallsCredentialListMappingInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return AuthCallsCredentialListMappingInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            domain_sid=self._solution["domain_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.AuthCallsCredentialListMappingContext {}>".format(
            context
        )
