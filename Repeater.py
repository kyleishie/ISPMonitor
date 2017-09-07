"""Repeater."""
from threading import Timer


class Repeater():
    """A Timer class that does not stop, unless you want it to."""

    def __init__(self, seconds, target):
        """Instantiate a Repeater.

        seconds - The Amount of time to wait between repeats.
        target - The function to call when the repeater fires.
        """
        self._should_continue = False
        self.is_running = False
        self.seconds = seconds
        self.target = target
        self.thread = None

    def _handle_target(self):
        self.is_running = True
        self.target()
        self.is_running = False
        self._start_timer()

    def _start_timer(self):
        # Code could have been running when cancel was called.
        if self._should_continue:
            self.thread = Timer(self.seconds, self._handle_target)
            self.thread.start()

    def start(self, wait=False):
        """Start the Repeater. wait - Indicates whether the target should be called before starting the first timer."""
        if not self._should_continue and not self.is_running:
            self._should_continue = True
            if wait:
                self._start_timer()
            else:
                self._handle_target()
        else:
            print("Timer already started or running.")

    def cancel(self):
        """Cancel any existing timer."""
        if self.thread is not None:
            # Just in case thread is running and cancel fails.
            self._should_continue = False
            self.thread.cancel()
        else:
            print("Timer never started or failed to initialize.")
