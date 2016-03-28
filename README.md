# seyir-analyzer

Tools to analyse the seyir (melodic progression) of scores and audio recordings of makam music

Introduction
=======
The repository implements the melody progression analysis methods explained in the paper.

_B. Bozkurt, "Computational analysis of overall melodic progression for Turkish Makam Music", in "Penser l’improvisation" edited by Mondher Ayari, pp. 289-298, ISBN: 9782752102485, 2015, Delatour France, Sampzon._

Currently audio seyir analysis is implemented. The algorithm gets the predominant melody of an audio recording as the input and divide it to chunks with the specified frame size and hop ratio. The pitch distribution of each chunk is computed and the peaks of these distributions are selected as the stable pitches performed at that interval. The mean pitch of each chunk is also computed. To visualize the analysis we decided to use the representation for the symbolic analysis (Figure 4), as we find it more informative.

Later score analysis and joint audio-score analysis (from alignment) will be added.

Usage
=======
```python
from seyiranalyzer.AudioSeyirAnalyzer import AudioSeyirAnalyzer

audioSeyirAnalyzer = AudioSeyirAnalyzer()
seyir_features = audioSeyirAnalyzer.analyze(pitch, frame_dur = frame_dur, hop_ratio = hop_ratio)

audioSeyirAnalyzer.plot(seyir_features)
```

The inputs for audioSeyirAnalyzer.analyze are:
```python
# pitch 		    : an n-by-2 numpy array, where the values in the first column are 
#					  the timestamps and the values in the second column are frequency 
#					  values. You can use the predominant melody extraction algorithm
#                     available in https://github.com/sertansenturk/predominantmelodymakam
# frame_size        : the duration of the chunks computed from the pitch in seconds
# hop_ratio         : the ratio of the time between the consecutive jumps of chunks
#                     with respect to the duration of the chunks.
#                     (Example: if the chunk_size is 16 seconds and the hop_ratio is
#                     0.25, the hop size is 4 seconds.)
```

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
Sertan Şentürk
contact@sertansenturk.com

Reference
-------
Thesis
