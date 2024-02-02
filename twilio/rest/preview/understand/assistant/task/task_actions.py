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

from typing import Any, Dict, Optional, Union
from twilio.base import serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class TaskActionsInstance(InstanceResource):
    """
    :ivar account_sid: The unique ID of the Account that created this Field.
    :ivar assistant_sid: The unique ID of the parent Assistant.
    :ivar task_sid: The unique ID of the Task.
    :ivar url:
    :ivar data:
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        assistant_sid: str,
        task_sid: str,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.assistant_sid: Optional[str] = payload.get("assistant_sid")
        self.task_sid: Optional[str] = payload.get("task_sid")
        self.url: Optional[str] = payload.get("url")
        self.data: Optional[Dict[str, object]] = payload.get("data")

        self._solution = {
            "assistant_sid": assistant_sid,
            "task_sid": task_sid,
        }
        self._context: Optional[TaskActionsContext] = None

    @property
    def _proxy(self) -> "TaskActionsContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: TaskActionsContext for this TaskActionsInstance
        """
        if self._context is None:
            self._context = TaskActionsContext(
                self._version,
                assistant_sid=self._solution["assistant_sid"],
                task_sid=self._solution["task_sid"],
            )
        return self._context

    def fetch(self) -> "TaskActionsInstance":
        """
        Fetch the TaskActionsInstance


        :returns: The fetched TaskActionsInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "TaskActionsInstance":
        """
        Asynchronous coroutine to fetch the TaskActionsInstance


        :returns: The fetched TaskActionsInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self, actions: Union[object, object] = values.unset
    ) -> "TaskActionsInstance":
        """
        Update the TaskActionsInstance

        :param actions: The JSON actions that instruct the Assistant how to perform this task.

        :returns: The updated TaskActionsInstance
        """
        return self._proxy.update(
            actions=actions,
        )

    async def update_async(
        self, actions: Union[object, object] = values.unset
    ) -> "TaskActionsInstance":
        """
        Asynchronous coroutine to update the TaskActionsInstance

        :param actions: The JSON actions that instruct the Assistant how to perform this task.

        :returns: The updated TaskActionsInstance
        """
        return await self._proxy.update_async(
            actions=actions,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Understand.TaskActionsInstance {}>".format(context)


class TaskActionsContext(InstanceContext):
    def __init__(self, version: Version, assistant_sid: str, task_sid: str):
        """
        Initialize the TaskActionsContext

        :param version: Version that contains the resource
        :param assistant_sid: The unique ID of the parent Assistant.
        :param task_sid: The unique ID of the Task.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
            "task_sid": task_sid,
        }
        self._uri = "/Assistants/{assistant_sid}/Tasks/{task_sid}/Actions".format(
            **self._solution
        )

    def fetch(self) -> TaskActionsInstance:
        """
        Fetch the TaskActionsInstance


        :returns: The fetched TaskActionsInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return TaskActionsInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
        )

    async def fetch_async(self) -> TaskActionsInstance:
        """
        Asynchronous coroutine to fetch the TaskActionsInstance


        :returns: The fetched TaskActionsInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return TaskActionsInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
        )

    def update(
        self, actions: Union[object, object] = values.unset
    ) -> TaskActionsInstance:
        """
        Update the TaskActionsInstance

        :param actions: The JSON actions that instruct the Assistant how to perform this task.

        :returns: The updated TaskActionsInstance
        """
        data = values.of(
            {
                "Actions": serialize.object(actions),
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TaskActionsInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
        )

    async def update_async(
        self, actions: Union[object, object] = values.unset
    ) -> TaskActionsInstance:
        """
        Asynchronous coroutine to update the TaskActionsInstance

        :param actions: The JSON actions that instruct the Assistant how to perform this task.

        :returns: The updated TaskActionsInstance
        """
        data = values.of(
            {
                "Actions": serialize.object(actions),
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TaskActionsInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Understand.TaskActionsContext {}>".format(context)


class TaskActionsList(ListResource):
    def __init__(self, version: Version, assistant_sid: str, task_sid: str):
        """
        Initialize the TaskActionsList

        :param version: Version that contains the resource
        :param assistant_sid: The unique ID of the parent Assistant.
        :param task_sid: The unique ID of the Task.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
            "task_sid": task_sid,
        }

    def get(self) -> TaskActionsContext:
        """
        Constructs a TaskActionsContext

        """
        return TaskActionsContext(
            self._version,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
        )

    def __call__(self) -> TaskActionsContext:
        """
        Constructs a TaskActionsContext

        """
        return TaskActionsContext(
            self._version,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Understand.TaskActionsList>"
