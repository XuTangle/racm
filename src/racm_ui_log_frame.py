"""Subclass of LogFrame, which is generated by wxFormBuilder."""

import racm_ui
from logcat import LogCatThread
import time


# Implementing LogFrame
class LogFrame(racm_ui.LogFrame):
    _thread = None

    def __init__(self, parent, host, adb):
        racm_ui.LogFrame.__init__(self, parent)
        self._adb = adb
        self.SetTitle("LogCat: " + host)
        self._thread = LogCatThread(adb, host, self.log_text)
        self._thread.setDaemon(True)  # Terminate when end of UI thread.
        self._thread.start()
        time.sleep(1)
        self._thread.ready()

    # Handlers for LogFrame events.
    def on_log_closed(self, event):
        self._thread.stop()
        self.Destroy()
