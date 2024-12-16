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

    with default_args(type="build"):
        depends_on("py-setuptools", when="@1:")
        depends_on("py-setuptools@:59", when="@0.14:")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:", when="@1:")
        depends_on("python@3.6:", when="@0.14:")

    with when("@1.17:"), default_args(type=("build", "run")):
        depends_on("py-cloudpickle@2.1:")
        depends_on("py-copulas@0.12:") 
        depends_on("py-ctgan@0.10.2") 
        depends_on("py-deepecho@0.6.1:")
        depends_on("py-faker@10:14")
        depends_on("py-graphviz@0.13.2:")
        depends_on("py-numpy@1.23.3:")
        depends_on("py-pandas@1.5.0:")
        depends_on("py-pyyaml@6.0.1:")
        depends_on("py-rdt@1.13.1:") 
        depends_on("py-sdmetrics@0.17:") 
        depends_on("py-tqdm@4.29:")

    with when("@1:"), default_args(type=("build", "run")):
        depends_on("py-cloudpickle@2.1:")
        depends_on("py-copulas@0.8") 
        depends_on("py-ctgan@0.7") 
        depends_on("py-deepecho@0.4")
        depends_on("py-faker@10:14")
        depends_on("py-graphviz@0.13.2:")
        depends_on("py-numpy@1.23.3:")
        depends_on("py-pandas@1.5.0:")
        depends_on("py-rdt@1.3:1") 
        depends_on("py-sdmetrics@0.9") 
        depends_on("py-tqdm@4.15:")

    with when("@0.18:"), default_args(type=("build", "run")):
        depends_on("py-faker@10:14")
        depends_on("py-graphviz@0.13.2:0")
        depends_on("py-numpy@1.20:1")
        depends_on("py-pandas@1.1.3:1")
        depends_on("py-tqdm@4.15:4")
        depends_on("py-copulas@0.8.0:0.8")
        depends_on("py-ctgan@0.7.0:0.7")
        depends_on("py-deepecho@0.4.0:0.4")
        depends_on("py-rdt@1.3.0:1")
        depends_on("py-sdmetrics@0.9")
        depends_on("py-cloudpickle@2.1:2")

    with when("@0.14:"), default_args(type=("build", "run")):
        depends_on("py-faker@3.0.0:9")
        depends_on("py-graphviz@0.13.2:0")
        depends_on("py-numpy@1.20:1")
        depends_on("py-pandas@1.1.3:1.1.4")
        depends_on("py-tqdm@4.15:4")
        depends_on("py-copulas@0.6.0:0.6")
        depends_on("py-ctgan@0.5.0:0.5")
        depends_on("py-deepecho@0.3.0.post1:0.3")
        depends_on("py-rdt@0.6.1:0.6")
        depends_on("py-sdmetrics@0.4.1:0.4")