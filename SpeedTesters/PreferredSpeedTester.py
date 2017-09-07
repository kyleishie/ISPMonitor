"""A Proxy to the users preferred SpeedTester."""
from SpeedTest import SpeedTester
from Fast_Com import Fast_Com
from MockSpeedTester import MockSpeedTester
from Speedtest_Net import Speedtest_Net
from RandomSpeedTester import RandomSpeedTester


class PreferredSpeedTester(SpeedTester):
    """A Proxy to the users preferred SpeedTester."""

    def performTest(self):
        """Perform a SpeedTest using the user's preferred SpeedTester."""
        # TODO: Repspect User Preferences Here
        return RandomSpeedTester().performTest()
