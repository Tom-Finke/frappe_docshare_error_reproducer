from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_docshare_error_reproducer/__init__.py
from frappe_docshare_error_reproducer import __version__ as version

setup(
	name="frappe_docshare_error_reproducer",
	version=version,
	description="App to formalize https://github.com/frappe/frappe/issues/17017",
	author="Tom Finke",
	author_email="tom.s.h.finke@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
