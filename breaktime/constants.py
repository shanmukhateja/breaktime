import os.path

# App title
TITLE_APP = "Break Time!"

# Set BASE_PATH so project resources are correctly resolved
# TODO: Fix path determine logic, if applicable
if os.path.exists('./breaktime'):
    BASE_PATH = os.path.join('.')
else:
    path, _ = os.path.split(os.path.abspath(__file__))
    BASE_PATH = os.path.join(path, '../..')

# App icon
ICON_APP = os.path.join(BASE_PATH, 'icons/app.ico')


### Menu items
TITLE_SESSION_NEW = "New Session"
TITLE_SESSION_STOP = "Stop Session"

### Session items
TITLE_TAKE_BREAK = "Take a break!"
SESSION_COUNTER_POLL_INTERVAL = 5 # in seconds

SESSION_STATE_OKAY_INTERVAL = 10 # in seconds
ICON_SESSION_OKAY = os.path.join(BASE_PATH, "icons/session_ok.ico")

SESSION_STATE_WARN_INTERVAL = 200 # in seconds
ICON_SESSION_WARN = os.path.join(BASE_PATH, "icons/session_warn.ico")

SESSION_STATE_DANGER_INTERVAL = 300 # in seconds
ICON_SESSION_DANGER = os.path.join(BASE_PATH, "icons/session_danger.ico")
