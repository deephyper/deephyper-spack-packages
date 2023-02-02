# DeepHyper Spack Packages

This repository contains a collection of [Spack](https://spack.io) packages to manage the building of DeepHyper from source. Start by installing Spack on your system:

```bash
git clone -c feature.manyFiles=true https://github.com/spack/spack.git
. ./spack/share/spack/setup-env.sh 
```

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
spack add py-deephyper@develop +autodeuq+hps-tl+mpi+nas+redis
```