"""A SpeedTester that performs a random SpeedTester."""
from SpeedTest import SpeedTester
import random
from Fast_Com import Fast_Com
from MockSpeedTester import MockSpeedTester
from Speedtest_Net import Speedtest_Net


class RandomSpeedTester(SpeedTester):
    """A SpeedTester that performs a random SpeedTester."""

    def __init__(self):
        """Instantiate a SpeedTester that performs a random SpeedTest."""
        self.speedTesters = [
            # MockSpeedTester(),
            Fast_Com(),
            Speedtest_Net()
        ]

    def performTest(self):
        """Perform a SpeedTest using a random SpeedTester."""
        secure_random = random.SystemRandom()
        randomTester = secure_random.choice(self.speedTesters)
        return randomTester.performTest()
