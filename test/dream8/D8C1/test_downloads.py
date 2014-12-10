from dreamtools.dream8.D8C1 import downloads



def test_downloads_submissions():
    d = downloads.SubmissionsDownloader()
    d.download_all() # takes some time



def test_downloads_gs():
    d = downloads.GSDownloader()
    d.download_experimental()


