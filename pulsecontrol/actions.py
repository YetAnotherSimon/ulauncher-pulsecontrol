from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

from pulsecontrol.pulse import get_devices

VOLUME_ACTIONS = dict()
VOLUME_ACTIONS['mute'] = (
    ExtensionResultItem(icon='images/Flat Mixer.png',
                        name='Mute',
                        description='Mute audio',
                        on_enter=ExtensionCustomAction(('volume', '0'), True)),
    ['mute', 'silent', 'minimize', 'deaf', 'down', 'lower', 'gentle', 'decrease', 'quietly']

)
VOLUME_ACTIONS['down'] = (
    ExtensionResultItem(icon='images/Flat Mixer.png',
                        name='Volume down',
                        description='Decrease volume by 10%',
                        on_enter=ExtensionCustomAction(('volume', '-10'), True)),
    ['down', 'lower', 'gentle', 'decrease', 'quietly', 'turn']
)
VOLUME_ACTIONS['normalize'] = (
    ExtensionResultItem(icon='images/Flat Mixer.png',
                        name='Normalize',
                        description='Normalize volume at 50%',
                        on_enter=ExtensionCustomAction(('volume', '50'), True)),
    ['normalize', 'normal', 'casual', 'mid', 'half', 'down', 'lower', 'gentle', 'decrease', 'quietly', 'up', 'higher',
     'aloud', 'increase', 'loudly', 'turn']
)
VOLUME_ACTIONS['up'] = (
    ExtensionResultItem(icon='images/Flat Mixer.png',
                        name='Volume up',
                        description='Increase volume by 10%',
                        on_enter=ExtensionCustomAction(('volume', '+10'), True)),
    ['up', 'higher', 'aloud', 'increase', 'loudly', 'turn']
)
VOLUME_ACTIONS['maximize'] = (
    ExtensionResultItem(icon='images/Flat Mixer.png',
                        name='Maximize',
                        description='Maximize volume to 100%',
                        on_enter=ExtensionCustomAction(('volume', '100'), True)),
    ['full', 'maximize', 'up', 'higher', 'aloud', 'increase', 'loudly']
)


def get_volume_actions(query: str = "") -> RenderResultListAction:
    volume_actions = list()
    if query.isdecimal():
        volume_actions.append(ExtensionResultItem(icon='images/Flat Mixer.png',
                                                  name='Set volume',
                                                  on_enter=ExtensionCustomAction(('volume', query), False)))
        return RenderResultListAction(volume_actions)
    for act in VOLUME_ACTIONS:
        for keyword in VOLUME_ACTIONS[act][1]:
            if query in keyword:
                volume_actions.append(VOLUME_ACTIONS[act][0])
                break
    return RenderResultListAction(volume_actions)


DEVICE_CACHE = None


def get_device_actions(query: str = "", error_msg: str = "") -> RenderResultListAction:
    global DEVICE_CACHE

    if query == "":
        DEVICE_CACHE = get_devices()

    device_actions = list()

    if error_msg != "":
        device_actions.append(ExtensionResultItem(icon='images/Flat XLR.png',
                                                  name='Something was gone wrong',
                                                  description=f'Error Message: {error_msg}',
                                                  on_enter=HideWindowAction()))
    print(DEVICE_CACHE)
    for device in DEVICE_CACHE:
        print(device)
        if query in device[1]:
            print(query)
            device_actions.append(ExtensionResultItem(icon='images/Flat XLR.png',
                                                      name=f'Device "{device[1]}"',
                                                      description='Change audio device',
                                                      on_enter=ExtensionCustomAction(('device', device[0]), False)))

    return RenderResultListAction(device_actions)


if __name__ == '__main__':
    exit(0)
