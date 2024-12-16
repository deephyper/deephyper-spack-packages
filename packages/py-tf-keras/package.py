# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTfKeras(PythonPackage):
    """TensorFlow is an open source machine learning framework for everyone."""

    homepage = "https://github.com/keras-team/tf-keras"
    pypi = "tf-keras/tf_keras-2.17.0.tar.gz"

    version("2.18.0", sha256="ebf744519b322afead33086a2aba872245473294affd40973694f3eb7c7ad77d")
    version("2.17.0", sha256="fda97c18da30da0f72a5a7e80f3eee343b09f4c206dad6c57c944fb2cd18560e")
    version("2.16.0", sha256="db53891f1ac98197c2acced98cdca8c06ba8255655a6cb7eb95ed49676118280")
    version("2.15.1", sha256="40ab605cecc7759c657cb2bccd9efaacd6fc2369a6c1eba8053890afeac46886")
    version("2.15.0", sha256="d7559c2ba40667679fcb2105d3e4b68bbc07ecafbf1037462ce7b3974c3c6798")

    with default_args(type="build"):
        depends_on("py-setuptools")
    
    with default_args(type=("build", "run")):
        depends_on("python@3.9:3.12", when="@2.16:")
        depends_on("python@3.9:3.11", when="@2.15:")
