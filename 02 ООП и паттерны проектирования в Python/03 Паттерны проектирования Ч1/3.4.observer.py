from abc import ABC, abstractmethod

#
# class Engine:
#     pass


class ObservableEngine(Engine):
    def __init__(self):
        self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, message):
        self.achievements.add(message["title"])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = list()

    def update(self, message):
        try:
            _ = self.achievements.index(message)
        except ValueError:
            self.achievements.append(message)


# oe = ObservableEngine()
# sp = ShortNotificationPrinter()
# fp = FullNotificationPrinter()
#
# oe.subscribe(sp)
# oe.subscribe(fp)
#
# message = {"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"}
# oe.notify(message)
# oe.notify(message)
#
# print(sp.achievements)
# print(fp.achievements)
