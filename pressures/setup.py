from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pressures',
    version='0.1.0',
    description='Make blood pressure reports.',
    long_description=readme,
    author="Jack O'Quin",
    author_email='jack.oquin@gmail.com',
    url='https://github.com/jack-oquin/python_tools',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
