import typing
from .atomictest import AtomicTest
import attr


@attr.s
class Atomic:
    """A single Atomic data structure. Each Atomic (technique)
    will contain a list of one or more AtomicTest objects.
    """

    attack_technique                      = attr.ib()
    display_name                          = attr.ib()
    path                                  = attr.ib()
    atomic_tests: typing.List[AtomicTest] = attr.ib()

    def __attrs_post_init__(self):
        if self.atomic_tests:
            test_list = []
            for test in self.atomic_tests:
                test_list.append(AtomicTest(**test))
            self.atomic_tests = test_list