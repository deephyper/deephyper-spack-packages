# DeepHyper Spack Packages

## Overview

This repository contains a collection of [Spack](https://spack.io) packages to manage the building of DeepHyper from source. Start by installing Spack on your system:

```bash
git clone -c feature.manyFiles=true https://github.com/spack/spack.git
. ./spack/share/spack/setup-env.sh 
```

Spack is quite recent and evolving quickly. Many packages are regularly updated. Therefore it can sometimes be useful to checkout the `develop` branch of Spack (`git checkout develop`) in case of issue to see if a fix has already been provided but not yet released.

Now should have access to the `spack` command. If you need spack to be loaded for any new session of your shell then you can add `. $PATH_TO_SPACK/spack/share/spack/setup-env.sh` to your `~/.bashrc` (or any other shell configuration). Once Spack is installed and loaded. Download the DeepHyper Spack packages and add them to your Spack installer:


```bash
git clone https://github.com/deephyper/deephyper-spack-packages.git
spack repo add deephyper-spack-packages
```

After adding the `deephyper-spack-packages` to your Spack installer, create a Spack environment for deephyper:

```bash
spack env create deephyper
spack env activate deephyper
```

You are now ready to install DeepHyper. DeepHyper provides different set of features which not necessary for all users. By default, DeepHyper's installation only brings the basic hyperparameter optimization algorithm with Bayesian optimization and allow parallelism with a centralized scheme (1-manager, n-workers) through basic multi-thread or multi-processing pools.

```
spack add py-deephyper
spack install
```

Other features can be installed with the following variants:

```bash
spack add deephyper +mpi # MPI support for MPICommEvaluator
spack add deephyper +ray # Ray support for RayEvaluator
spack add deephyper +redis # Redis/RedisJSON/py-redis support for RedisStorage and Distributed Search
spack add deephyper +hps-tl # SDV support for transfer-learning with Bayesian Optimization
spack add deephyper +nas # Tensorflow support for Neural Architecture Search
spack add deephyper +autodeuq # Tensorflow/Tensorflow-Probability/Ray support for Deep Ensemble with Uncertainty Quantitification

# All Features at Once
spack add py-deephyper +autodeuq+hps-tl+mpi+nas+redis
```

For versions and branches of DeepHyper it is possible to either build from the github repository branches or to build from a release published on pypi.

```bash
spack add py-deephyper@master # from master branch on Github
spack add py-deephyper@develop # from develop branch on Github
spack add py-deephyper # from pypi
spack add py-deephyper@0.4.2 # version 0.4.2 from pypi
```

The `info` command can help retrieve more information about the possible variants and versions which can be installed.

```bash
spack info py-deephyper
```

## Accessing Shared Site Packages

Sometimes the HPC facility can provide already compiled/installed packages. Spack can reuse these packages by defining a new `upstream` configuration. After cloning the Spack repository and activating the Spack environment (the command `spack` should now be available in your shell) add a new upstream configuration in the YAML file `$SPACK_ROOT/etc/spack/upstream.yaml` (`$SPACK_ROOT` should be available in your environment after activation of Spack).

At the Argonne Leadership Computing Facility (ALCF), Spack packages are provided at the `/soft/spack/root/opt/spack` location. Therefore we can edit the `upstream.yaml` file such as:


```yaml
upstreams: 
    alcf-spack: 
        install_tree: /soft/spack/root/opt/spack
```

More information about [Chaining Spack Installations](https://spack.readthedocs.io/en/latest/chain.html#using-multiple-upstream-spack-instances).

## Spack and Conda

```
spack add miniconda3
```

for mac with arm64 use the `conda-forge` channel!
```
conda install -c conda-forge ...
```