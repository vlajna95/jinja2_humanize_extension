from setuptools import setup, find_packages

# with open("README.md", "r", encoding="utf-8") as readme:
long_description = "" # readme.read()

setup(
	name = "jinja2_humanize_extension",
	version = "1.0.0",
	keywords = "markdown-extension humanize datetime formats",
	description = "Python Jinja2 extension to humanize datetime and other data",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	author = "Danijela Popović",
	author_email = "eternal.romania@gmail.com",
	python_requires = ">=3",
	url = "https://github.com/vlajna95/jinja2_humanize_extension",
	packages = find_packages(exclude=["test*"]),
	entry_point = {
		# "markdown.extensions": [
		"jinja2_humanize_extension = jinja2_humanize_extension:HumanizeExtension"
		# ]
	},
	install_requires = [
		"jinja2>=3",
	],
	license = "GNU General Public License v3.0",
	classifiers = [
		"Development Status :: 5 - Production/Stable",
		"Environment :: Console",
		"Intended Audience :: Developers",
		"Intended Audience :: Science/Research",
		"Intended Audience :: Other Audience",
		"License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.5",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: 3.10",
		"Programming Language :: Python :: 3.11",
		"Programming Language :: Python :: 3.12",
		"Programming Language :: Python :: 3.13",
		"Topic :: Internet :: WWW/HTTP :: Dynamic Content",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Topic :: Text Processing :: Filters",
		"Topic :: Text Processing :: Markup :: HTML",
	]
)