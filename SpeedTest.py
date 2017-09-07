"""SpeedTester."""
import datetime
import json
import dateutil.parser


class SpeedTestResult(object):
    """Represents the results of a test performed by a SpeedTester."""

    def __init__(self, download, startTime, ping=None, upload=None, endTime=None):
        """Results of a speedtest performed by a SpeedTester."""
        super(SpeedTestResult, self).__init__()
        self.download = download
        self.upload = upload
        self.ping = ping
        self.startTime = startTime
        self.endTime = endTime
        if self.endTime is None:
            self.endTime = datetime.datetime.now()
        self.duration = round((self.endTime - self.startTime).total_seconds(), 2)

    def description(self):
        """Return string describing the test result."""
        durationString = "{}s".format(self.duration)
        downloadSpeedString = "{} Kbps".format(self.download)
        uploadSpeedString = "{} Kbps".format(self.upload)
        return "\t".join((self.startTime.isoformat(), downloadSpeedString, uploadSpeedString, durationString))

    def toString(self):
        """Return JSON String."""
        return json.dumps(self)

    def toJSON(self):
        """Return JSON String of Test Result."""
        return {
            "start": self.startTime.isoformat(),
            "end": self.endTime.isoformat(),
            "duration": self.duration,
            "download": self.download,
            "upload": self.upload,
            "ping": self.ping
        }

    def fromJSON(json):
        """Instantiate a SpeedTestResult from JSON."""
        startTime = dateutil.parser.parse(json["start"])
        endTime = dateutil.parser.parse(json["end"])
        return SpeedTestResult(json["download"], startTime, ping=json["ping"], upload=json["upload"], endTime=endTime)


class SpeedTester:
    """Interface for an object that can produce SpeedTestResult(s)."""

    def performTest(self):
        """Perform the speedtest and return a SpeedTestResult."""
        raise NotImplementedError("performTest must be implemented.")


class SpeedTestResultArchive(object):
    """Interface for an object that can persist SpeedTestResult objects."""

    def testResults(self):
        """Return all SpeedTestResultObjects."""
        raise NotImplementedError("testResults must be implemented.")

    def append(self):
        """Append a SpeedTestResult to the persistent store."""
        raise NotImplementedError("append must be implemented.")
