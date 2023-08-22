r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Voice
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import date
from twilio.base.instance_context import InstanceContext

from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class ArchivedCallContext(InstanceContext):
    def __init__(self, version: Version, date: date, sid: str):
        """
        Initialize the ArchivedCallContext

        :param version: Version that contains the resource
        :param date: The date of the Call in UTC.
        :param sid: The Twilio-provided Call SID that uniquely identifies the Call resource to delete
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "date": date,
            "sid": sid,
        }
        self._uri = "/Archives/{date}/Calls/{sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the ArchivedCallInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ArchivedCallInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Voice.V1.ArchivedCallContext {}>".format(context)


class ArchivedCallList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the ArchivedCallList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(self, date: date, sid: str) -> ArchivedCallContext:
        """
        Constructs a ArchivedCallContext

        :param date: The date of the Call in UTC.
        :param sid: The Twilio-provided Call SID that uniquely identifies the Call resource to delete
        """
        return ArchivedCallContext(self._version, date=date, sid=sid)

    def __call__(self, date: date, sid: str) -> ArchivedCallContext:
        """
        Constructs a ArchivedCallContext

        :param date: The date of the Call in UTC.
        :param sid: The Twilio-provided Call SID that uniquely identifies the Call resource to delete
        """
        return ArchivedCallContext(self._version, date=date, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Voice.V1.ArchivedCallList>"
