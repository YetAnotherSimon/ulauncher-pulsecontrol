from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent, PreferencesUpdateEvent, PreferencesEvent, SystemExitEvent

from pulsecontrol import listeners


class PulseControl(Extension):
    def __init__(self) -> None:
        super(PulseControl, self).__init__()
        self.subscribe(KeywordQueryEvent, listeners.KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, listeners.ItemEnterEventListener())
        self.subscribe(PreferencesEvent, listeners.PreferencesListener())
        self.subscribe(PreferencesUpdateEvent, listeners.PreferencesChangeKeywordListener())


if __name__ == '__main__':
    PulseControl().run()
