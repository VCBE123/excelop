from __future__ import print_function
from setuptools import setup, find_packages
import sys

setup(
    name="excelop",
    version="0.1.0",
    author="vcbe",  # 作者名字
    author_email="945193029@qq.com",
    description="simple Excel Operation",
    license="MIT",
    url="",  # github地址或其他地址
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Chinese',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Topic :: NLP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'openpyxl>=3.0.7'  # 所需要包的版本号
        'os'
    ],
    zip_safe=True,
)
