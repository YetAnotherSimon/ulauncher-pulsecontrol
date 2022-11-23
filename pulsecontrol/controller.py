from typing import List, Tuple
from types import ModuleType

from pulsecontrol import adapter as pulse_adapter

adapter = pulse_adapter
DriverException = pulse_adapter.DriverException


def set_adapter(adapter_module: ModuleType) -> None:
    global adapter, DriverException
    adapter = adapter_module
    DriverException = adapter_module.DriverException


def set_volume(percent: str) -> None:
    adapter.set_volume(percent)


def set_device(name: str) -> None:
    adapter.set_default_input_device(name)


def get_devices() -> List[Tuple[str, str]]:
    devices = adapter.get_input_devices()
    return [(device['name'], device['description']) for device in devices]


if __name__ == '__main__':
    exit(0)
