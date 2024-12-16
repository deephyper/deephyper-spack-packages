# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySdmetrics(PythonPackage):
    """The SDMetrics library provides a set of dataset-agnostic
    tools for evaluating the quality of a synthetic database
    by comparing it to the real database that it is modeled
    after."""

    maintainers = ["Kerilk", "jke513"]

    homepage = "https://github.com/sdv-dev/SDMetrics"
    pypi = "sdmetrics/sdmetrics-0.17.0.tar.gz"

    version("0.17.0", sha256="8e6d48ca1721b77f153e6fb4110cb2a14948f9e760fc88779a32c2c976e857e3")

    with default_args(type="build"):
        depends_on("py-setuptools", type="build")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:")
        depends_on("py-numpy")
        depends_on("py-pandas")
        depends_on("py-scikit-learn")
        depends_on("py-scipy")
        depends_on("py-copulas@0.12.0")
        depends_on("py-tqdm")
        depends_on("py-plotly@5.20.0")

    