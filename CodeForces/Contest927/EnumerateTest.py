from enum import Enum


class F:
    def __init__(self, name):
        self.name = name


g = F
print(g, g("hello").name)


def makeEnum(name, dicctionary):
    i = j = None

    class E:
        nonlocal i, j
        for i, j in dicctionary.items():
            print(i, j)
            locals()[i] = j

        def __init__(self) -> None:
            x = 10
            print(locals()['self'])
    val = E.value1
    E.__name__ = name
    print(E.__name__)
    print(dir(E()))
    print(dir(Enum))
    return E


makeEnum("hello", {"value1": 1, "value2": 1})
