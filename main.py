from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent

from pulsecontrol.pulse import set_volume, set_device
from pulsecontrol.actions import get_volume_actions, get_device_actions


class PulseControl(Extension):
    def __init__(self):
        super(PulseControl, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        func, data = event.get_data()
        if func == 'volume':
            set_volume(data)
            return get_volume_actions()
        elif func == 'device':
            result = set_device(data)
            return get_device_actions(error_msg=result)


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        query = event.get_argument() if event.get_argument() else ""
        if event.get_keyword() == 'volume':
            return get_volume_actions(query)
        elif event.get_keyword() == 'device':
            return get_device_actions(query)


if __name__ == '__main__':
    PulseControl().run()
