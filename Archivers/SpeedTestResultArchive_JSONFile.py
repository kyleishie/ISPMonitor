"""JSON File Archiver for SpeedTestResult Objects."""
from SpeedTest import SpeedTestResultArchive
from SpeedTest import SpeedTestResult
import json


class SpeedTestResultArchive_JSONFile(SpeedTestResultArchive):
    """Interface for an object that can archive a SpeedTestResult."""

    def __init__(self, file):
        """JSON_Archiver for SpeedTestResult Objects."""
        super(SpeedTestResultArchive_JSONFile, self).__init__()
        self.file = file

    def _load(self, file):
        """Load any and all stored SpeedTestResult Objects."""
        data = []
        try:
            dataStoreFile = open(file, "r")
            for line in dataStoreFile:
                testResultJSON = json.loads(line)
                testResult = SpeedTestResult.fromJSON(testResultJSON)
                if testResult is not None:
                    data.append(testResult)

        except IOError as e:
            print(e)

        return data

    def testResults(self):
        """Return all SpeedTestResultObjects."""
        return self._load(self.file)

    def append(self, testResult):
        """Archive the SpeedTestResult."""
        try:
            dataStoreFile = open(self.file, "a")
            # json.dump(data, dataStoreFile)
            dataStoreFile.write("{}\n".format(json.dumps(testResult.toJSON())))
        except IOError as e:
            print(e)
