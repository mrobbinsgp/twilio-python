r"""
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

from typing import Any, Dict, Optional, Union
from twilio.base import serialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class ComplianceRegistrationInquiriesInstance(InstanceResource):

    class BusinessIdentityType(object):
        DIRECT_CUSTOMER = "direct_customer"
        ISV_RESELLER_OR_PARTNER = "isv_reseller_or_partner"
        UNKNOWN = "unknown"

    class EndUserType(object):
        INDIVIDUAL = "Individual"
        BUSINESS = "Business"

    class PhoneNumberType(object):
        LOCAL = "local"
        NATIONAL = "national"
        MOBILE = "mobile"
        TOLL_FREE = "toll-free"

    """
    :ivar inquiry_id: The unique ID used to start an embedded compliance registration session.
    :ivar inquiry_session_token: The session token used to start an embedded compliance registration session.
    :ivar registration_id: The RegistrationId matching the Registration Profile that should be resumed or resubmitted for editing.
    :ivar url: The URL of this resource.
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.inquiry_id: Optional[str] = payload.get("inquiry_id")
        self.inquiry_session_token: Optional[str] = payload.get("inquiry_session_token")
        self.registration_id: Optional[str] = payload.get("registration_id")
        self.url: Optional[str] = payload.get("url")

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Trusthub.V1.ComplianceRegistrationInquiriesInstance>"


