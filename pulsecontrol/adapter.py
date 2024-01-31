from os import environ
from subprocess import run
from json import loads


class DriverException(Exception):
    def __init__(self, error_code: int, reason: str):
        self.error_code = error_code
        self.reason = reason


def _execute_pactl(cmd: str) -> str:
    bash_command = '/usr/bin/env bash -c "pactl {}"'.format(cmd)

    # pactl fix for versions prior 16.0
    env = environ.copy()
    env['LC_NUMERIC'] = 'C'
    
    process = run(
        bash_command,
        capture_output=True,
        shell=True,
        env=env
    )
    if process.returncode != 0:
        raise DriverException(error_code=process.returncode, reason=process.stderr.decode('ascii'))
    return process.stdout.decode('ascii')


def get_input_devices() -> dict:
    return loads(_execute_pactl('--format=json list sinks'))


def set_default_input_device(name: str) -> None:
    _execute_pactl('set-default-sink {}'.format(name))


def set_volume(percent: str, input_device: str = '@DEFAULT_SINK@') -> None:
    _execute_pactl('set-sink-volume {} {}%'.format(input_device, percent))
