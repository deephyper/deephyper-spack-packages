# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFaker(PythonPackage):
    """Faker is a Python package that generates fake data for
    you. Whether you need to bootstrap your database, create
    good-looking XML documents, fill-in your persistence to
    stress test it, or anonymize data taken from a production
    service, Faker is for you."""

    homepage = "https://github.com/joke2k/faker"
    pypi = "Faker/Faker-9.8.2.tar.gz"

    version("16.6.1", sha256="b76e5d2405470e3d38d37d1bfaa9d9bbf171bdf41c814f5bbd8117b121f6bccb")
    version("16.6.0", sha256="dc8b2a8bf0d852d26eacf7763afd5e7d6e9e50d80ec648b51b8ecd3c505435fd")
    version("16.5.0", sha256="c62d25f3f78b76e839f27213d913e6463a971f71772bed384f0a18328a99d0ee")
    version("16.4.0", sha256="dcffdca8ec9a715982bcd5f53ee688dc4784cd112f9910f8f7183773eb3ec276")
    version("16.3.0", sha256="79354c15477e7ee41067cd75e033155ec9b669adbf7bbce8b66e54893cfee1e4")
    version("16.2.0", sha256="cc14622e15f528440e60e80eb891826a8a8583d490babf3c7d4c75cd59e06294")
    version("16.1.0", sha256="4a8bc3cec832dde1928f8ce0817452bdadf63863d9e4d8307817247a38e51523")
    version("16.0.1", sha256="533c2eff1e8331d41674ff7a35c466bd289a14e23fa0d714927e37b24bc9d610")
    version("16.0.0", sha256="10058e8ccf8a590bd25f4efa85be4fc541f198dcdeb4ca9a6d691d89a03808b4")
    version("15.3.4", sha256="2d5443724f640ce07658ca8ca8bbd40d26b58914e63eec6549727869aa67e2cc")
    version("15.3.3", sha256="20d090e661bbe88a5d801ea5eb3d853564940352120c84c9a14968847aca2893")
    version("15.3.2", sha256="0094fe3340ad73c490d3ffccc59cc171b161acfccccd52925c70970ba23e6d6b")
    version("15.3.1", sha256="b9dd2fd9a9ac68a4e0c5040cd9e9bfaa099fa8dd15bae5f01f224a45431818d5")
    version("15.3.0", sha256="a1ebb55b1787b1d02ddf70f8441f21a6ac535b61b50f19175f89f442b27678b2")
    version("15.2.0", sha256="f35b9b47fb84d7334645feba0dd87bbf5aba2b617cd83ec8e1b8c6dcd859a710")
    version("15.1.5", sha256="bea7ac1f2d5cc9f8a2a22b7b8acf604928398891ee2f4f110ab5423423f72e5f")
    version("15.1.4", sha256="040146b044dc83f65e6b04f97c685f60ea43dc0f60062cef9be05fc1b110c4b1")
    version("15.1.3", sha256="1bfb1b447cd45169a74a09f821cee47f51548508b62a29f6dfdab1d001d448a4")
    version("15.1.2", sha256="39c4e7915813923829675488cafef07ddf11cf59ecbaac518f53dd8e7b0df5cf")
    version("15.1.1", sha256="a741b77f484215c3aab2604100669657189548f440fcb2ed0f8b7ee21c385629")
    version("15.1.0", sha256="bc2634053fd1fd82edd78e6b9bdcdcee19a0d9501227b6e0fc531c7b00b0e805")
    version("15.0.0", sha256="245fc7d23470dc57164bd9a59b7b1126e16289ffcf813d88a6c8e9b8a37ea3fb")
    version("14.2.1", sha256="daad7badb4fd916bd047b28c8459ef4689e4fe6acf61f6dfebee8cc602e4d009")
    version("14.2.0", sha256="6db56e2c43a2b74250d1c332ef25fef7dc07dcb6c5fab5329dd7b4467b8ed7b9")
    version("14.1.2", sha256="461ba5240e17104b25d01e4eed58a59078f295b7e0257e28aca78540050f9037")
    version("14.1.1", sha256="2d506c09aeafa87296f834fd15c6efa87182320f8bf4f709bd3d882397c18076")
    version("14.1.0", sha256="0e00bfa1eadf1493f15662edb181222fea4847764cf3f9ff3e66ee0f95c9a644")
    version("14.0.0", sha256="0c7d283a96c49af64fe319f70d2b68927873c9173e922f8eda6001e7757cb63b")
    version("13.16.0", sha256="25c5be99bc5fd8676eea8c1490e0de87f6d9734651c7af2cefc99b322b2936f4")
    version("13.15.1", sha256="7c3f8ee807d3916415568169a172bf0893ea9cc3371ab55e4e5f5170d2185bea")
    version("9.8.2", sha256="393bd1b5becf3ccbc04a4f0f13da7e437914b24cafd1a4d8b71b5fecff54fb34")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-python-dateutil@2.4:", type=("build", "run"))
    depends_on("py-typing-extensions@3.10.0.2:", type=("build", "run"), when="^python@:3.8")

    with when("@:11"):
        depends_on("py-text-unidecode@1.3", type=("build", "run"))