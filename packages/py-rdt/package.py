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
    pypi = "rdt/rdt-1.13.1.tar.gz"

    version("1.13.1", sha256="fef2488058b65eb6a65d4e49ad81e02435cebbdcf3d9c8624af8e57ce53710a6")

    with default_args(type="build"):
        depends_on("py-setuptools")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:")
        depends_on("py-numpy")
        depends_on("py-pandas")
        depends_on("py-scipy")
        depends_on("py-scikit-learn")
        depends_on("py-faker@33.0.0:")