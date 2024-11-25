# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCopulas(PythonPackage):
    """Copulas is a Python library for modeling multivariate
    distributions and sampling from them using copula
    functions. Given a table containing numerical data, we can
    use Copulas to learn the distribution and later on generate
    new synthetic rows following the same statistical
    properties."""

    homepage = "https://github.com/sdv-dev/Copulas"
    pypi = "copulas/copulas-0.12.0.tar.gz"
    version("0.12.0", sha256="ff49a6226db9a56657cdbffb12cface9065e5b6f50cdc1e950115fa8180580f3")

    depends_on("python@3.9:3.12", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))