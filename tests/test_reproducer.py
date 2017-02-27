import reproducer.const


def test_one():
    assert reproducer.const.ONE == 1


def test_two():
    assert reproducer.const.TWO == 2


def test_import_lxml():
    import lxml
    assert lxml.__file__.startswith("/usr/lib64")


def test_import_kernelconfig():
    import kernelconfig
    assert "/.tox/python/lib" in kernelconfig.__file__
