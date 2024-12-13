# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyDeephyper(PythonPackage):
    """Scalable asynchronous hyperparameter optimization, neural architecture search,
    and parallel ensemble of predictive models."""

    homepage = "https://deephyper.readthedocs.io/"
    pypi = "deephyper/deephyper-0.8.1.tar.gz"
    git = "https://github.com/deephyper/deephyper.git"

    maintainers("mdorier", "Deathn0t")

    # Versions
    version("master", branch="master")
    version("develop", branch="develop")
    version(
        "0.8.1",
        sha256="ac27edd62ff81fcfb9b0b49f44963dadd8338be687f8f616d4cbdd6f5c68e511",
    )

    # Variants
    variant(
        "hpo-tl",
        default=False,
        description="Build with Hyperparameter Tuning with Transfer Learning dependencies",
    )
    variant("jax-cpu", default=False, description="Build with JAX dependencies")
    # variant("jax-gpu", default=False, description="Build with JAX dependencies + GPU")
    variant(
        "tf-keras2",
        default=False,
        description="Build with TensorFlow and Keras2 dependencies",
    )
    variant("torch", default=False, description="Build with PyTorch dependencies")

    """
    variant("mpi", default=False, description="Build with MPI dependencies")
    variant("ray", default=False, description="Build with Ray dependencies")
    variant("redis", default=False, description="Build with Redis dependencies")
    variant("dev", default=False, description="Build with dev dependencies")
    """

    # Build backend
    with default_args(type=("build")):
        depends_on("py-hatchling@1.25:", when="@master")
        depends_on("py-hatchling@1.25:", when="@develop")
        depends_on("py-hatchling@1.25:", when="@0.9:")
        depends_on("py-setuptools@42:", when="@0.8:")
        depends_on("py-cython@0.29.24:", when="@0.8:")

    # Python versions
    with default_args(type=("build", "run")):

        depends_on("python@3.10:", when="@0.9:")
        depends_on("python@3.9:", when="@0.8:")

    # Dependencies from setup/toml files
    with default_args(type=("build", "run")):

        depends_on("py-configspace@1.1.1:", when="@0.8:")
        depends_on("py-dm-tree", when="@0.8:")
        depends_on("py-jinja2@3.1.4:", when="@0.8:")
        depends_on("py-matplotlib", when="@0.8:")
        depends_on("py-numpy@1.26.0:", when="@0.8:")
        depends_on("py-pandas@0.24.2:", when="@0.8:")
        depends_on("py-packaging", when="@0.8:")
        depends_on("py-parse", when="@0.8:")
        depends_on("py-scikit-learn@0.23.1:", when="@0.8:")
        depends_on("py-scipy@1.10:", when="@0.8:")
        depends_on("py-tqdm@4.64.0:", when="@0.8:")
        depends_on("py-psutil", when="@0.8:")
        depends_on("py-pymoo@0.6:", when="@0.8:")
        depends_on("py-pyyaml", when="@0.8:")

    with when("+dev"), default_args(type=("build", "run")):
        depends_on("py-pytest")

    with when("+hpo-tl"), default_args(type=("build", "run")):
        depends_on("py-sdv@1.15", when="@0.8:")

    with when("+jax-cpu"), default_args(type=("build", "run")):
        depends_on("py-jax@0.4.3:", when="@0.8:")
        depends_on("py-numpyro@0.15.3:", when="@0.8:")

    with when("+tf-keras2"), default_args(type=("build", "run")):
        depends_on("py-tf-keras@2.17:", when="@0.8:")
        depends_on("py-tensorflow@2.17:", when="@0.8:")
        depends_on("py-tensorflow-probability@0.24.0:", when="0.8:")

    #     depends_on("py-keras@3.6.0:", type=("build", "run"))
    #     depends_on("openssl@3.4.0:", type=("build", "run"))
    #     depends_on("py-decorator@5.1.1:", type=("build", "run"))
    #     depends_on("py-cloudpickle@3.0.0:3", type=("build", "run"))

    # with when("+torch"):
    #     depends_on("py-torch@2.5.1:2.5", type=("build", "run"))

    # with when ("+jax-gpu"):
    #     depends_on("py-jax@0.4.3:", type=("build", "run"))
    #     depends_on("py-numpyro@0.15.3:", type=("build", "run"))

    # depends_on("py-mpi4py", type=("build", "run"), when="+mpi")
    # depends_on("py-ray", type=("build", "run"), when="+ray")

    # with when("+redis"):
    #     depends_on("py-redis", type=("build", "run"))
    #     depends_on("redisjson", type=("build", "run"))
