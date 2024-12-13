# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCtgan(PythonPackage):
    """CTGAN is a collection of Deep Learning based Synthetic
    Data Generators for single table data, which are able to
    learn from real data and generate synthetic clones with
    high fidelity."""

    homepage = "https://github.com/sdv-dev/CTGAN"
    pypi = "ctgan/ctgan-0.10.2.tar.gz"

    version("0.10.2", sha256="e696fcb52c1591e589498eb42ff3d465bfd9052dadb75ee0eef85993ee0d358e")

    depends_on("python@3.9:3.12", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-rdt@1.13.0:1", type=("build", "run"))