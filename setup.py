from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erp_shoppingcart/__init__.py
from erp_shoppingcart import __version__ as version

setup(
	name="erp_shoppingcart",
	version=version,
	description="shopping cart",
	author="biswajit@buzztagmedia.com",
	author_email="biswajit@buzztagmedia.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
