"""Fix random seeds so that a run can be repeated and give the same result.

Deep learning uses randomness in many places (shuffling data, starting weights,
dropout). Setting every random number generator to the same starting value
("seed") makes runs repeatable.
"""

import os
import random

import numpy as np


def set_seed(seed: int = 42, deterministic: bool = False) -> int:
    """Set the seed for Python, NumPy and PyTorch (CPU and GPU).

    Args:
        seed: any whole number. We log it with every run.
        deterministic: if True, also ask PyTorch to use only repeatable GPU
            algorithms. This is slower, so it is off by default.

    Returns:
        The seed that was used, so callers can log it.
    """
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)

    # Import torch here so the rest of this file works even before torch loads.
    import torch

    torch.manual_seed(seed)  # also seeds all GPUs in recent PyTorch versions
    if deterministic:
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
        torch.use_deterministic_algorithms(True, warn_only=True)
    return seed
