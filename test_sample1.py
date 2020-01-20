import sample1


def test_check_for_pi():
    new = sample1.SampleClass()
    assert new.value_pi() == 3.141


def test_check_for_e():
    new = sample1.SampleClass()
    assert new.value_e() == 2.718


def test_check_for_gamma():
    new = sample1.SampleClass()
    assert new.value_gamma() == 0.577


def test_check_for_goldenratio():
    new = sample1.SampleClass()
    assert new.value_goldenratio() == 1.618
    del new  # Deleting the object
