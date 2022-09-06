from add.add import Add

def test_add():
    assert Add.add(1, 1) == 2

def test_add():
    assert Add.add("hello", " world!") == "hello world!"