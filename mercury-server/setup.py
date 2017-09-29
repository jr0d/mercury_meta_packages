from setuptools import setup


setup(
    name='mercury-server',
    packages=['mercury_server']
    version='0.0.2',
    url='http://www.mercurysoft.io',
    license='Apache-2.0',
    author='Jared Rodriguez',
    author_email='jared@mercurysoft.io',
    description='Mercury meta-package for server components',
    install_requires=['mercury-common', 'mercury-inventory', 'mercury-rpc', 'mercury-log'],
    entry_points="""
[console_scripts]
hg_server = mercury_server.cli:main
"""
)

