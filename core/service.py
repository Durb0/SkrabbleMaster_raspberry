from abc import ABC

# define decorator service
def Service(cls):
    # each service has a instance attribute
    cls.instance = None
    # each service has a get_instance static method
    cls.get_instance = staticmethod(lambda: cls.instance if cls.instance else cls())
    return cls