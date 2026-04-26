from ex0 import CreatureFactory, FlameFactory, AquaFactory

flame = FlameFactory()
aqua = AquaFactory()


def test_factories(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evol = factory.create_evolved()
    print(f"{base.describe()}")
    print(f"{base.attack()}")
    print(f"{evol.describe()}")
    print(f"{evol.attack()}")
    return


def battle(f1: CreatureFactory, f2: CreatureFactory) -> None:
    f1_base = f1.create_base()
    f2_base = f2.create_base()

    print(f"{f1_base.describe()}\n vs.\n {f2_base.describe()}\n  fight!")
    print(f"{f1_base.attack()}")
    print(f"{f2_base.attack()}")


if __name__ == "__main__":
    print("Testing factory")
    test_factories(flame)

    print("\nTesting factory")
    test_factories(aqua)

    print("\nTesting battle")
    battle(flame, aqua)
