import pathlib
import re

from setuptools import find_packages, setup


DIST_PKG_NAME = "realfakepg"
CORE_PKG_NAME = DIST_PKG_NAME
SRC_DIR = "src"

PACKAGES = find_packages(where=SRC_DIR)
META_PATH = pathlib.Path(SRC_DIR) / CORE_PKG_NAME / "__init__.py"

KEYWORDS = ["postgres"]
PROJECT_URLS = {
    "Source Code": "https://github.com/nicktimko/realfakepg",
}
CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: Implementation :: CPython",
    "Topic :: Software Development :: Libraries :: Python Modules",
]
INSTALL_REQUIRES = []
EXTRAS_REQUIRE = {
    "docs": [
        "sphinx",
    ],
    "tests": [
        "pytest>=6",
        # psutil extra is needed for correct core count detection.
        "pytest-xdist[psutil]",
    ],
    "cov": [
        f"{DIST_PKG_NAME}[tests]",
        "coverage-enable-subprocess",
        "coverage[toml]>=5.3",
    ],
    "dev": [f"{DIST_PKG_NAME}[tests,cov]"],
}

HERE = pathlib.Path(__file__).parent.resolve()


def read(*other):
    """
    Get the UTF-8 contents of the path specified by 'other' parts,
    relative to the repo root.
    """
    with HERE.joinpath(*other).open(mode="r", encoding="utf-8") as f:
        return f.read()


META_FILE = read(META_PATH)


def find_meta(meta):
    """
    Extract __*meta*__ from META_FILE.
    """
    meta_match = re.search(
        rf"^__{meta}__ = ['\"]([^'\"]*)['\"]", META_FILE, re.MULTILINE
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError(f"Unable to find __{meta}__ string.")


DESCRIPTION_FILE = "README.md"
DESCRIPTION_TYPE = {
    "txt": "text/plain",
    "md": "text/markdown",
    "rst": "text/x-rst",
}.get(DESCRIPTION_FILE.rsplit(".")[-1], "txt")
DESCRIPTION = read(DESCRIPTION_FILE)


if __name__ == "__main__":
    setup(
        name=DIST_PKG_NAME,
        description=find_meta("description"),
        license=find_meta("license"),
        url=find_meta("url"),
        project_urls=PROJECT_URLS,
        version=find_meta("version"),
        author=find_meta("author"),
        author_email=find_meta("email"),
        maintainer=find_meta("author"),
        maintainer_email=find_meta("email"),
        keywords=KEYWORDS,
        long_description=DESCRIPTION,
        long_description_content_type=DESCRIPTION_TYPE,
        packages=PACKAGES,
        package_dir={"": SRC_DIR},
        python_requires=">=3.7",
        zip_safe=False,
        classifiers=CLASSIFIERS,
        install_requires=INSTALL_REQUIRES,
        extras_require=EXTRAS_REQUIRE,
        include_package_data=True,
    )
