from ex1 import HealCreatureFactory, TransformCreatureFactory


def test_heal_factory(factory: HealCreatureFactory) -> None:
    base = factory.create_base()
    evol = factory.create_evolved()

    print(" base:")
    print(f"{base.describe()}")
    print(f"{base.attack()}")
    print(f"{base.heal()}")

    print(" evolved:")
    print(f"{evol.describe()}")
    print(f"{evol.attack()}")
    print(f"{evol.heal()}")
    return


def test_trans_factory(factory: TransformCreatureFactory) -> None:
    base = factory.create_base()
    evol = factory.create_evolved()

    print(" base:")
    print(f"{base.describe()}")
    print(f"{base.attack()}")
    print(f"{base.transform()}")
    print(f"{base.attack()}")
    print(f"{base.revert()}")

    print(" evolved:")
    print(f"{evol.describe()}")
    print(f"{evol.attack()}")
    print(f"{evol.transform()}")
    print(f"{evol.attack()}")
    print(f"{evol.revert()}")
    return


if __name__ == "__main__":

    heal_ = HealCreatureFactory()
    trans = TransformCreatureFactory()

    print("Testing Creature with healing capability")
    test_heal_factory(heal_)

    print("\nTesting Creature with transform capability")
    test_trans_factory(trans)
