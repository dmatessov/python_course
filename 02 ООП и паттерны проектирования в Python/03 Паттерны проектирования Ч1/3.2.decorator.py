from abc import ABC, abstractmethod

# class Hero:
#     def __init__(self):
#         self.positive_effects = []
#         self.negative_effects = []
#         self.stats = {
#             "HP": 128,  # health points
#             "MP": 42,  # magic points,
#             "SP": 100,  # skill points
#             "Strength": 15,  # сила
#             "Perception": 4,  # восприятие
#             "Endurance": 8,  # выносливость
#             "Charisma": 2,  # харизма
#             "Intelligence": 3,  # интеллект
#             "Agility": 8,  # ловкость
#             "Luck": 1  # удача
#         }
#
#     def get_positive_effects(self):
#         return self.positive_effects.copy()
#
#     def get_negative_effects(self):
#         return self.negative_effects.copy()
#
#     def get_stats(self):
#         return self.stats.copy()


class AbstractEffect(Hero, ABC):
    def __init__(self, obj):
        self.base = obj

    @abstractmethod
    def get_positive_effects(self):
        #return self.base.get_positive_effects()
        pass

    @abstractmethod
    def get_negative_effects(self):
        #return self.base.get_negative_effects()
        pass

    @abstractmethod
    def get_stats(self):
        # return self.base.get_stats()
        pass


class AbstractPositive(AbstractEffect):
    def get_positive_effects(self):
        pe = self.base.get_positive_effects()
        pe.append(self.__class__.__name__)
        return pe

    def get_negative_effects(self):
        return self.base.get_negative_effects()

    @abstractmethod
    def get_stats(self):
        pass


class AbstractNegative(AbstractEffect):
    def get_positive_effects(self):
        return self.base.get_positive_effects()

    def get_negative_effects(self):
        ne = self.base.get_negative_effects()
        ne.append(self.__class__.__name__)
        return ne

    @abstractmethod
    def get_stats(self):
        pass



class Berserk(AbstractPositive):
    def get_stats(self):
        # Увеличивает характеристики: Сила, Выносливость, Ловкость, Удача на 7;
        # уменьшает характеристики: Восприятие, Харизма, Интеллект на 3;
        # количество единиц здоровья увеличивается на 50.
        st = self.base.get_stats()
        st["Strength"] = st["Strength"] + 7
        st["Endurance"] = st["Endurance"] + 7
        st["Agility"] = st["Agility"] + 7
        st["Luck"] = st["Luck"] + 7
        st["HP"] = st["HP"] + 50
        st["Perception"] = st["Perception"] - 3
        st["Charisma"] = st["Charisma"] - 3
        st["Intelligence"] = st["Intelligence"] - 3
        return st


class Blessing(AbstractPositive):
    # увеличивает все основные характеристики на 2.
    def get_stats(self):
        st = self.base.get_stats()
        st["Strength"] = st["Strength"] + 2
        st["Perception"] = st["Perception"] + 2
        st["Endurance"] = st["Endurance"] + 2
        st["Charisma"] = st["Charisma"] + 2
        st["Intelligence"] = st["Intelligence"] + 2
        st["Agility"] = st["Agility"] + 2
        st["Luck"] = st["Luck"] + 2
        return st


class Weakness(AbstractNegative):
    # уменьшает характеристики: Сила, Выносливость, Ловкость на 4.
    def get_stats(self):
        st = self.base.get_stats()
        st["Strength"] = st["Strength"] - 4
        st["Endurance"] = st["Endurance"] - 4
        st["Agility"] = st["Agility"] - 4
        return st


class Curse(AbstractNegative):
    # уменьшает все основные характеристики на 2.
    def get_stats(self):
        st = self.base.get_stats()
        st["Strength"] = st["Strength"] - 2
        st["Perception"] = st["Perception"] - 2
        st["Endurance"] = st["Endurance"] - 2
        st["Charisma"] = st["Charisma"] - 2
        st["Intelligence"] = st["Intelligence"] - 2
        st["Agility"] = st["Agility"] - 2
        st["Luck"] = st["Luck"] - 2
        return st


class EvilEye(AbstractNegative):
    # уменьшает  характеристику Удача на 10.
    def get_stats(self):
        st = self.base.get_stats()
        st["Luck"] = st["Luck"] - 10
        return st

# h = Hero()
# b = Berserk(h)
