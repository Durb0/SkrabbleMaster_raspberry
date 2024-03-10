def inject(name, cls):
    def wrapper(target):
        setattr(target, name, cls.get_instance())
        return target
    return wrapper