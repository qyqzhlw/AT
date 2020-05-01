
def test_version():
    from at import __version__
    assert isinstance(__version__,str)