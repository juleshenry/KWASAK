from kwasak import kwasak, kwasak_static


def einstein():
    class Einstein:
        @kwasak
        def einstein(s, e: float = None, m: float = None, **kwargs):
            return  # decorator skips return

        def einstein__m(s, e: float):
            return e / 8.98755179e16

        def einstein__e(s, m: float) -> float:
            return m * 8.98755179e16

    e = Einstein()
    ans = e.einstein(e=1000)  # returns m, (1000 / 8.98755179 e16), ~1.11265 e -14
    assert 1.1126500557278013e-14 == (ans)
    ans = e.einstein(m=1000)  # returns e, 1000 * 8.98755179 e16, ~8.98755179 e19
    assert 8.98755179e19 == (ans)
    ans = e.einstein(e=ans)  # returns e, 1000 * 8.98755179 e16, ~8.98755179 e19
    assert 1000.0 == (ans)


def pythagoras():
    class Pythagoras:
        @kwasak
        def pythagorean(s, a: float = None, b: float = None, c: float = None, **kwargs):
            return

        def pythagorean__a(s, b: float, c: float):
            return (c**2 - b**2) ** 0.5

        def pythagorean__b(s, a: float, c: float):
            return (c**2 - a**2) ** 0.5

        def pythagorean__c(s, a: float, b: float):
            return (a**2 + b**2) ** 0.5

    p = Pythagoras()

    ans = p.pythagorean(a=12, c=13)  # 5
    assert 5 == (ans)
    ans = p.pythagorean(a=12, b=5)  # 13
    assert 13 == (ans), ans
    ans = p.pythagorean(b=5, c=13)  # 12
    assert 12 == (ans), ans


def vacuum_theory():
    class VacuumTheory:

        @kwasak
        def eqn_1_3(s, k=None, m=None, T=None, **kwargs):
            return

        def eqn_1_3__T(s, k: float, m: float):
            # .5 * m * v**2 = 1.5 * k * T
            result = []
            T = 0.333333333333333 * m**2 / k
            result.append(T)
            return T

        def eqn_1_3__k(s, T: float, m: float):
            # .5 * m * v**2 = 1.5 * k * T
            result = []
            k = 0.333333333333333 * m**2 / T
            result.append(k)
            return k

        def eqn_1_3__m(s, T: float, k: float):
            # .5 * m * v**2 = 1.5 * k * T
            result = []
            m = 3.0 * T * k**2
            result.append(m)
            return m

    VT = VacuumTheory()

    ans = VT.eqn_1_3(k=1, T=3)  # 5
    assert 9 == (ans), ans
    ans = VT.eqn_1_3(m=2, T=3)  # 12
    assert 0.444444444444444 == (ans), f"{ans}"
    ans = VT.eqn_1_3(m=2, k=1)  # 13
    assert 1.333333333333332 == (ans), ans

def pythagoras_static():
    class Pythagoras:
        @kwasak_static
        def pythagorean(a: float = None, b: float = None, c: float = None, **kwargs):
            return
        
        @staticmethod
        def pythagorean__a(b: float, c: float):
            return (c**2 - b**2) ** 0.5
        @staticmethod
        def pythagorean__b(a: float, c: float):
            return (c**2 - a**2) ** 0.5
        @staticmethod
        def pythagorean__c( a: float, b: float):
            return (a**2 + b**2) ** 0.5

    p = Pythagoras()

    ans = p.pythagorean(a=12, c=13)  # 5
    assert 5 == (ans)
    ans = p.pythagorean(a=12, b=5)  # 13
    assert 13 == (ans), ans
    ans = p.pythagorean(b=5, c=13)  # 12
    assert 12 == (ans), ans


def einstein_static():
    class Einstein:

        # @staticmethod/?
        @kwasak_static
        def einstein(e: float = None, m: float = None, **kwargs):
            return  # decorator skips return

        @staticmethod
        def einstein__m(e: float):
            return e / 8.98755179e16

        @staticmethod
        def einstein__e(m: float) -> float:
            return m * 8.98755179e16

    e = Einstein()
    ans = e.einstein(e=1000)  # returns m, (1000 / 8.98755179 e16), ~1.11265 e -14
    assert 1.1126500557278013e-14 == (ans)
    ans = e.einstein(m=1000)  # returns e, 1000 * 8.98755179 e16, ~8.98755179 e19
    assert 8.98755179e19 == (ans)
    ans = e.einstein(e=ans)  # returns e, 1000 * 8.98755179 e16, ~8.98755179 e19
    assert 1000.0 == (ans)

if __name__ == "__main__":
    einstein()
    print("Einstein, ✅")
    pythagoras()
    print("Pythagoras, ✅")
    vacuum_theory()
    print("Vacuum Theory, ✅")
    pythagoras_static()
    print("Einstein (Static), ✅")
    einstein_static()
    print("Einstein (Static), ✅")
    print("Done! ✅")
