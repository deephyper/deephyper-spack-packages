# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyNumpyro(PythonPackage):
    """Probabilistic programming powered by JAX for autograd and JIT compilation to GPU/TPU/CPU."""

    homepage = "https://num.pyro.ai"
    pypi = "numpyro/numpyro-0.10.1.tar.gz"
    git = "https://github.com/pyro-ppl/numpyro"

    # Versions
    version("0.10.1", sha256="dfa896f01c8df43ddd41663af2b3e2fc4aea73489e669474e83329b183b29150")

    # Variants
    variant("cuda", default=False, description="CUDA support")

    # Dependencies
    depends_on("python@3.7:", type=("build", "run"))

    depends_on("py-setuptools", type="build")

    depends_on("py-jax@0.2.13:~cuda", type=("build", "run"), when="~cuda")
    depends_on("py-jax@0.2.13:+cuda", type=("build", "run"), when="+cuda")
    # depends_on("py-jaxlib@0.1.65:~cuda", type=("build", "run"), when="~cuda")
    depends_on("py-multipledispatch", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))