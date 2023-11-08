# Deep Video

A curated collection of material and tutorials for video processing. 

## Dependencies

### Pyenv
There are several options to work with virtual enviroments in Python, but I personally prefer to use Pyenv. To see how to install and use this tool, see the following [link](https://github.com/pyenv/pyenv). 

To learn more about how to use Pyenv, you can see this [RealPython article](https://realpython.com/intro-to-pyenv/)

After installing Pyenv, you should install Python version 3.10.3 (This was the lattest Python version tested for the present repo):

```
pyenv install 3.10.3
```
Then, create a new environment:
```
pyenv virtualenv 3.10.3 deep-video
```
If you don't know the Python versions installed on your computer under Pyenv, run the following code: 
```
pyenv versions
```
Then, activate the environment:
```
pyenv activate deep-video
```
Finally, install the dependencies:
```
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

## Run the experiments
All examples are implemented in folder `examples`, and you can execute them as follows:

```
python exampleX.py
```
where X is the number of experiment. 