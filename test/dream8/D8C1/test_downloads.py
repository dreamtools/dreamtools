from dreamtools.dream8.D8C1 import downloads
from nose.plugins.attrib import attr


@attr('skip')
def test_downloads_submissions():
    d = downloads.SubmissionsDownloader()
    d.download_all() # takes some time


