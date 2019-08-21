![banner](https://github.com/charlesfrye/psych101d-demo/blob/master/content/shared/img/banner.png?raw=true)

## Course Materials

{% capture materialtable  %}{% include materialtable.md %}{% endcapture %}
{{ materialtable | markdownify }}

This repository contains a subset of the materials for the course PSYCH101-D, "Data Science for Research Psychology", to be taught at UC Berkeley in Fall 2019.

It's intended to enable feedback on course content while development happens on a private repo.

Lectures (`lec/`), homeworks (`hw/`), and labs (`lab/`) are formatted as `.ipynb` files, aka JuPyter notebooks.

Currently, there are full demo materials for week 3, on Models and Random Variables.
There are also lab materials for weeks 4 and 7.
A link to a draft of the whole syllabus is available on request.

## Context

This class is targeted at sophomores and above who have completed one course on coding/statistics,
[data8](http://data8.org).
They will be familiar with Python, but won't have a full formal course in programming/computer science,
and they will be familiar with statistical concepts, especially the bootstrap.

Here's the course description:

> Experimental and data science abound with models. Models of data can be used to simulate, as in models of the climate, to explain simply, as in paper airplanes, and to predict, as in prototype models; all of these are forms of inferential thinking. In this course, we will learn to use Python to describe, create, manipulate, and interrogate models of data. With these new skills, we will simulate, explain, and predict phenomena and data, drawing examples from research psychology. As one application of these tools, we will learn classical statistical approaches, like null hypothesis significance testing and linear regression.

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

### datahub
This option is only available for individuals with a `berkeley.edu` account.
Simply click [this link](http://datahub.berkeley.edu/user-redirect/interact?account=charlesfrye&repo=psych101d-demo&branch=master&path=content/)
and then log in with your CalNet ID.
After a quick build, you'll be dropped into a JuPyter instance
with all of the materials loaded.
This material is persistent.

_If you've never used this service_, check out [this video](https://data.berkeley.edu/file/327).

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

## Known Issues

The `Slides` files in the `lec/` folder are intended for use with
[RISE](https://github.com/damianavila/RISE),
a "live-coding" presentation package.
This is currently not part of `requirements.txt`,
pending its incorporation into the master `datahub` environment,
so the `Slides` files here are formatted as traditional JuPyter notebooks.
