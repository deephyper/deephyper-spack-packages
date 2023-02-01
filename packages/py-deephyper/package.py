# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyDeephyper(PythonPackage):
    """Scalable asynchronous neural architecture and hyperparameter
    search for deep neural networks."""

    homepage = "https://deephyper.readthedocs.io/"
    pypi = "deephyper/deephyper-0.4.2.tar.gz"
    git = "https://github.com/deephyper/deephyper.git"

    maintainers = ["mdorier", "Deathn0t"]

    # Versions
    version("master", branch="master")
    version("develop", branch="develop")
    version("0.4.2", sha256="ee1811a22b08eff3c9098f63fbbb37f7c8703e2f878f2bdf2ec35a978512867f")

    # Variants
    variant("dev", default=False, description="Build with dev dependencies")
    variant("nas", default=False, description="Build with Neural Architecture Search dependencies")
    variant("autodeuq", default=False, description="Build with Automated Deep Ensemble dependencies")
    variant("hps-tl", default=False, description="Build with Hyperparameter Tuning with Transfer Learning dependencies")
    variant("mpi", default=False, description="Build with MPI dependencies")
    variant("ray", default=False, description="Build with Ray dependencies")
    variant("redis", default=False, description="Build with Redis dependencies")

    # Dependencies
    depends_on("python@3.7:", type=("build", "run"))
    
    # "py-wheel" is already a depdenency of PythonPackage class
    depends_on("py-setuptools@42:", type="build") 
    depends_on("py-cython@0.29.24", type="build")

    depends_on("py-configspace@0.4.20:", type=("build", "run"))
    depends_on("py-dm-tree", type=("build", "run"))
    depends_on("py-jinja2@:3.0", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas@0.24.2:", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))
    depends_on("py-parse", type=("build", "run"))
    depends_on("py-scikit-learn@0.23.1:", type=("build", "run"))
    depends_on("py-scipy@1.7:", type=("build", "run"))
    depends_on("py-tqdm@4.64.0:", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-tinydb", type=("build", "run"))
    depends_on("py-jax@0.3:", type=("build", "run"))
    depends_on("py-numpyro@0.10:", type=("build", "run"))

    depends_on("py-mpi4py", type=("build", "run"), when="+mpi")
    depends_on("py-ray", type=("build", "run"), when="+ray")

    depends_on("py-redis", type=("build", "run"), when="+redis")
    depends_on("redisjson", type=("build", "run"), when="+redis")

    # "ConfigSpace>=0.4.20",
    # "dm-tree",
    #! "jax[cpu]>=0.3.25", 
    # "Jinja2<3.1",
    # "numpy",  # ==1.19.4",  # working with 1.20.1
    #! "numpyro[cpu]",
    # "pandas>=0.24.2",
    # "packaging",
    # "scikit-learn>=0.23.1",
    # "scipy>=0.19.1",
    # "tqdm>=4.64.0",
    # "pyyaml",
    # "tinydb",

    # if "+dev" in self.spec:
        # pass