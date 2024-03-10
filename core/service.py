from abc import ABC

# define decorator service
def Service(cls):

    cls.instance = None

    def get_instance():
        if not cls.instance:
            cls.instance = cls()
        return cls.instance

    cls.get_instance = staticmethod(lambda: get_instance())
    return cls