class ComplianceRegistrationInquiriesList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the ComplianceRegistrationInquiriesList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = (
            "/ComplianceInquiries/Registration/RegulatoryCompliance/GB/Initialize"
        )

    def create(
        self,
        end_user_type: "ComplianceRegistrationInquiriesInstance.EndUserType",
        phone_number_type: "ComplianceRegistrationInquiriesInstance.PhoneNumberType",
        business_identity_type: Union[
            "ComplianceRegistrationInquiriesInstance.BusinessIdentityType", object
        ] = values.unset,
        business_registration_authority: Union[str, object] = values.unset,
        business_legal_name: Union[str, object] = values.unset,
        notification_email: Union[str, object] = values.unset,
        accepted_notification_receipt: Union[bool, object] = values.unset,
        business_registration_number: Union[str, object] = values.unset,
        business_website_url: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        authorized_representative1_first_name: Union[str, object] = values.unset,
        authorized_representative1_last_name: Union[str, object] = values.unset,
        authorized_representative1_phone: Union[str, object] = values.unset,
        authorized_representative1_email: Union[str, object] = values.unset,
        authorized_representative1_date_of_birth: Union[str, object] = values.unset,
        address_street: Union[str, object] = values.unset,
        address_street_secondary: Union[str, object] = values.unset,
        address_city: Union[str, object] = values.unset,
        address_subdivision: Union[str, object] = values.unset,
        address_postal_code: Union[str, object] = values.unset,
        address_country_code: Union[str, object] = values.unset,
        emergency_address_street: Union[str, object] = values.unset,
        emergency_address_street_secondary: Union[str, object] = values.unset,
        emergency_address_city: Union[str, object] = values.unset,
        emergency_address_subdivision: Union[str, object] = values.unset,
        emergency_address_postal_code: Union[str, object] = values.unset,
        emergency_address_country_code: Union[str, object] = values.unset,
        use_address_as_emergency_address: Union[bool, object] = values.unset,
        file_name: Union[str, object] = values.unset,
        file: Union[str, object] = values.unset,
    ) -> ComplianceRegistrationInquiriesInstance:
        """
        Create the ComplianceRegistrationInquiriesInstance

        :param end_user_type:
        :param phone_number_type:
        :param business_identity_type:
        :param business_registration_authority: The authority that registered the business
        :param business_legal_name: he name of the business or organization using the Tollfree number.
        :param notification_email: he email address to receive the notification about the verification result.
        :param accepted_notification_receipt: The email address to receive the notification about the verification result.
        :param business_registration_number: Business registration number of the business
        :param business_website_url: The URL of the business website
        :param friendly_name: Friendly name for your business information
        :param authorized_representative1_first_name: First name of the authorized representative
        :param authorized_representative1_last_name: Last name of the authorized representative
        :param authorized_representative1_phone: Phone number of the authorized representative
        :param authorized_representative1_email: Email address of the authorized representative
        :param authorized_representative1_date_of_birth: Birthdate of the authorized representative
        :param address_street: Street address of the business
        :param address_street_secondary: Street address of the business
        :param address_city: City of the business
        :param address_subdivision: State or province of the business
        :param address_postal_code: Postal code of the business
        :param address_country_code: Country code of the business
        :param emergency_address_street: Street address of the business
        :param emergency_address_street_secondary: Street address of the business
        :param emergency_address_city: City of the business
        :param emergency_address_subdivision: State or province of the business
        :param emergency_address_postal_code: Postal code of the business
        :param emergency_address_country_code: Country code of the business
        :param use_address_as_emergency_address: Use the business address as the emergency address
        :param file_name: The name of the verification document to upload
        :param file: The verification document to upload

        :returns: The created ComplianceRegistrationInquiriesInstance
        """

        data = values.of(
            {
                "EndUserType": end_user_type,
                "PhoneNumberType": phone_number_type,
                "BusinessIdentityType": business_identity_type,
                "BusinessRegistrationAuthority": business_registration_authority,
                "BusinessLegalName": business_legal_name,
                "NotificationEmail": notification_email,
                "AcceptedNotificationReceipt": serialize.boolean_to_string(
                    accepted_notification_receipt
                ),
                "BusinessRegistrationNumber": business_registration_number,
                "BusinessWebsiteUrl": business_website_url,
                "FriendlyName": friendly_name,
                "AuthorizedRepresentative1FirstName": authorized_representative1_first_name,
                "AuthorizedRepresentative1LastName": authorized_representative1_last_name,
                "AuthorizedRepresentative1Phone": authorized_representative1_phone,
                "AuthorizedRepresentative1Email": authorized_representative1_email,
                "AuthorizedRepresentative1DateOfBirth": authorized_representative1_date_of_birth,
                "AddressStreet": address_street,
                "AddressStreetSecondary": address_street_secondary,
                "AddressCity": address_city,
                "AddressSubdivision": address_subdivision,
                "AddressPostalCode": address_postal_code,
                "AddressCountryCode": address_country_code,
                "EmergencyAddressStreet": emergency_address_street,
                "EmergencyAddressStreetSecondary": emergency_address_street_secondary,
                "EmergencyAddressCity": emergency_address_city,
                "EmergencyAddressSubdivision": emergency_address_subdivision,
                "EmergencyAddressPostalCode": emergency_address_postal_code,
                "EmergencyAddressCountryCode": emergency_address_country_code,
                "UseAddressAsEmergencyAddress": serialize.boolean_to_string(
                    use_address_as_emergency_address
                ),
                "FileName": file_name,
                "File": file,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ComplianceRegistrationInquiriesInstance(self._version, payload)

    async def create_async(
        self,
        end_user_type: "ComplianceRegistrationInquiriesInstance.EndUserType",
        phone_number_type: "ComplianceRegistrationInquiriesInstance.PhoneNumberType",
        business_identity_type: Union[
            "ComplianceRegistrationInquiriesInstance.BusinessIdentityType", object
        ] = values.unset,
        business_registration_authority: Union[str, object] = values.unset,
        business_legal_name: Union[str, object] = values.unset,
        notification_email: Union[str, object] = values.unset,
        accepted_notification_receipt: Union[bool, object] = values.unset,
        business_registration_number: Union[str, object] = values.unset,
        business_website_url: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        authorized_representative1_first_name: Union[str, object] = values.unset,
        authorized_representative1_last_name: Union[str, object] = values.unset,
        authorized_representative1_phone: Union[str, object] = values.unset,
        authorized_representative1_email: Union[str, object] = values.unset,
        authorized_representative1_date_of_birth: Union[str, object] = values.unset,
        address_street: Union[str, object] = values.unset,
        address_street_secondary: Union[str, object] = values.unset,
        address_city: Union[str, object] = values.unset,
        address_subdivision: Union[str, object] = values.unset,
        address_postal_code: Union[str, object] = values.unset,
        address_country_code: Union[str, object] = values.unset,
        emergency_address_street: Union[str, object] = values.unset,
        emergency_address_street_secondary: Union[str, object] = values.unset,
        emergency_address_city: Union[str, object] = values.unset,
        emergency_address_subdivision: Union[str, object] = values.unset,
        emergency_address_postal_code: Union[str, object] = values.unset,
        emergency_address_country_code: Union[str, object] = values.unset,
        use_address_as_emergency_address: Union[bool, object] = values.unset,
        file_name: Union[str, object] = values.unset,
        file: Union[str, object] = values.unset,
    ) -> ComplianceRegistrationInquiriesInstance:
        """
        Asynchronously create the ComplianceRegistrationInquiriesInstance

        :param end_user_type:
        :param phone_number_type:
        :param business_identity_type:
        :param business_registration_authority: The authority that registered the business
        :param business_legal_name: he name of the business or organization using the Tollfree number.
        :param notification_email: he email address to receive the notification about the verification result.
        :param accepted_notification_receipt: The email address to receive the notification about the verification result.
        :param business_registration_number: Business registration number of the business
        :param business_website_url: The URL of the business website
        :param friendly_name: Friendly name for your business information
        :param authorized_representative1_first_name: First name of the authorized representative
        :param authorized_representative1_last_name: Last name of the authorized representative
        :param authorized_representative1_phone: Phone number of the authorized representative
        :param authorized_representative1_email: Email address of the authorized representative
        :param authorized_representative1_date_of_birth: Birthdate of the authorized representative
        :param address_street: Street address of the business
        :param address_street_secondary: Street address of the business
        :param address_city: City of the business
        :param address_subdivision: State or province of the business
        :param address_postal_code: Postal code of the business
        :param address_country_code: Country code of the business
        :param emergency_address_street: Street address of the business
        :param emergency_address_street_secondary: Street address of the business
        :param emergency_address_city: City of the business
        :param emergency_address_subdivision: State or province of the business
        :param emergency_address_postal_code: Postal code of the business
        :param emergency_address_country_code: Country code of the business
        :param use_address_as_emergency_address: Use the business address as the emergency address
        :param file_name: The name of the verification document to upload
        :param file: The verification document to upload

        :returns: The created ComplianceRegistrationInquiriesInstance
        """

        data = values.of(
            {
                "EndUserType": end_user_type,
                "PhoneNumberType": phone_number_type,
                "BusinessIdentityType": business_identity_type,
                "BusinessRegistrationAuthority": business_registration_authority,
                "BusinessLegalName": business_legal_name,
                "NotificationEmail": notification_email,
                "AcceptedNotificationReceipt": serialize.boolean_to_string(
                    accepted_notification_receipt
                ),
                "BusinessRegistrationNumber": business_registration_number,
                "BusinessWebsiteUrl": business_website_url,
                "FriendlyName": friendly_name,
                "AuthorizedRepresentative1FirstName": authorized_representative1_first_name,
                "AuthorizedRepresentative1LastName": authorized_representative1_last_name,
                "AuthorizedRepresentative1Phone": authorized_representative1_phone,
                "AuthorizedRepresentative1Email": authorized_representative1_email,
                "AuthorizedRepresentative1DateOfBirth": authorized_representative1_date_of_birth,
                "AddressStreet": address_street,
                "AddressStreetSecondary": address_street_secondary,
                "AddressCity": address_city,
                "AddressSubdivision": address_subdivision,
                "AddressPostalCode": address_postal_code,
                "AddressCountryCode": address_country_code,
                "EmergencyAddressStreet": emergency_address_street,
                "EmergencyAddressStreetSecondary": emergency_address_street_secondary,
                "EmergencyAddressCity": emergency_address_city,
                "EmergencyAddressSubdivision": emergency_address_subdivision,
                "EmergencyAddressPostalCode": emergency_address_postal_code,
                "EmergencyAddressCountryCode": emergency_address_country_code,
                "UseAddressAsEmergencyAddress": serialize.boolean_to_string(
                    use_address_as_emergency_address
                ),
                "FileName": file_name,
                "File": file,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ComplianceRegistrationInquiriesInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Trusthub.V1.ComplianceRegistrationInquiriesList>"
