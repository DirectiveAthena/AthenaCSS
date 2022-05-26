# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import setuptools

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
setuptools.setup(
    name="AthenaCSS",
    version="0.3.0",
    author="Andreas Sas",
    author_email="",
    description="",
    url="https://github.com/DirectiveAthena/VerSC-AthenaCSS",
    project_urls={
        "Bug Tracker": "https://github.com/DirectiveAthena/VerSC-AthenaCSS/issues",
    },
    license="GPLv3",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.10",
    install_requires=["AthenaColor>=4.2.0", "AthenaLib>=0.2.0"]
)