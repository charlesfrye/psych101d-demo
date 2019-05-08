![banner](https://github.com/charlesfrye/psych101d-demo/blob/master/shared/img/banner.png?raw=true)

# psych101d-demo

This repository contains a subset of the materials for the course PSYCH101-D, "Data Science for Research Psychology", to be taught at UC Berkeley in Fall 2019.

It's intended to enable feedback on course content while development happens on a private repo.

Lectures (`lec/`), homeworks (`hw/`), and labs (`lab/`) are formatted as `.ipynb` files, aka JuPyter notebooks.

Currently, there are demo materials for week 3, on Models and Random Variables.
A link to a draft of the whole syllabus is available on request.

## How to Contribute

It's easiest for contributors to raise issues, rather than make pull requests,
since the actual development branch for this class is a private repository.

## How to Get Started

If you don't want to install anything ...
    
... and you're **not Berkeley-affiliated**, check out the instructions for **Binder**.

... and you're **Berkeley-affiliated**, check out the instructions for **`datahub`**.
    
Otherwise, follow the instructions for **local installation**.

### Binder
This option is available for all users and minimizes installation effort, but does not provide a persistent environment.
That is, edits will be lost.
However, it has the benefit of automatically tracking the latest version of the material without any effort.

Click the badge below to deploy the content to a cloud instance with [Binder](https://mybinder.org).
You'll be able to edit and execute notebooks in a temporary environment.
If you stop interacting for some time (~20 minutes) you will lose any changes.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/charlesfrye/psych101d-demo/master)

### `datahub`
This option is only available for individuals with a `berkeley.edu` account.
Simply download the repo as a `zip` and upload it to `datahub.berkeley.edu`,
then unzip it.

_If you've never used this service_: just head to
[datahub.berkeley.edu](https://datahub.berkeley.edu)
and log in with your CalNet ID.
You'll be given persistent space on a cloud deployment of JupyterHub.
Upload the zipped repository.

**Unzipping on `datahub`**:
to unzip on `datahub`, start by launching a command line.
Use the dropdown `New` menu (top-right) and select `Terminal`.
Then, use the command
```
unzip name_of_zip.zip
```
to unzip the uploaded `zip` file.
You can then close the command line.

### Local Installation

Clone the repository as normal, then install using
```
pip install -r requirements.txt
```
in your development environment.

For reasons related to the current computing setup for data science education on Berkeley's campus,
the `requirements` are strict: versions are specified to the third decimal point
and Python must be version `3.6.*`.
This level of specificity typically requires the building of many wheels, some of which have known bugs
on Python 3.5 or 3.7.

## Notes and Known Issues

The `Slides` files in the `lec/` folder are intended for use with
[RISE](https://github.com/damianavila/RISE),
a "live-coding" presentation package.
This is currently not part of `requirements.txt`,
pending its incorporation into the master `datahub` environment,
so the `Slides` files here are formatted as traditional JuPyter notebooks.
