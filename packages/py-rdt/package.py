# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyRdt(PythonPackage):
    """RDT is a Python library used to transform data for data
    science libraries and preserve the transformations in order
    to revert them as needed."""

    homepage = "https://github.com/sdv-dev/RDT"
    pypi = "rdt/rdt-0.6.1.tar.gz"

    version("1.3.0", sha256="3e008acb734d894d7e7c21cdb77277ab70cabbbbd3342c082ec06ed6e8666f3c")
    version("0.6.1", sha256="ee2ac0d3479b254f99f35a709a24ffd5f2c899de6ea71f1ee844c6113febba71")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-numpy@1.20:1", type=("build", "run"))
    depends_on("py-pandas@1.1.3:1", type=("build", "run"))
    depends_on("py-scipy@1.5.4:1", type=("build", "run"))
    depends_on("py-psutil@5.7:5", type=("build", "run"))

    with when("@1.3.0:"):
        depends_on("py-scikit-learn@0.24:2", type=("build", "run"))
        depends_on("py-faker@10:", type=("build", "run"))