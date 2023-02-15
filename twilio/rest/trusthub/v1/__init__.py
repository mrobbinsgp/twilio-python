"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Trusthub
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.trusthub.v1.customer_profiles import CustomerProfilesList
from twilio.rest.trusthub.v1.end_user import EndUserList
from twilio.rest.trusthub.v1.end_user_type import EndUserTypeList
from twilio.rest.trusthub.v1.policies import PoliciesList
from twilio.rest.trusthub.v1.supporting_document import SupportingDocumentList
from twilio.rest.trusthub.v1.supporting_document_type import SupportingDocumentTypeList
from twilio.rest.trusthub.v1.trust_products import TrustProductsList


class V1(Version):

    def __init__(self, domain: Domain):
        """
        Initialize the V1 version of Trusthub

        :param domain: The Twilio.trusthub domain
        """
        super().__init__(domain)
        self.version = 'v1'
        self._customer_profiles = None
        self._end_users = None
        self._end_user_types = None
        self._policies = None
        self._supporting_documents = None
        self._supporting_document_types = None
        self._trust_products = None
        
    @property
    def customer_profiles(self) -> CustomerProfilesList:
        if self._customer_profiles is None:
            self._customer_profiles = CustomerProfilesList(self)
        return self._customer_profiles

    @property
    def end_users(self) -> EndUserList:
        if self._end_users is None:
            self._end_users = EndUserList(self)
        return self._end_users

    @property
    def end_user_types(self) -> EndUserTypeList:
        if self._end_user_types is None:
            self._end_user_types = EndUserTypeList(self)
        return self._end_user_types

    @property
    def policies(self) -> PoliciesList:
        if self._policies is None:
            self._policies = PoliciesList(self)
        return self._policies

    @property
    def supporting_documents(self) -> SupportingDocumentList:
        if self._supporting_documents is None:
            self._supporting_documents = SupportingDocumentList(self)
        return self._supporting_documents

    @property
    def supporting_document_types(self) -> SupportingDocumentTypeList:
        if self._supporting_document_types is None:
            self._supporting_document_types = SupportingDocumentTypeList(self)
        return self._supporting_document_types

    @property
    def trust_products(self) -> TrustProductsList:
        if self._trust_products is None:
            self._trust_products = TrustProductsList(self)
        return self._trust_products

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trusthub.V1>'
