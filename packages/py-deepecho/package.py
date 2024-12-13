# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDeepecho(PythonPackage):
    """DeepEcho is a Synthetic Data Generation Python library
    for mixed-type, multivariate time series."""

    homepage = "https://github.com/sdv-dev/DeepEcho"
    pypi = "deepecho/deepecho-0.6.1.tar.gz"

    version("0.6.1", sha256="e3b2bb876c810953595d1999277aa9c653b33e1cc97662292893aa4608c80d4a")

    depends_on("python@3.9:3.12", type=("build", "run"))
    depends_on("py-setuptools", type="build")