from distutils.core import setup

setup(
    name='XboxLeadersAPI',
    version='0.1',
    author="Adam Parkin",
    author_email="pzelnip@gmail.com",
    url="https://github.com/pzelnip/XboxLeadersAPI",
    description="A simple Python wrapper for the XboxLeaders.com Xbox API (http://www.xboxleaders.com/docs/api)",
    packages=['xboxleaders',],
    license='BSD',
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords=['xbox xbox360 xboxleaders'],
)
