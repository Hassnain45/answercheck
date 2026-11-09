"""Report what machine and package versions we are running on.

We print this at the start of every Colab session, so that results can later be
matched to the exact software that produced them.
"""

import platform
import sys
from importlib import metadata

# The main packages from requirements.txt that we want to see versions for.
KEY_PACKAGES = [
    "torch",
    "transformers",
    "datasets",
    "scikit-learn",
    "numpy",
    "pandas",
    "pyyaml",
    "gradio",
    "pytest",
    "tensorboard",
]


def package_versions() -> dict:
    """Return {package name: installed version}, or 'not installed'."""
    versions = {}
    for name in KEY_PACKAGES:
        try:
            versions[name] = metadata.version(name)
        except metadata.PackageNotFoundError:
            versions[name] = "not installed"
    return versions


def gpu_info() -> dict:
    """Return basic GPU facts. On a machine without a GPU, 'available' is False."""
    import torch

    info = {"available": torch.cuda.is_available()}
    if info["available"]:
        props = torch.cuda.get_device_properties(0)
        info["name"] = props.name
        info["memory_gb"] = round(props.total_memory / 1024**3, 1)
        info["cuda_version"] = torch.version.cuda
    return info


def environment_report() -> dict:
    """Collect Python, platform, package and GPU information in one dictionary."""
    from answercheck import __version__

    return {
        "answercheck": __version__,
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "packages": package_versions(),
        "gpu": gpu_info(),
    }


def print_environment_report() -> dict:
    """Print the environment report in a readable way and also return it."""
    report = environment_report()
    print(f"answercheck  {report['answercheck']}")
    print(f"python       {report['python']}")
    print(f"platform     {report['platform']}")
    print("packages:")
    for name, version in report["packages"].items():
        print(f"  {name:<14}{version}")
    gpu = report["gpu"]
    if gpu["available"]:
        print(f"GPU: {gpu['name']} ({gpu['memory_gb']} GB, CUDA {gpu['cuda_version']})")
    else:
        print("GPU: none found (on Colab: Runtime > Change runtime type > T4 GPU)")
    return report
