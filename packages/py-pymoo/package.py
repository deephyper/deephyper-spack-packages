# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPymoo(PythonPackage):
    """RDT is a Python library used to transform data for data
    science libraries and preserve the transformations in order
    to revert them as needed."""

    homepage = "https://github.com/anyoptimization/pymoo"
    pypi = "pymoo/pymoo-0.6.1.3.tar.gz"

    version("0.6.1.3", sha256="ab440986cbaede547125ca9d1545781fdee94b719488de44119a86b8e9af526e")

    depends_on("python@3.9:3.12", type=("build", "run"))
    depends_on("py-setuptools", type="build")