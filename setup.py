from distutils.core import setup

setup(
    name='XboxLeadersAPI',
    version='1.0',
    author="Adam Parkin",
    author_email="pzelnip@gmail.com",
    url="https://github.com/pzelnip/XboxLeadersAPI",
    description="A simple Python wrapper for the XboxLeaders.com Xbox API (http://www.xboxleaders.com/docs/api)",
    packages=['xboxleaders',],
    license='FreeBSD',
    long_description=open('README').read(),
)