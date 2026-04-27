from ex0 import FlameFactory, AquaFactory
from ex0.factory import CreatureFactory
from ex1 import HealCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex2.strategy import BattleStrategy, InvalidStrategyCombinationError


def single_battle(opp: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opp)} opponents involved\n")

    for i in range(len(opp)):
        for j in range(i + 1, len(opp)):
            f1, s1 = opp[i]
            f2, s2 = opp[j]

            c1 = f1.create_base()
            c2 = f2.create_base()

            print("* Battle *")
            print(c1.describe())
            print("vs. ")
            print(c2.describe())
            print("now fight!")

            try:
                s1.act(c1)
                s2.act(c2)
                print("")
            except InvalidStrategyCombinationError as e:
                print(f"Battle error, aborting tournament: {e}\n")
                return


if __name__ == "__main__":

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    single_battle([
        (FlameFactory(), NormalStrategy()),
        (HealCreatureFactory(), DefensiveStrategy()),
    ])

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    single_battle([
        (FlameFactory(), AggressiveStrategy()),
        (HealCreatureFactory(), DefensiveStrategy()),
    ])

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    single_battle([
        (AquaFactory(), NormalStrategy()),
        (HealCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ])
