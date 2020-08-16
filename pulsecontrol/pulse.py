from subprocess import run, PIPE


def set_volume(percent: str):
    process = run('pacmd list-sinks | grep index', capture_output=True, shell=True, executable='/bin/bash')
    sinks = str(process.stdout)[2:-1].replace('\\t', '').rstrip('\\n').split('\\n')
    for sink in sinks:
        sink_index = sink.strip().split(' ')[-1]
        run('pactl -- set-sink-volume {} {}%'.format(sink_index, percent), shell=True, executable='/bin/bash')


def set_device(index: str) -> str:
    process = run('pacmd set-default-sink {}'.format(index, ), capture_output=True, shell=True, executable='/bin/bash')
    if process.returncode != 0:
        return str(process.stderr)[2:-1]
    process = run('pacmd list-sink-inputs | grep index', capture_output=True, shell=True, executable='/bin/bash')
    sinks = str(process.stdout)[2:-1].replace('\\t', '').rstrip('\\n').split('\\n')
    error = ""
    for sink in sinks:
        sink_index = sink.strip().split(' ')[1]
        process = run('pacmd move-sink-input {} {}'.format(sink_index, index), capture_output=True, shell=True,
                      executable='/bin/bash')
        if process.returncode != 0:
            error = process.stderr
    return error


def get_devices() -> list:
    process = run('pacmd list-sinks | grep -E "device.description|index"', capture_output=True, shell=True,
                  executable='/bin/bash')
    if process.returncode != 0:
        return list()
    devices = str(process.stdout)[2:-1].replace('\\t', '').rstrip('\\n').split('\\n')
    output = list()
    for i in range(0, len(devices), 2):
        index = devices[i].split(' ')[-1]
        description = devices[i+1].split('"')[-2]
        output.append((index, description))
    return output


if __name__ == '__main__':
    exit(0)
