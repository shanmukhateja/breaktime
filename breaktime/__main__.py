from infi.systray import SysTrayIcon
from .constants import *
from .actions import *

def init():
  # Context menu actions
  menu_options = (
      (TITLE_SESSION_NEW, None, action_new_session),
      (TITLE_SESSION_STOP, None, action_stop_session),
  )

  systray = SysTrayIcon(ICON_APP, TITLE_APP, menu_options)
  systray.start()

if __name__ == '__main__':
  init()