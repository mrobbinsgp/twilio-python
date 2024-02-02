r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Routes
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, Optional, Union
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class TrunkInstance(InstanceResource):
    """
    :ivar sip_trunk_domain: The absolute URL of the SIP Trunk
    :ivar url: The absolute URL of the resource.
    :ivar sid: A 34 character string that uniquely identifies the Inbound Processing Region assignments for this SIP Trunk.
    :ivar account_sid: The unique SID identifier of the Account.
    :ivar friendly_name: A human readable description of the Inbound Processing Region assignments for this SIP Trunk, up to 64 characters.
    :ivar voice_region: The Inbound Processing Region used for this SIP Trunk for voice.
    :ivar date_created: The date that this SIP Trunk was assigned an Inbound Processing Region, given in ISO 8601 format.
    :ivar date_updated: The date that the Inbound Processing Region was updated for this SIP Trunk, given in ISO 8601 format.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        sip_trunk_domain: Optional[str] = None,
    ):
        super().__init__(version)

        self.sip_trunk_domain: Optional[str] = payload.get("sip_trunk_domain")
        self.url: Optional[str] = payload.get("url")
        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.voice_region: Optional[str] = payload.get("voice_region")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )

        self._solution = {
            "sip_trunk_domain": sip_trunk_domain or self.sip_trunk_domain,
        }
        self._context: Optional[TrunkContext] = None

    @property
    def _proxy(self) -> "TrunkContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: TrunkContext for this TrunkInstance
        """
        if self._context is None:
            self._context = TrunkContext(
                self._version,
                sip_trunk_domain=self._solution["sip_trunk_domain"],
            )
        return self._context

    def fetch(self) -> "TrunkInstance":
        """
        Fetch the TrunkInstance


        :returns: The fetched TrunkInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "TrunkInstance":
        """
        Asynchronous coroutine to fetch the TrunkInstance


        :returns: The fetched TrunkInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        voice_region: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
    ) -> "TrunkInstance":
        """
        Update the TrunkInstance

        :param voice_region: The Inbound Processing Region used for this SIP Trunk for voice
        :param friendly_name: A human readable description of this resource, up to 64 characters.

        :returns: The updated TrunkInstance
        """
        return self._proxy.update(
            voice_region=voice_region,
            friendly_name=friendly_name,
        )

    async def update_async(
        self,
        voice_region: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
    ) -> "TrunkInstance":
        """
        Asynchronous coroutine to update the TrunkInstance

        :param voice_region: The Inbound Processing Region used for this SIP Trunk for voice
        :param friendly_name: A human readable description of this resource, up to 64 characters.

        :returns: The updated TrunkInstance
        """
        return await self._proxy.update_async(
            voice_region=voice_region,
            friendly_name=friendly_name,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Routes.V2.TrunkInstance {}>".format(context)


class TrunkContext(InstanceContext):
    def __init__(self, version: Version, sip_trunk_domain: str):
        """
        Initialize the TrunkContext

        :param version: Version that contains the resource
        :param sip_trunk_domain: The absolute URL of the SIP Trunk
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sip_trunk_domain": sip_trunk_domain,
        }
        self._uri = "/Trunks/{sip_trunk_domain}".format(**self._solution)

    def fetch(self) -> TrunkInstance:
        """
        Fetch the TrunkInstance


        :returns: The fetched TrunkInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return TrunkInstance(
            self._version,
            payload,
            sip_trunk_domain=self._solution["sip_trunk_domain"],
        )

    async def fetch_async(self) -> TrunkInstance:
        """
        Asynchronous coroutine to fetch the TrunkInstance


        :returns: The fetched TrunkInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return TrunkInstance(
            self._version,
            payload,
            sip_trunk_domain=self._solution["sip_trunk_domain"],
        )

    def update(
        self,
        voice_region: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
    ) -> TrunkInstance:
        """
        Update the TrunkInstance

        :param voice_region: The Inbound Processing Region used for this SIP Trunk for voice
        :param friendly_name: A human readable description of this resource, up to 64 characters.

        :returns: The updated TrunkInstance
        """
        data = values.of(
            {
                "VoiceRegion": voice_region,
                "FriendlyName": friendly_name,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TrunkInstance(
            self._version, payload, sip_trunk_domain=self._solution["sip_trunk_domain"]
        )

    async def update_async(
        self,
        voice_region: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
    ) -> TrunkInstance:
        """
        Asynchronous coroutine to update the TrunkInstance

        :param voice_region: The Inbound Processing Region used for this SIP Trunk for voice
        :param friendly_name: A human readable description of this resource, up to 64 characters.

        :returns: The updated TrunkInstance
        """
        data = values.of(
            {
                "VoiceRegion": voice_region,
                "FriendlyName": friendly_name,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TrunkInstance(
            self._version, payload, sip_trunk_domain=self._solution["sip_trunk_domain"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Routes.V2.TrunkContext {}>".format(context)


class TrunkList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the TrunkList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(self, sip_trunk_domain: str) -> TrunkContext:
        """
        Constructs a TrunkContext

        :param sip_trunk_domain: The absolute URL of the SIP Trunk
        """
        return TrunkContext(self._version, sip_trunk_domain=sip_trunk_domain)

    def __call__(self, sip_trunk_domain: str) -> TrunkContext:
        """
        Constructs a TrunkContext

        :param sip_trunk_domain: The absolute URL of the SIP Trunk
        """
        return TrunkContext(self._version, sip_trunk_domain=sip_trunk_domain)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Routes.V2.TrunkList>"
