import requests
import json

IS_DEBUGGING = False

# load the contents of settings into memory and write it
# such that it is private and called when each main method
# is called.
def readConfiguration(key, settingsPath='settings.json'):
    key = key or ''
    if key == '':
        print('Empty value for key received.')
        return ''

    jsonContents = None
    
    try:
        f = open(settingsPath, 'r')
        jsonContents = json.loads(f.read())
        return jsonContents[key]
    except FileNotFoundError:
        print('Settings file not found.')
        return ''
    finally:
        f.close()

# get authorization thing

# get the other thing