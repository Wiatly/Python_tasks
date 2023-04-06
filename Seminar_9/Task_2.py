class DocMeta(type):
    a = None

    def __call__(cls, *args, **kwargs):
        if not cls.a:
            cls.a = type.__call__(cls, *args, **kwargs)
        return cls.a


class My_class(metaclass=DocMeta):
    pass


class Wy_class():
    pass


obj_1 = My_class()
print(obj_1)
obj_2 = My_class()
print(obj_2)
obj_3 = My_class()
print(obj_2)
obj_4 = My_class()
print(obj_2)
print(obj_1 is obj_4)

obj_5 = Wy_class()
print(obj_5)
obj_6 = Wy_class()
print(obj_6)
obj_7 = Wy_class()
print(obj_7)
obj_8 = Wy_class()
print(obj_8)
print(obj_6 is obj_8)
