# seyir-analyzer

Introduction
============
Tools to analyse the seyir (melodic progression) of scores and audio recordings of makam music

Usage
=======

Installation
============

If you want to install the repository, it is recommended to install the package and dependencies into a virtualenv. In the terminal, do the following:

    virtualenv env
    source env/bin/activate
    python setup.py install

If you want to be able to edit files and have the changes be reflected, then install the repository like this instead

    pip install -e .

The algorithm uses several modules in Essentia. Follow the [instructions](essentia.upf.edu/documentation/installing.html) to install the library.

Now you can install the rest of the dependencies:

    pip install -r requirements

Authors
-------
Sertan Senturk
contact@sertansenturk.com

Acknowledgements
------
We would like to thank Dr. Robert Grafias for allowing us to use [his makam music collection](https://eee.uci.edu/programs/rgarfias/films.html) in our research (in this repository the recording with MBID: [d2731692-626d-4a6d-9b67-a70c9e7b9745](http://musicbrainz.org/recording/d2731692-626d-4a6d-9b67-a70c9e7b9745)).

Reference
-------
Thesis