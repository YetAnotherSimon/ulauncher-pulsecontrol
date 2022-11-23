from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction

from pulsecontrol import controller
from pulsecontrol.actions import items

device_cache = None


def get_volume_actions(query: str = "") -> RenderResultListAction:
    if query.isdecimal():
        return RenderResultListAction([items.action_item_set_volume(query)])

    action_items = []
    for item in items.VOLUME_ACTION_ITEMS:
        if any([query in keyword for keyword in items.VOLUME_ACTION_ITEMS[item]['keywords']]):
            action_items.append(items.VOLUME_ACTION_ITEMS[item]['item'])

    return RenderResultListAction(action_items)


def get_device_actions(query: str = "", error_msg: str | None = None) -> RenderResultListAction:
    global device_cache
    if query == "":
        try:
            device_cache = controller.get_devices()
        except controller.DriverException as e:
            return RenderResultListAction([items.action_item_error_msg(e.reason)])

    device_actions = list()

    if error_msg:
        device_actions.append(items.action_item_error_msg(error_msg))

    for device in device_cache:
        if query in device[1]:
            device_actions.append(items.action_item_change_device(device[0], device[1]))

    return RenderResultListAction(device_actions)


def get_error_action(error_msg: str) -> RenderResultListAction:
    return RenderResultListAction([items.action_item_error_msg(error_msg)])


if __name__ == '__main__':
    exit(0)
