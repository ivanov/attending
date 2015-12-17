# content of test_sample.py
def test_this():
    # is there a import context manager?
    import this
    assert this.__doc__ == None

def test_attending():
    import attending
    import this
    assert this.__doc__ != None



def test_attending():
    import attending
    import this
    attending.concur()
    assert this.__doc__ != None
    assert this.__doc__.endswith("I concur.")
