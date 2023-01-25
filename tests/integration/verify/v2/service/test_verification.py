# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class VerificationTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .verifications.create(to="to", channel="channel")

        values = {'To': "to", 'Channel': "channel", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Verifications',
            data=values,
        ))

    def test_create_verification_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "to": "+15017122661",
                "channel": "sms",
                "status": "pending",
                "valid": false,
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "lookup": {},
                "amount": null,
                "payee": null,
                "send_code_attempts": [
                    {
                        "time": "2015-07-30T20:00:00Z",
                        "channel": "SMS",
                        "attempt_sid": "VLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "sna": null,
                "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications/VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .verifications.create(to="to", channel="channel")

        self.assertIsNotNone(actual)

    def test_create_verification_whatsapp_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "to": "+15017122661",
                "channel": "whatsapp",
                "status": "pending",
                "valid": false,
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "lookup": {},
                "amount": null,
                "payee": null,
                "send_code_attempts": [
                    {
                        "time": "2015-07-30T20:00:00Z",
                        "channel": "whatsapp",
                        "attempt_sid": "VLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "sna": null,
                "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications/VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .verifications.create(to="to", channel="channel")

        self.assertIsNotNone(actual)

    def test_create_verification_email_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "to": "mail@email.com",
                "channel": "email",
                "status": "pending",
                "valid": false,
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "lookup": {},
                "amount": null,
                "payee": null,
                "send_code_attempts": [
                    {
                        "time": "2015-07-30T20:00:00Z",
                        "channel": "EMAIL",
                        "attempt_sid": "VLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "sna": null,
                "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications/VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .verifications.create(to="to", channel="channel")

        self.assertIsNotNone(actual)

    def test_create_verification_with_rate_limits_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "to": "+15017122661",
                "channel": "sms",
                "status": "pending",
                "valid": false,
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "lookup": {},
                "amount": null,
                "payee": null,
                "send_code_attempts": [
                    {
                        "time": "2015-07-30T20:00:00Z",
                        "channel": "SMS",
                        "attempt_sid": "VLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "sna": null,
                "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications/VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .verifications.create(to="to", channel="channel")

        self.assertIsNotNone(actual)

    def test_create_verification_sna_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "to": "+15017122661",
                "channel": "sna",
                "status": "pending",
                "valid": false,
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "lookup": {
                    "carrier": {
                        "mobile_country_code": "311",
                        "type": "mobile",
                        "error_code": null,
                        "mobile_network_code": "180",
                        "name": "T-Mobile USA, Inc."
                    }
                },
                "amount": null,
                "payee": null,
                "send_code_attempts": [
                    {
                        "time": "2015-07-30T20:00:00Z",
                        "channel": "sna",
                        "attempt_sid": "VLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "sna": {
                    "url": "https://mi.dnlsrv.com/m/id/ANBByzx7?data=AAAglRRdNn02iTFWfDWwdTjOzM8o%2F6JB86fH%2Bt%2FFftUPj0pFA0u8%2FibWuYwzmMeMOtdTwYlsO8V%2FXF%2BJmngMhbeGKYhHeTOF2H9VrGEYKcEEklPxHgb5GgL3XtYa33j3lIU%2By6InvoV%2FowWHBzA0QeFPBh6vmJ8LoUPJqGE7q0PRz618Z4ym1AGq%2BaomSq9PlP4rCduv9Cmtxu%2FrvPSBwocs0GCWDE8seK8t9epmPQW7gwODxkAiKr9UxhJd9KvmBVuAQPf%2BoFQVo86USXkhXqTvUzB2bNUYY9FCy3CWgZFTOa1D3H1CVxf1eHzYIswNA7SmOzP%2FBX8g6%2B0hkzwMRkcit3gBNs4evAVJiqAgYvUlrtGwwv9bFx4X7jWSHY4%3D&cipherSalt=yANeDq09bwM38SJs"
                },
                "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications/VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .verifications.create(to="to", channel="channel")

        self.assertIsNotNone(actual)

    def test_create_verification_auto_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "to": "+15017122661",
                "channel": "sna",
                "status": "pending",
                "valid": false,
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "lookup": {
                    "carrier": {
                        "mobile_country_code": "311",
                        "type": "mobile",
                        "error_code": null,
                        "mobile_network_code": "180",
                        "name": "T-Mobile USA, Inc."
                    }
                },
                "amount": null,
                "payee": null,
                "send_code_attempts": [
                    {
                        "time": "2015-07-30T20:00:00Z",
                        "channel": "sna",
                        "attempt_sid": "VLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "sna": {
                    "url": "https://mi.dnlsrv.com/m/id/ANBByzx7?data=AAAglRRdNn02iTFWfDWwdTjOzM8o%2F6JB86fH%2Bt%2FFftUPj0pFA0u8%2FibWuYwzmMeMOtdTwYlsO8V%2FXF%2BJmngMhbeGKYhHeTOF2H9VrGEYKcEEklPxHgb5GgL3XtYa33j3lIU%2By6InvoV%2FowWHBzA0QeFPBh6vmJ8LoUPJqGE7q0PRz618Z4ym1AGq%2BaomSq9PlP4rCduv9Cmtxu%2FrvPSBwocs0GCWDE8seK8t9epmPQW7gwODxkAiKr9UxhJd9KvmBVuAQPf%2BoFQVo86USXkhXqTvUzB2bNUYY9FCy3CWgZFTOa1D3H1CVxf1eHzYIswNA7SmOzP%2FBX8g6%2B0hkzwMRkcit3gBNs4evAVJiqAgYvUlrtGwwv9bFx4X7jWSHY4%3D&cipherSalt=yANeDq09bwM38SJs"
                },
                "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications/VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .verifications.create(to="to", channel="channel")

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .verifications("sid").update(status="canceled")

        values = {'Status': "canceled", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Verifications/sid',
            data=values,
        ))

    def test_update_verification_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "to": "+15017122661",
                "channel": "sms",
                "status": "canceled",
                "valid": false,
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "lookup": {},
                "amount": null,
                "payee": null,
                "send_code_attempts": [
                    {
                        "time": "2015-07-30T20:00:00Z",
                        "channel": "SMS",
                        "attempt_sid": "VLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "sna": null,
                "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications/VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .verifications("sid").update(status="canceled")

        self.assertIsNotNone(actual)

    def test_approve_verification_with_pn_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "to": "+15017122661",
                "channel": "sms",
                "status": "approved",
                "valid": true,
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "lookup": {},
                "amount": null,
                "payee": null,
                "send_code_attempts": [
                    {
                        "time": "2015-07-30T20:00:00Z",
                        "channel": "SMS",
                        "attempt_sid": "VLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "sna": null,
                "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications/VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .verifications("sid").update(status="canceled")

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .verifications("sid").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Verifications/sid',
        ))

    def test_fetch_verification_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "to": "+15017122661",
                "channel": "sms",
                "status": "pending",
                "valid": false,
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "lookup": {},
                "amount": null,
                "payee": null,
                "send_code_attempts": [
                    {
                        "time": "2015-07-30T20:00:00Z",
                        "channel": "SMS",
                        "attempt_sid": "VLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "sna": null,
                "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications/VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.verify.v2.services("VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .verifications("sid").fetch()

        self.assertIsNotNone(actual)
