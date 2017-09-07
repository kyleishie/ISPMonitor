"""In-Memory Archiver for SpeedTestResult Objects."""
from SpeedTest import SpeedTestResultArchive


class SpeedTestResultArchive_InMemory(SpeedTestResultArchive):
    """Interface for an object that can archive a SpeedTestResult."""

    def __init__(self, dataSource=None):
        """JSON_Archiver for SpeedTestResult Objects."""
        super(SpeedTestResultArchive_InMemory, self).__init__()
        self.data = []
        if dataSource is not None:
            self._load(dataSource)

    def _load(self, dataSource):
        """Load any and all stored SpeedTestResult Objects."""
        self.data = dataSource.testResults()

    def testResults(self):
        """Return all SpeedTestResultObjects."""
        return self.data

    def append(self, testResult):
        """Archive the SpeedTestResult."""
        self.data.append(testResult)
