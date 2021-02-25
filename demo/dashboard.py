from setuptools import find_packages
from setuptools import setup

setup(
    name="backend",
    version="1.0.0",
    description="Test",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask", "python_version>3.4", "requests", "urllib3"],
)
