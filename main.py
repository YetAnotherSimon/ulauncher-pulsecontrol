from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent, PreferencesUpdateEvent, PreferencesEvent, SystemExitEvent

from pulsecontrol.pulse import set_volume, set_device
from pulsecontrol.actions import get_volume_actions, get_device_actions

PREFERENCES = dict()


class PulseControl(Extension):
    def __init__(self):
        super(PulseControl, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())
        self.subscribe(PreferencesEvent, PreferencesListener())
        self.subscribe(PreferencesUpdateEvent, PreferencesChangeKeywordListener())


class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        func, data = event.get_data()
        LOGGER.info(func)
        if func == 'volume':
            set_volume(data)
            return get_volume_actions()
        elif func == 'device':
            result = set_device(data)
            return get_device_actions(error_msg=result)


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        global PREFERENCES
        query = event.get_argument() if event.get_argument() else ""
        if event.get_keyword() == PREFERENCES['volume']:
            return get_volume_actions(query)
        elif event.get_keyword() == PREFERENCES['device']:
            return get_device_actions(query)


class PreferencesChangeKeywordListener(EventListener):
    def on_event(self, event, extension):
        global PREFERENCES
        PREFERENCES[event.id] = event.new_value


class PreferencesListener(EventListener):
    def on_event(self, event, extension):
        global PREFERENCES
        PREFERENCES = event.preferences


if __name__ == '__main__':
    PulseControl().run()
