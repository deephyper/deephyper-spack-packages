# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTfKeras(PythonPackage):
    """RDT is a Python library used to transform data for data
    science libraries and preserve the transformations in order
    to revert them as needed."""

    homepage = "https://github.com/keras-team/tf-keras"
    pypi = "tf-keras/tf_keras-2.17.0.tar.gz"

    version("2.17.0", sha256="fda97c18da30da0f72a5a7e80f3eee343b09f4c206dad6c57c944fb2cd18560e")

    depends_on("python@3.9:3.12", type=("build", "run"))
    depends_on("py-setuptools", type="build")