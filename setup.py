from pathlib import Path

from setuptools import find_packages, setup

from comel import __version__ as version

PROJECT_NAME = "Comel"
PROJECT_ROOT = Path(__file__).parent
REQUIREMENTS = [
    "darkdetect",
    "PySide6",
]
EXCLUDE_FOLDERS = [
    "docs",
    "examples",
    "qss",
    "tests",
]

with open(str(PROJECT_ROOT / "README.md"), "r") as readme:
    README = readme.read()

setup(
    name=PROJECT_NAME,
    version=version,
    url="https://github.com/hueyyeng/Comel",
    author="Huey Yeng",
    author_email="huey.yeng.mmu@gmail.com",
    maintainer="Huey Yeng",
    maintainer_email="huey.yeng.mmu@gmail.com",
    description="Opinionated PySide6 Light/Dark Theme Toggler.",
    long_description_content_type="text/markdown",
    long_description=README,
    packages=find_packages(where=str(PROJECT_ROOT), exclude=EXCLUDE_FOLDERS),
    install_requires=REQUIREMENTS,
    python_requires=">=3.7",
    keywords=[
        "python",
        "library",
        "qt",
        "widgets",
        "development"
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Windows :: Windows 10",
    ]
)
