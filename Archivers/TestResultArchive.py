"""In-Memory Archiver for SpeedTestResult Objects backed by JSONFile Archiver."""
from SpeedTest import SpeedTestResultArchive
from SpeedTestResultArchive_JSONFile import SpeedTestResultArchive_JSONFile
from SpeedTestResultArchive_InMemory import SpeedTestResultArchive_InMemory


class TestResultArchive(SpeedTestResultArchive):
    """Interface for an object that can archive a SpeedTestResult."""

    def __init__(self):
        """JSON_Archiver for SpeedTestResult Objects."""
        super(TestResultArchive, self).__init__()
        self.jsonArchive = SpeedTestResultArchive_JSONFile("data.json")
        self.inMemoryArchive = SpeedTestResultArchive_InMemory(dataSource=self.jsonArchive)

    def testResults(self):
        """Return all SpeedTestResultObjects."""
        return self.inMemoryArchive.testResults()

    def append(self, testResult):
        """Archive the SpeedTestResult."""
        self.inMemoryArchive.append(testResult)
        self.jsonArchive.append(testResult)
