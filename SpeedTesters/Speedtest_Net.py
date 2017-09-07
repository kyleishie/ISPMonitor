"""A Python interface for the speedtest.net SpeedTester."""
from SpeedTest import SpeedTester
from SpeedTest import SpeedTestResult
import speedtest
import datetime


class Speedtest_Net(SpeedTester):
    """A Proxy to the users preferred SpeedTester."""

    def performTest(self):
        """Perform a SpeedTest using speedtest.net."""
        startTime = datetime.datetime.now()
        s = speedtest.Speedtest()
        s.get_best_server()
        s.download()
        s.upload()

        download = round(s.results.download / 1000.0, 2)  # Bps to Kbps
        upload = round(s.results.upload / 1000.0, 2)  # Bps to Kbps
        ping = round(s.results.ping / 1000.0, 2)  # ms to s

        return SpeedTestResult(download, startTime, ping, upload)
