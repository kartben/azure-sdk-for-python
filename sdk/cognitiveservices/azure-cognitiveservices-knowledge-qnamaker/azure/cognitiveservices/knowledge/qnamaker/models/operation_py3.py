# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Operation(Model):
    """Record to track long running operation.

    :param operation_state: Operation state. Possible values include:
     'Failed', 'NotStarted', 'Running', 'Succeeded'
    :type operation_state: str or
     ~azure.cognitiveservices.knowledge.qnamaker.models.OperationStateType
    :param created_timestamp: Timestamp when the operation was created.
    :type created_timestamp: str
    :param last_action_timestamp: Timestamp when the current state was
     entered.
    :type last_action_timestamp: str
    :param resource_location: Relative URI to the target resource location for
     completed resources.
    :type resource_location: str
    :param user_id: User Id
    :type user_id: str
    :param operation_id: Operation Id.
    :type operation_id: str
    :param error_response: Error details in case of failures.
    :type error_response:
     ~azure.cognitiveservices.knowledge.qnamaker.models.ErrorResponse
    """

    _attribute_map = {
        'operation_state': {'key': 'operationState', 'type': 'str'},
        'created_timestamp': {'key': 'createdTimestamp', 'type': 'str'},
        'last_action_timestamp': {'key': 'lastActionTimestamp', 'type': 'str'},
        'resource_location': {'key': 'resourceLocation', 'type': 'str'},
        'user_id': {'key': 'userId', 'type': 'str'},
        'operation_id': {'key': 'operationId', 'type': 'str'},
        'error_response': {'key': 'errorResponse', 'type': 'ErrorResponse'},
    }

    def __init__(self, *, operation_state=None, created_timestamp: str=None, last_action_timestamp: str=None, resource_location: str=None, user_id: str=None, operation_id: str=None, error_response=None, **kwargs) -> None:
        super(Operation, self).__init__(**kwargs)
        self.operation_state = operation_state
        self.created_timestamp = created_timestamp
        self.last_action_timestamp = last_action_timestamp
        self.resource_location = resource_location
        self.user_id = user_id
        self.operation_id = operation_id
        self.error_response = error_response
