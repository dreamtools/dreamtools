from dreamtools.dream8.D8C1 import submissions



def test_submissions_sc1a():
    s = submissions.SC1ASubmissions()
    s.load_submissions()
    assert len(s.submissions) == 74
    s.summary_final()


def test_submissions_sc1b():
    s = submissions.SC1BSubmissions()
    s.load_submissions()
    assert len(s.submissions) == 65
    s.summary_final()


def test_submissions_sc2a():
    s = submissions.SC2ASubmissions()
    s.load_submissions()
    assert len(s.submissions) == 14
    s.summary_final()


def test_submissions_sc2b():
    s = submissions.SC2BSubmissions()
    s.load_submissions()
    assert len(s.submissions) == 11
    s.summary_final()

