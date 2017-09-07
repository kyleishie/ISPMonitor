"""This is my docstring."""
import sys
sys.path.insert(0, 'SpeedTesters')
sys.path.insert(0, 'Archivers')
from Repeater import Repeater
from PreferredSpeedTester import PreferredSpeedTester
from TestResultArchive import TestResultArchive

testResultArchive = TestResultArchive()
for testResult in testResultArchive.testResults():
    print(testResult.description())


def performSpeedTest(tester=PreferredSpeedTester()):
    testResult = tester.performTest()
    print(testResult.description())
    testResultArchive.append(testResult)


# Start a Repeater
repeater = Repeater(60, performSpeedTest)
repeater.start()
