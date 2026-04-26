from abc import ABC, abstractmethod
from ex0.factory import Creature


# NEW CODE: -------------------------------
class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str = "") -> str:
        pass


class TransformCapability(ABC):

    def __init__(self) -> None:
        self.is_transformed = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Sproutling", "Grass")

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self, target: str = "") -> str:
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self, target: str = "") -> str:
        return "Bloomelle heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return "Morphagon unleashes a devastating morph strike!"
        return "Shiftling attacks normally."

    def transform(self) -> str:
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return "Shiftling performs a boosted strike!"
        return "Morphagon attacks normally."

    def transform(self) -> str:
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        return "Morphagon stabilizes its form."
