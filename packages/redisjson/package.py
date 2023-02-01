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
        redis-server --module $REDISJSON_MODULE_PATH

    """

    homepage = "http://redisjson.io"
    url = "https://github.com/RedisJSON/RedisJSON/archive/refs/tags/v2.4.3.tar.gz"

    version("2.4.3", sha256="8d2919d25b6b6a8730ae55976058ad3d2a62e608d98cb2cc420b142a8c4c9884")

    depends_on("rust")
    depends_on("redis")

    def build(self, spec, prefix):
        cargo = which("cargo")
        cargo("build", "--release")

    def install(self, spec, prefix):
        mkdir(prefix.lib)
        install_tree("target/release", prefix.lib)

        ext = "dylib" if self.spec.satisfies("platform=darwin") else "so"
        target = join_path(prefix.lib, f"librejson.{ext}")
        with open(join_path(prefix, "redis.conf"), "w") as f:
            f.write(f"loadmodule {target}")

    def setup_run_environment(self, env):
        ext = "dylib" if self.spec.satisfies("platform=darwin") else "so"
        target = join_path(prefix.lib, f"librejson.{ext}")
        env.set("REDISJSON_MODULE_PATH", target)
        