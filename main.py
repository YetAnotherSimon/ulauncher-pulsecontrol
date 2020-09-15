from logging import Logger, getLogger, FileHandler, StreamHandler, Formatter, DEBUG

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent, PreferencesUpdateEvent, PreferencesEvent, SystemExitEvent

from pulsecontrol.pulse import set_volume, set_device
from pulsecontrol.actions import get_volume_actions, get_device_actions

PREFERENCES = dict()


def setup_logger() -> Logger:
    logger = getLogger('ulauncher-pulsecontrol')
    logger.setLevel(DEBUG)
    formatter = Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
    file_handler = FileHandler(filename='/tmp/ulauncher-pulsecontrol.log', encoding='utf-8', mode='w')
    file_handler.setFormatter(formatter)
    stream_handler = StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger


def dismantle_logger(logger: Logger):
    handlers = logger.handlers.copy()
    for handler in handlers:
        handler.close()
        logger.removeHandler(handler)


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
    LOGGER = setup_logger()
    try:
        PulseControl().run()
    except SystemExitEvent:
        dismantle_logger(LOGGER)
