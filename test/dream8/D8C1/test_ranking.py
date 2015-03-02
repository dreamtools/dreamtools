


from dreamtools.dream8.D8C1 import ranking


def test_sc1a_ranking():
    r = ranking.SC1A_ranking()
    r.append_submission("/home/cokelaer/.config/dreamtools/dream8/D8C1/submissions/sc1a/limax-Network.zip")
    assert r.get_rank_your_submission() == 2


def test_sc1b_ranking():
    r = ranking.SC1B_ranking()
    r.append_submission("/home/cokelaer/.config/dreamtools/dream8/D8C1/submissions/sc1b/NMSUSongLab-Network-Insilico.zip")
    assert r.get_rank_your_submission() == 1


