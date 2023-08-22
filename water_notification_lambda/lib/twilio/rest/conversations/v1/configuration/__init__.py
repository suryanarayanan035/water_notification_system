r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Conversations
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Any, Dict, Optional, Union
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version

from twilio.rest.conversations.v1.configuration.webhook import WebhookList


class ConfigurationInstance(InstanceResource):

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this configuration.
    :ivar default_chat_service_sid: The SID of the default [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) used when creating a conversation.
    :ivar default_messaging_service_sid: The SID of the default [Messaging Service](https://www.twilio.com/docs/sms/services/api) used when creating a conversation.
    :ivar default_inactive_timer: Default ISO8601 duration when conversation will be switched to `inactive` state. Minimum value for this timer is 1 minute.
    :ivar default_closed_timer: Default ISO8601 duration when conversation will be switched to `closed` state. Minimum value for this timer is 10 minutes.
    :ivar url: An absolute API resource URL for this global configuration.
    :ivar links: Contains absolute API resource URLs to access the webhook and default service configurations.
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.default_chat_service_sid: Optional[str] = payload.get(
            "default_chat_service_sid"
        )
        self.default_messaging_service_sid: Optional[str] = payload.get(
            "default_messaging_service_sid"
        )
        self.default_inactive_timer: Optional[str] = payload.get(
            "default_inactive_timer"
        )
        self.default_closed_timer: Optional[str] = payload.get("default_closed_timer")
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._context: Optional[ConfigurationContext] = None

    @property
    def _proxy(self) -> "ConfigurationContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ConfigurationContext for this ConfigurationInstance
        """
        if self._context is None:
            self._context = ConfigurationContext(
                self._version,
            )
        return self._context

    def fetch(self) -> "ConfigurationInstance":
        """
        Fetch the ConfigurationInstance


        :returns: The fetched ConfigurationInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "ConfigurationInstance":
        """
        Asynchronous coroutine to fetch the ConfigurationInstance


        :returns: The fetched ConfigurationInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        default_chat_service_sid: Union[str, object] = values.unset,
        default_messaging_service_sid: Union[str, object] = values.unset,
        default_inactive_timer: Union[str, object] = values.unset,
        default_closed_timer: Union[str, object] = values.unset,
    ) -> "ConfigurationInstance":
        """
        Update the ConfigurationInstance

        :param default_chat_service_sid: The SID of the default [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to use when creating a conversation.
        :param default_messaging_service_sid: The SID of the default [Messaging Service](https://www.twilio.com/docs/sms/services/api) to use when creating a conversation.
        :param default_inactive_timer: Default ISO8601 duration when conversation will be switched to `inactive` state. Minimum value for this timer is 1 minute.
        :param default_closed_timer: Default ISO8601 duration when conversation will be switched to `closed` state. Minimum value for this timer is 10 minutes.

        :returns: The updated ConfigurationInstance
        """
        return self._proxy.update(
            default_chat_service_sid=default_chat_service_sid,
            default_messaging_service_sid=default_messaging_service_sid,
            default_inactive_timer=default_inactive_timer,
            default_closed_timer=default_closed_timer,
        )

    async def update_async(
        self,
        default_chat_service_sid: Union[str, object] = values.unset,
        default_messaging_service_sid: Union[str, object] = values.unset,
        default_inactive_timer: Union[str, object] = values.unset,
        default_closed_timer: Union[str, object] = values.unset,
    ) -> "ConfigurationInstance":
        """
        Asynchronous coroutine to update the ConfigurationInstance

        :param default_chat_service_sid: The SID of the default [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to use when creating a conversation.
        :param default_messaging_service_sid: The SID of the default [Messaging Service](https://www.twilio.com/docs/sms/services/api) to use when creating a conversation.
        :param default_inactive_timer: Default ISO8601 duration when conversation will be switched to `inactive` state. Minimum value for this timer is 1 minute.
        :param default_closed_timer: Default ISO8601 duration when conversation will be switched to `closed` state. Minimum value for this timer is 10 minutes.

        :returns: The updated ConfigurationInstance
        """
        return await self._proxy.update_async(
            default_chat_service_sid=default_chat_service_sid,
            default_messaging_service_sid=default_messaging_service_sid,
            default_inactive_timer=default_inactive_timer,
            default_closed_timer=default_closed_timer,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Conversations.V1.ConfigurationInstance>"


class ConfigurationContext(InstanceContext):
    def __init__(self, version: Version):
        """
        Initialize the ConfigurationContext

        :param version: Version that contains the resource
        """
        super().__init__(version)

        self._uri = "/Configuration"

    def fetch(self) -> ConfigurationInstance:
        """
        Fetch the ConfigurationInstance


        :returns: The fetched ConfigurationInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ConfigurationInstance(
            self._version,
            payload,
        )

    async def fetch_async(self) -> ConfigurationInstance:
        """
        Asynchronous coroutine to fetch the ConfigurationInstance


        :returns: The fetched ConfigurationInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return ConfigurationInstance(
            self._version,
            payload,
        )

    def update(
        self,
        default_chat_service_sid: Union[str, object] = values.unset,
        default_messaging_service_sid: Union[str, object] = values.unset,
        default_inactive_timer: Union[str, object] = values.unset,
        default_closed_timer: Union[str, object] = values.unset,
    ) -> ConfigurationInstance:
        """
        Update the ConfigurationInstance

        :param default_chat_service_sid: The SID of the default [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to use when creating a conversation.
        :param default_messaging_service_sid: The SID of the default [Messaging Service](https://www.twilio.com/docs/sms/services/api) to use when creating a conversation.
        :param default_inactive_timer: Default ISO8601 duration when conversation will be switched to `inactive` state. Minimum value for this timer is 1 minute.
        :param default_closed_timer: Default ISO8601 duration when conversation will be switched to `closed` state. Minimum value for this timer is 10 minutes.

        :returns: The updated ConfigurationInstance
        """
        data = values.of(
            {
                "DefaultChatServiceSid": default_chat_service_sid,
                "DefaultMessagingServiceSid": default_messaging_service_sid,
                "DefaultInactiveTimer": default_inactive_timer,
                "DefaultClosedTimer": default_closed_timer,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ConfigurationInstance(self._version, payload)

    async def update_async(
        self,
        default_chat_service_sid: Union[str, object] = values.unset,
        default_messaging_service_sid: Union[str, object] = values.unset,
        default_inactive_timer: Union[str, object] = values.unset,
        default_closed_timer: Union[str, object] = values.unset,
    ) -> ConfigurationInstance:
        """
        Asynchronous coroutine to update the ConfigurationInstance

        :param default_chat_service_sid: The SID of the default [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to use when creating a conversation.
        :param default_messaging_service_sid: The SID of the default [Messaging Service](https://www.twilio.com/docs/sms/services/api) to use when creating a conversation.
        :param default_inactive_timer: Default ISO8601 duration when conversation will be switched to `inactive` state. Minimum value for this timer is 1 minute.
        :param default_closed_timer: Default ISO8601 duration when conversation will be switched to `closed` state. Minimum value for this timer is 10 minutes.

        :returns: The updated ConfigurationInstance
        """
        data = values.of(
            {
                "DefaultChatServiceSid": default_chat_service_sid,
                "DefaultMessagingServiceSid": default_messaging_service_sid,
                "DefaultInactiveTimer": default_inactive_timer,
                "DefaultClosedTimer": default_closed_timer,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ConfigurationInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Conversations.V1.ConfigurationContext>"


class ConfigurationList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the ConfigurationList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._webhooks: Optional[WebhookList] = None

    @property
    def webhooks(self) -> WebhookList:
        """
        Access the webhooks
        """
        if self._webhooks is None:
            self._webhooks = WebhookList(self._version)
        return self._webhooks

    def get(self) -> ConfigurationContext:
        """
        Constructs a ConfigurationContext

        """
        return ConfigurationContext(self._version)

    def __call__(self) -> ConfigurationContext:
        """
        Constructs a ConfigurationContext

        """
        return ConfigurationContext(self._version)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Conversations.V1.ConfigurationList>"