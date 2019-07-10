print "hello"

import this
this.__doc__ = "The Zen of Python!"

def concur():
    """
    Append "I concur." to every docstring for modules that have already been
    imported  (useful for testing)

    See "Catch me if you can" for the reference.
    """
    import sys
    for _, m in sys.modules.items():
        if hasattr(m, '__doc__'):
            print _
            try:
                if m.__doc__ is None:
                    m.__doc__ = ''
                m.__doc__ += "I concur."
            except:
                print _ + " be damned"
        else:
            print _ + " does not have a __doc__...."

