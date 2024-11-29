# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTensorflowProbability(PythonPackage):
    """RDT is a Python library used to transform data for data
    science libraries and preserve the transformations in order
    to revert them as needed."""

    homepage = "https://github.com/tensorflow/probability"
    pypi = "tensorflow-probability/tensorflow_probability-0.24.0-py2.py3-none-any.whl"

    version("0.24.0", sha256="8c1774683e38359dbcaf3697e79b7e6a4e69b9c7b3679e78ee18f43e59e5759b")

    depends_on("python@3.9:3.12", type=("build", "run"))
    depends_on("py-setuptools", type="build")