r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Video
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from twilio.base import deserialize, serialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class SubscribeRulesInstance(InstanceResource):

    """
    :ivar participant_sid: The SID of the Participant resource for the Subscribe Rules.
    :ivar room_sid: The SID of the Room resource for the Subscribe Rules
    :ivar rules: A collection of Subscribe Rules that describe how to include or exclude matching tracks. See the [Specifying Subscribe Rules](https://www.twilio.com/docs/video/api/track-subscriptions#specifying-sr) section for further information.
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        room_sid: str,
        participant_sid: str,
    ):
        super().__init__(version)

        self.participant_sid: Optional[str] = payload.get("participant_sid")
        self.room_sid: Optional[str] = payload.get("room_sid")
        self.rules: Optional[List[str]] = payload.get("rules")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )

        self._solution = {
            "room_sid": room_sid,
            "participant_sid": participant_sid,
        }

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Video.V1.SubscribeRulesInstance {}>".format(context)


class SubscribeRulesList(ListResource):
    def __init__(self, version: Version, room_sid: str, participant_sid: str):
        """
        Initialize the SubscribeRulesList

        :param version: Version that contains the resource
        :param room_sid: The SID of the Room resource where the subscribe rules to update apply.
        :param participant_sid: The SID of the Participant resource to update the Subscribe Rules.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "room_sid": room_sid,
            "participant_sid": participant_sid,
        }
        self._uri = (
            "/Rooms/{room_sid}/Participants/{participant_sid}/SubscribeRules".format(
                **self._solution
            )
        )

    def fetch(self) -> SubscribeRulesInstance:
        """
        Asynchronously fetch the SubscribeRulesInstance

        :returns: The fetched SubscribeRulesInstance
        """
        payload = self._version.fetch(method="GET", uri=self._uri)

        return SubscribeRulesInstance(
            self._version,
            payload,
            room_sid=self._solution["room_sid"],
            participant_sid=self._solution["participant_sid"],
        )

    async def fetch_async(self) -> SubscribeRulesInstance:
        """
        Asynchronously fetch the SubscribeRulesInstance

        :returns: The fetched SubscribeRulesInstance
        """
        payload = await self._version.fetch_async(method="GET", uri=self._uri)

        return SubscribeRulesInstance(
            self._version,
            payload,
            room_sid=self._solution["room_sid"],
            participant_sid=self._solution["participant_sid"],
        )

    def update(
        self, rules: Union[object, object] = values.unset
    ) -> SubscribeRulesInstance:
        """
        Update the SubscribeRulesInstance

        :param rules: A JSON-encoded array of subscribe rules. See the [Specifying Subscribe Rules](https://www.twilio.com/docs/video/api/track-subscriptions#specifying-sr) section for further information.

        :returns: The created SubscribeRulesInstance
        """
        data = values.of(
            {
                "Rules": serialize.object(rules),
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SubscribeRulesInstance(
            self._version,
            payload,
            room_sid=self._solution["room_sid"],
            participant_sid=self._solution["participant_sid"],
        )

    async def update_async(
        self, rules: Union[object, object] = values.unset
    ) -> SubscribeRulesInstance:
        """
        Asynchronously update the SubscribeRulesInstance

        :param rules: A JSON-encoded array of subscribe rules. See the [Specifying Subscribe Rules](https://www.twilio.com/docs/video/api/track-subscriptions#specifying-sr) section for further information.

        :returns: The created SubscribeRulesInstance
        """
        data = values.of(
            {
                "Rules": serialize.object(rules),
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SubscribeRulesInstance(
            self._version,
            payload,
            room_sid=self._solution["room_sid"],
            participant_sid=self._solution["participant_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Video.V1.SubscribeRulesList>"
