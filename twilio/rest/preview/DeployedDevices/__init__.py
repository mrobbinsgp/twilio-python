"""
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

from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.preview.deployed_devices.fleet import FleetList


class DeployedDevices(Version):

    def __init__(self, domain: Domain):
        """
        Initialize the DeployedDevices version of Preview

        :param domain: The Twilio.preview domain
        """
        super().__init__(domain)
        self.version = 'DeployedDevices'
        self._fleets = None
        
    @property
    def fleets(self) -> FleetList:
        if self._fleets is None:
            self._fleets = FleetList(self)
        return self._fleets

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.DeployedDevices>'
