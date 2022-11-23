# Ulauncher-PulseControl

_Ulauncher plugin to control pulseaudio/pipewire_

This plugin is meant to be used to quickly change audio device and set the current volume.

## Usage

Your system needs to use pulseaudio or pipewire with pulseaudio support for this plugin to work.

### Volume

The default keyword is 'volume'. You are offered several shortcut options for convenience, but you can also type in a
number between 0 and 100 to set the volume of the default output device to that percentage value.

### Device

The default keyword is 'device'. Without any arguments, it will show a list of your audio devices. Selecting one will 
set it as the default output device. You can also type in the name of the device to narrow the selection.

## Suggestions

If you have any suggestions or if you encounter any problems, you can always create an issue.
The plugin was built in ~~one~~ two days without intention to create a big thing. But I'm open to any suggestions and 
pull requests.

## License

[MIT License](./LICENSE)
