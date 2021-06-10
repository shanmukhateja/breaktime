import threading
import time
from .constants import *
from .utils import format_time


class SessionCounter(threading.Thread):

    # used to kill thread
    can_run = True

    def run(self):
        self.start_time = time.time()
        self.tray.update(hover_text="New Session is starting!")
        while self.can_run:
            self.cur_time = time.time()
            self.delay = int(self.cur_time - self.start_time) + 3600
            if self.delay > 0:
                self.update_tray_icon()
            print("delay: "+str(self.delay))
            time.sleep(SESSION_COUNTER_POLL_INTERVAL)
        threading._shutdown()

    def update_tray_icon(self):
        # Tray seconds time
        self.tray.update(hover_text=format_time(self.delay))

        # Tray icon
        if self.delay <= SESSION_STATE_OKAY_INTERVAL:
            self.tray.update(icon=ICON_SESSION_OKAY)
        elif self.delay >= SESSION_STATE_WARN_INTERVAL and self.delay < SESSION_STATE_DANGER_INTERVAL:
            self.tray.update(icon=ICON_SESSION_WARN)
        elif self.delay >= SESSION_STATE_DANGER_INTERVAL:
            self.tray.update(icon=ICON_SESSION_DANGER,
                        hover_text=format_time(self.delay))

    def stop_session(self):
        self.can_run = False
        # reset tray
        self.reset_tray()

    def reset_tray(self):
        self.tray.update(hover_text=TITLE_APP, icon=ICON_APP)


    def __init__(self, tray):
        threading.Thread.__init__(self, daemon=True)
        self.tray = tray
        self.start()

