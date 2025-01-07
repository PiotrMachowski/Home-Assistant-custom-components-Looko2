from abc import ABC
from typing import Self


class LookO2Exception(Exception, ABC):
    pass


class LookO2MissingDataException(LookO2Exception):
    def __init__(self, *missing_fields: str) -> None:
        super().__init__(f'Missing data for required fields: {", ".join(missing_fields)}')


class LookO2UnauthorizedException(LookO2Exception):
    def __init__(self: Self, status_code: int, response: str) -> None:
        super().__init__(f'Unauthorized access: {status_code}')
        self.status_code = status_code
        self.response = response


class LookO2ApiException(LookO2Exception):
    def __init__(self: Self, status_code: int, response: str) -> None:
        super().__init__(f'Api error: {status_code}')
        self.status_code = status_code
        self.response = response


class LookO2InvalidDeviceIdException(LookO2Exception):
    def __init__(self: Self, device_id: str) -> None:
        super().__init__(f'Invalid device id: {device_id}')
        self.device_id = device_id
