from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent, PreferencesUpdateEvent, PreferencesEvent, SystemExitEvent
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction

from pulsecontrol import controller, actions

PREFERENCES: dict = {}


class ItemEnterEventListener(EventListener):
    def on_event(self, event: ItemEnterEvent, extension: Extension) -> RenderResultListAction:
        func, data = event.get_data()
        if func == 'volume':
            try:
                controller.set_volume(data)
            except controller.DriverException as e:
                return actions.get_error_action(e.reason)
            return actions.get_volume_actions()
        elif func == 'device':
            try:
                controller.set_device(data)
            except controller.DriverException as e:
                return actions.get_device_actions(error_msg=e.reason)
            return actions.get_device_actions()
        else:
            return actions.get_error_action('Unknown event')


class KeywordQueryEventListener(EventListener):
    def on_event(self, event: KeywordQueryEvent, extension: Extension) -> RenderResultListAction:
        global PREFERENCES
        query = event.get_argument() or ""
        if event.get_keyword() == PREFERENCES['volume']:
            return actions.get_volume_actions(query)
        elif event.get_keyword() == PREFERENCES['device']:
            return actions.get_device_actions(query)


class PreferencesChangeKeywordListener(EventListener):
    def on_event(self, event: PreferencesUpdateEvent, extension: Extension):
        global PREFERENCES
        PREFERENCES[event.id] = event.new_value


class PreferencesListener(EventListener):
    def on_event(self, event: PreferencesEvent, extension: Extension):
        global PREFERENCES
        PREFERENCES = event.preferences
