class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class EventGet:
    def __init__(self, type_):
        self.type_ = type_


class EventSet:
    def __init__(self, value):
        self.value = value


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, some_object, event):
        if self.__successor is not None:
            return self.__successor.handle(some_object, event)


class IntHandler(NullHandler):
    def handle(self, some_object, event):
        if isinstance(event, EventGet) and event.type_ is int:
            return some_object.integer_field
        elif isinstance(event, EventSet) and type(event.value) is int:
            some_object.integer_field = event.value
        else:
            return super().handle(some_object, event)


class FloatHandler(NullHandler):
    def handle(self, some_object, event):
        if isinstance(event, EventGet) and event.type_ is float:
            return some_object.float_field
        elif isinstance(event, EventSet) and type(event.value) is float:
            some_object.float_field = event.value
        else:
            return super().handle(some_object, event)


class StrHandler(NullHandler):
    def handle(self, some_object, event):
        if isinstance(event, EventGet) and event.type_ is str:
            return some_object.string_field
        elif isinstance(event, EventSet) and type(event.value) is str:
            some_object.string_field = event.value
        else:
            return super().handle(some_object, event)


# obj = SomeObject()
# obj.integer_field = 42
# obj.float_field = 3.14
# obj.string_field = "some text"
#
# chain = IntHandler(FloatHandler(StrHandler(NullHandler())))
#
# print(chain.handle(obj, EventGet(int)))
# chain.handle(obj, EventSet(43))
# print(chain.handle(obj, EventGet(int)))
#
# print(chain.handle(obj, EventGet(str)))

