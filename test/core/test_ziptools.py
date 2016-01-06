from dreamtools.core.ziptools import ZIP


# most of the ZIP class is tests in various challenges
# Here, we just want to test things that fails.

def test_zip():
    z = ZIP()
    try:
        z.loadZIPFile('p')
    except:
        pass
