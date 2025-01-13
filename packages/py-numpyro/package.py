# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyNumpyro(PythonPackage):
    """Probabilistic programming powered by JAX for autograd and JIT compilation to GPU/TPU/CPU."""

    homepage = "https://num.pyro.ai"
    pypi = "numpyro/numpyro-0.15.3.tar.gz"
    git = "https://github.com/pyro-ppl/numpyro"

    # Versions
    version("0.15.3", sha256="f445eeae6200f883d790d65ce29ff245f7a9639bac3322d993eccf91c44023b3")


    with default_args(type="build"):
        depends_on("py-setuptools")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:")
        depends_on("py-jax@0.4.3:")
        depends_on("py-multipledispatch")
        depends_on("py-numpy")
        depends_on("py-tqdm")
