# -*- coding: utf-8 -*-
# Copyright (C) 2019 by Bill Schumacher
#
# Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby
# granted.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER
# IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.

import platform

from setuptools import setup

long_description = None

packages = [
    "pycflare",
]

requirements = ["requests"]
system_platform = platform.system()

these_requirements = []
for requirement in requirements:
    if not requirement.startswith('-e'):
        these_requirements.append(requirement)
setup_requirements = ['pytest-runner', ]
setup_requirements += these_requirements
test_requirements = ['pytest', ]
test_requirements += these_requirements

setup(
    name="pycflare",
    version="0.6",
    author="Bill Schumacher",
    author_email="williamschumacher@gmail.com",
    description="Python bindings for CloudFlare",
    license="BSD 0-Clause",
    keywords="cloudflare workers kv",
    url="https://github.com/BillSchumacher/pycflare.git",
    packages=packages,
    install_requires=these_requirements,
    scripts=[],
    setup_requires=setup_requirements,
    tests_require=test_requirements
)
