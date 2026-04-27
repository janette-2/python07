from abc import ABC, abstractmethod
from ex0.factory import Creature
from ex1.capability import TransformCapability, HealCapability


class InvalidStrategyCombinationError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, cr: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, cr: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, cr: Creature) -> None:
        print(cr.attack())

    def is_valid(self, cr: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):

    def act(self, cr: Creature) -> None:
        # isinstance() allows the program to determine
        # the 'parents' and therefore, the methods that
        # the generic 'Creature' is narrowed to, letting
        # access to the specific attributes of a Creature
        # after isinstance is checked
        if not isinstance(cr, TransformCapability):
            raise InvalidStrategyCombinationError(
                f"Invalid Creature '{cr.name}' for this aggressive strategy")
        print(cr.transform())
        print(cr.attack())
        print(cr.revert())

    def is_valid(self, cr: Creature) -> bool:
        return isinstance(cr, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def act(self, cr: Creature) -> None:
        if not isinstance(cr, HealCapability):
            raise InvalidStrategyCombinationError(
                f"Invalid Creature '{cr.name}' for this defensive strategy")
        print(cr.attack())
        print(cr.heal())

    def is_valid(self, cr: Creature) -> bool:
        return isinstance(cr, TransformCapability)
