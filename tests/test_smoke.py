"""Smoke test: checks that the project installs and its basic pieces work.

A "smoke test" is the simplest possible test. If it fails, something is broken
at the most basic level (for example a missing package or a typo in a folder name).
"""

import importlib
import random

import numpy as np
import pytest

SUBPACKAGES = ["data", "models", "training", "evaluation", "inference"]


def test_package_imports_and_has_version():
    import answercheck

    assert isinstance(answercheck.__version__, str)


@pytest.mark.parametrize("name", SUBPACKAGES)
def test_subpackages_import(name):
    importlib.import_module(f"answercheck.{name}")


def test_set_seed_makes_random_numbers_repeatable():
    import torch

    from answercheck.training.seeds import set_seed

    def draw():
        return random.random(), np.random.rand(), torch.rand(1).item()

    set_seed(123)
    first = draw()
    set_seed(123)
    second = draw()
    assert first == second


def test_environment_report_lists_key_packages():
    from answercheck.environment import KEY_PACKAGES, environment_report

    report = environment_report()
    assert set(KEY_PACKAGES) == set(report["packages"])
    assert "available" in report["gpu"]
