# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDeepecho(PythonPackage):
    """DeepEcho is a Synthetic Data Generation Python library
    for mixed-type, multivariate time series."""

    homepage = "https://github.com/sdv-dev/DeepEcho"
    pypi = "deepecho/deepecho-0.3.0.post1.tar.gz"

    version("0.4.0", sha256="c49baee281691f220b880b17fe095134c797dfb90bdb2b2d8b783da69386b51c")
    version("0.3.0", sha256="c202c8e140ca13c41f5e66d6c03217bce9ad63ebe06c3f9569a2e90bb4045a6f")
    version("0.2.1", sha256="564113deefe9b9f3b678b956342bc559711e39b1ff975c494c1bbbc8b10f0fe8")
    version("0.2.0", sha256="377ee06c21ff795c3fc87178e6fce018baf9b0705da0d12e76e548d787658251")
    version(
        "0.3.0.post1", sha256="9f67373a435b5bcd84441c53eae87a2ba17a27574419a59191f92198f400b914"
    )

    depends_on("python@3.6:3.9", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-pytest-runner@2.11.1:", type="build")
    depends_on("py-numpy@1.20.0:1", type=("build", "run"))
    depends_on("py-pandas@1.1.3:1", type=("build", "run"))
    depends_on("py-torch@1.8.0:1", type=("build", "run"))
    depends_on("py-tqdm@4.15:4", type=("build", "run"))