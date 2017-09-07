"""A Python interface for Netflix's Fast.com Speedtester."""
from SpeedTest import SpeedTester
from SpeedTest import SpeedTestResult
import fastdotcom as FastSpeedTest
import datetime


class Fast_Com(SpeedTester):
    """Netflix's Fast.com Speedtester."""

    def performTest(self):
        """Perform the Fast.com SpeedTest."""
        startTime = datetime.datetime.now()
        downloadSpeed = FastSpeedTest.fast_com() * 1000.0  # convert to Kbps
        return SpeedTestResult(downloadSpeed, startTime)
