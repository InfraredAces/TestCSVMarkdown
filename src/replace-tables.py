import pandas as pd

ps5_compatibility = pd.read_csv('playstation-5-Compatibility.csv')
usb_passthrough_devices = pd.read_csv('usb-passthrough-devices.csv')

with open('README.md', 'r') as readme:
    data = readme.read()

    ps5_compatibility_replace_txt = "--Playstation 5 Compatibility Table--"
    data = data.replace(ps5_compatibility_replace_txt, ps5_compatibility.to_markdown())


    usb_passthrough_devices_replace_text = "--USB Passthrough Authentication Device Table--"
    data = data.replace(usb_passthrough_devices_replace_text, usb_passthrough_devices.to_markdown())


with open(r'README.md', 'w') as readme:
    readme.write(data)