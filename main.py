from logging import Logger, getLogger, FileHandler, StreamHandler, Formatter, DEBUG

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent, SystemExitEvent

from pulsecontrol.pulse import set_volume, set_device
from pulsecontrol.actions import get_volume_actions, get_device_actions


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
    LOGGER = setup_logger()
    try:
        PulseControl().run()
    except SystemExitEvent:
        dismantle_logger(LOGGER)
