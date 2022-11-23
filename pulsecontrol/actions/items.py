from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

VOLUME_ACTION_ITEMS = {
    'mute': {
        'item': ExtensionResultItem(
            icon='images/Flat Mixer.png',
            name='Mute',
            description='Mute audio',
            on_enter=ExtensionCustomAction(('volume', '0'), True)
        ),
        'keywords': ['mute', 'silent', 'minimize', 'deaf', 'down', 'lower', 'gentle', 'decrease', 'quietly']
    }, 'down': {
        'item': ExtensionResultItem(
            icon='images/Flat Mixer.png',
            name='Volume down',
            description='Decrease volume by 10%',
            on_enter=ExtensionCustomAction(('volume', '-10'), True)
        ),
        'keywords': ['down', 'lower', 'gentle', 'decrease', 'quietly', 'turn']
    }, 'normalize': {
        'item': ExtensionResultItem(
            icon='images/Flat Mixer.png',
            name='Normalize',
            description='Normalize volume at 50%',
            on_enter=ExtensionCustomAction(('volume', '50'), True)
        ),
        'keywords': ['normalize', 'normal', 'casual', 'mid', 'half', 'down', 'lower', 'gentle', 'decrease', 'quietly',
                     'up', 'higher', 'aloud', 'increase', 'loudly', 'turn']
    }, 'up': {
        'item': ExtensionResultItem(
            icon='images/Flat Mixer.png',
            name='Volume up',
            description='Increase volume by 10%',
            on_enter=ExtensionCustomAction(('volume', '+10'), True)
        ),
        'keywords': ['up', 'higher', 'aloud', 'increase', 'loudly', 'turn']
    }, 'maximize': {
        'item': ExtensionResultItem(
            icon='images/Flat Mixer.png',
            name='Maximize',
            description='Maximize volume to 100%',
            on_enter=ExtensionCustomAction(('volume', '100'), True)
        ),
        'keywords': ['full', 'maximize', 'up', 'higher', 'aloud', 'increase', 'loudly']
    }
}


def action_item_set_volume(percent: str) -> ExtensionResultItem:
    return ExtensionResultItem(
        icon='images/Flat Mixer.png',
        name='Set volume',
        on_enter=ExtensionCustomAction(('volume', percent), False)
    )


def action_item_error_msg(error_msg: str) -> ExtensionResultItem:
    return ExtensionResultItem(
        icon='images/Flat XLR.png',
        name='Something was gone wrong',
        description=f'Error Message: {error_msg}',
        on_enter=HideWindowAction()
    )


def action_item_change_device(device_name: str, device_description: str) -> ExtensionResultItem:
    return ExtensionResultItem(
        icon='images/Flat XLR.png',
        name=f'Device "{device_description}"',
        description='Change audio device',
        on_enter=ExtensionCustomAction(('device', device_name), False)
    )
