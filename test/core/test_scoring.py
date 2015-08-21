from dreamtools.core.scoring import scoring


def test_download_template():
    pass


def test_download_scoring():
    scoring(['dummy',  '--challenge', 'D3C1', '--download-template'])
    scoring(['dummy',  '--challenge', 'D3C2', '--download-template', '--sub-challenge', 'cytokine'])
 
 
 

