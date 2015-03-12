from distutils.core import setup
from setuptools.command.install import install
import urllib
import tarfile
import os

class CustomInstall(install):
    def run(self):
        install.run(self)
        print "Installing latest dynamodblocal"
        f, response = urllib.urlretrieve("http://dynamodb-local.s3-website-us-west-2.amazonaws.com/dynamodb_local_latest")
        bundle = tarfile.open(f)
        bundle.extractall(path=self.install_scripts)
        os.remove(f)
        print "extracted latest dynamodb local"

setup(
    name='dynamodblocal',
    version='0.3dev',
    packages=['dynamodblocal',],
    license='The MIT License (MIT)',
    long_description=open('README.txt').read(),
    cmdclass={'install' : CustomInstall },
    scripts=['scripts/dynamodblocal',]
)