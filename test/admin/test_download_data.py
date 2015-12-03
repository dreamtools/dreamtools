import dreamtools.admin.download_data as ds
from nose.plugins.attrib import attr


@attr('skip')
def test_ds():


    b = ds.DREAMToolsBundle()
    b.download_all()
