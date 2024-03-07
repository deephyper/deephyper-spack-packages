# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Redisjson(Package):
    """A JSON extension for Redis

    To start the redis server with the RediSJSON module:
    
    .. code-block:: console

        redis-server $(spack find --path redisjson | grep  -o "/.*/redisjson.*")/redis.conf

    """

    homepage = "http://redisjson.io"
    url = "https://github.com/RedisJSON/RedisJSON/archive/refs/tags/v2.4.3.tar.gz"

    version("2.6.9", sha256="c2fe3dc6dfc53e5e32eeb6e6672b30f0740a80c4cbc2e984897aa45ef3735753")
    version("2.6.8", sha256="3f3cdf984ab7ecdd9c2c05cb61f9103a4876dce7d24e4608808e204a309b38d0")
    version("2.6.7", sha256="5ef34b542b9a42d7e774322763f3f5e00591e35e7cacf741aadd682801c785cd")
    version("2.6.6", sha256="dae540857508fc7337e2822576b490f6169c2fa0a8abcee8c0bf16d4fe76d1b6")
    version("2.6.4", sha256="52a22ea8c28c43ac981ee7935f0f5c9cd3b00aa9e58309dfed0d3ae854d3ec06")
    version("2.6.3", sha256="7ad8341d24b67e35e0c544f72f8c4201eceee423404a4e677bd2c28222f3c490")
    version("2.6.2", sha256="6774e516878d03c0b66b9b25f2ecb6109d0666b8877ef4ab20cece0c9ff7ddec")
    version("2.6.1", sha256="7bb1094bf160112719396786d9c8602d1e03c652234e73e32185463efe9e5e76")
    version("2.6.0", sha256="908455294a1bd7b7740cb526c453c9354fad2463b0d971ed1e9f91bf821a3267")
    version("2.4.8", sha256="478d0165ed98984aee544a5faf1576062b94da611da2c1c728ebe54cf8f9b378")
    version("2.4.3", sha256="8d2919d25b6b6a8730ae55976058ad3d2a62e608d98cb2cc420b142a8c4c9884")

    depends_on("rust")
    depends_on("redis")

    def setup_build_environment(self, env):
        env.set("CARGO_HOME", self.stage.source_path)

    def install(self, spec, prefix):
        cargo = which("cargo")
        cargo("build", "--release")

        mkdir(prefix.lib)
        install_tree(
            join_path(
                self.stage.source_path, 
                "target", 
                "release"
            ), 
            prefix.lib
        )

        ext = "dylib" if self.spec.satisfies("platform=darwin") else "so"
        target = join_path(prefix.lib, f"librejson.{ext}")
        with open(join_path(prefix, "redis.conf"), "w") as f:
            f.write(f"loadmodule {target}")
