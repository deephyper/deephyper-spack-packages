# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPlotly(PythonPackage):
    """An interactive, browser-based graphing library for Python"""

    homepage = "https://plot.ly/python/"
    pypi = "plotly/plotly-2.2.0.tar.gz"

    version("5.13.0", sha256="81a3aae4021d5ab91790fc71c3433791f41bfc71586e857f7777f429a955039a")
    version("5.12.0", sha256="8bf1b37a1e3cb260a4aa77ab79c9db4fd0ad3ccd66463c3a3e8a5300196ec61e")
    version("5.11.0", sha256="4efef479c2ec1d86dcdac8405b6ca70ca65649a77408e39a7e84a1ea2db6c787")
    version("5.10.0", sha256="4d36d9859b7a153b273562deeed8c292587a472eb1fd57cd4158ec89d9defadb")
    version("5.2.2", sha256="809f0674a7991daaf4f287964d617d24e9fa44463acd5a5352ebd874cfd98b07")
    version("2.2.0", sha256="ca668911ffb4d11fed6d7fbb12236f8ecc6a7209db192326bcb64bdb41451a58")

    depends_on("python@3.6:", when="@5.2.2:", type=("build", "run"))

    depends_on("py-setuptools", type="build")
    depends_on("py-six", type=("build", "run"))

    depends_on("py-pytz", when="@:2.2.0", type=("build", "run"))
    depends_on("py-decorator@4.0.6:", when="@:2.2.0", type=("build", "run"))
    depends_on("py-nbformat@4.2.0:", when="@:2.2.0", type=("build", "run"))
    depends_on("py-requests", when="@:2.2.0", type=("build", "run"))

    depends_on("py-tenacity@6.2.0:", when="@5.2.2:", type=("build", "run"))