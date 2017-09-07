"""A Mock SpeedTester for testing."""
from SpeedTest import SpeedTester
from SpeedTest import SpeedTestResult
import datetime


class MockSpeedTester(SpeedTester):
    """Mock Speedtester."""

    def performTest(self):
        """Perform a Mock SpeedTest."""
        startTime = datetime.datetime.now()
        endTime = datetime.datetime.now() + datetime.timedelta(seconds=10)
        return SpeedTestResult(100000.0, startTime, 10000.0, 10.0, endTime)
