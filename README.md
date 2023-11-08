<h1 align="center">
  Deep Video
</h1>

A curated collection of material and tutorials for video processing. 

<div align="center">
  <a href="#installation"><b>Installation</b></a>
  | <a href="#usage"><b>Usage</b></a>
  | <a href="#examples"><b>Examples</b></a>
</div>

## Installation

### Pyenv
You need to install [Pyenv](https://github.com/pyenv/pyenv), then run the code below:  

```bash
# Install Python version 3.10.3  (This was the lattest Python version tested for the present repo):
pyenv install 3.10.3

# Create a new environment:
pyenv virtualenv 3.10.3 deep-video

# Activate the environment:
pyenv activate deep-video

#Finally, install the dependencies:
pip install -r requirements
```

### ML dependencies

#### DLib
[Dlib](http://dlib.net/) is a cutting-edge C++ toolkit that includes tools and pre-trained ML models. Numerous fields, including robotics, embedded devices, and mobile phones, employ it in both industry and academia. Dlib is freely applicable in any application due to its open source licencing. As for image processing, Dlib counts on the following tools: 
- Image Processing
- Routines for reading and writing common image formats.
- Automatic color space conversion between various pixel types
- Common image operations such as edge finding and morphological operations
- Implementations of the SURF, HOG, and FHOG feature extraction algorithms.
- Tools for detecting objects in images including frontal face detection and object pose estimation.
- High quality face recognition

We will make use of DLib face landmark detection in the examples. 

## Usage
All examples are implemented in folder `examples`, and you can execute them as follows:

```
python exampleX.py
```
where X is the number of experiment. 

## Examples
* [Open Video](examples/example1.py)

