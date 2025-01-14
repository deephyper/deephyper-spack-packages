# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFaker(PythonPackage):
    """Faker is a Python package that generates fake data for
    you. Whether you need to bootstrap your database, create
    good-looking XML documents, fill-in your persistence to
    stress test it, or anonymize data taken from a production
    service, Faker is for you."""

    homepage = "https://github.com/joke2k/faker"
    pypi = "Faker/faker-33.0.0.tar.gz"
    version("33.0.0", sha256="9b01019c1ddaf2253ca2308c0472116e993f4ad8fc9905f82fa965e0c6f932e9")

    with default_args(type="build"):
        depends_on("py-setuptools")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:")
        depends_on("py-python-dateutil@2.8.2:")
        depends_on("py-typing-extensions@4.12.2:", when="^python@:3.8")
        depends_on("py-text-unidecode@1.3", when="@:11")
