from setuptools import setup, find_packages
import os

version = __import__('multimedia').__version__

install_requires = [
    'setuptools',
    'django-celery',
    'django-filer',
    'paramiko',
    'pycrypto',
]

setup(
    name = "django-multimedia",
    version = version,
    url = 'http://github.com/salvaorenick/django-multimedia',
    license = 'BSD',
    platforms=['OS Independent'],
    description = "",
    author = "Andrew Schoen",
    author_email = 'andrew.schoen@gmail.com',
    packages=find_packages(),
    install_requires = install_requires,
    include_package_data=True,
    zip_safe=False,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Multimedia :: Video',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Video :: Conversion',
    ],
    package_dir={
        'multimedia': 'multimedia',
    },
)