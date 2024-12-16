# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySdv(PythonPackage):
    """The Synthetic Data Vault (SDV) is a Synthetic Data
    Generation ecosystem of libraries that allows users to
    easily learn single-table, multi-table and timeseries
    datasets to later on generate new Synthetic Data that
    has the same format and statistical properties as the
    original dataset."""

    maintainers = ["Kerilk", "jke513"]

    homepage = "https://github.com/sdv-dev/SDV"
    pypi = "sdv/sdv-1.15.0.tar.gz"

    version("1.15.0", sha256="61cde74dcf097e2324cefdb8e66f2f5bf2331c416d149694897c06add0213932")

    depends_on("python@3.9:3.13", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    with when("@:1.15.0"):
        depends_on("py-copulas@0.12.0:0.12", type=("build", "run")) #* update spack package
        depends_on("py-ctgan@0.10.2:0.10", type=("build", "run")) #* update spack package
        depends_on("py-deepecho@0.6.1:0.6", type=("build", "run")) #* update spack package
        depends_on("py-rdt@1.13.1:1", type=("build", "run")) #* update spack package
        depends_on("py-sdmetrics@0.17.0", type=("build", "run")) #* update spack package