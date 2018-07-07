from setuptools import setup, find_packages
import os
import pyautoit3

with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as fp:
    long_description = fp.read()

setup(
    name='PyAutoit3',
    version=pyautoit3.__version__,
    url='https://github.com/EcmaXp/PyAutoit3',
    author='EcmaXp',
    author_email='package-pyautoit3@ecmaxp.pe.kr',
    description='AutoItX3 for Python3',
    long_description=long_description,
    python_requires='>=3.6',
    platforms=[
        'win32',
    ],
    setup_requires=[
        "wheel",
    ],
    packages=find_packages(),
    package_data={
        'pyautoit3': [
            'dll/library/AutoitX3_DLL.h',
            'dll/library/AutoitX3*.dll',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: Quality Assurance',
    ],
    keywords='autoit',
)
