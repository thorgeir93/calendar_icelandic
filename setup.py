#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='cal_is',
    version='0.1.0',
    description=(
        'Simple terminal calender with '
        'Icelandic words and holidays.'
    ),
    author='Þorgeir Sigurðsson',
    author_email='thorgeirsigurd@gmail.com',
    packages=['cal_is'],
    install_requires=['workalendar', 'calendar']
)
