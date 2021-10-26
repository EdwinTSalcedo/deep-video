# Examples of Video Processing with OpenCV

## Install Pyenv 
There are several options to work with independent development enviroments in Python but I personally 
prefer to use Pyenv. To see how to use this library, see the following links for [Windows](https://github.com/pyenv-win/pyenv-win) & [Linux](https://github.com/pyenv/pyenv). 

To learn more about how to use Pyenv, you can see this RealPython [article](https://realpython.com/intro-to-pyenv/)

## Create a new environment 
```
pyenv virtualenv 3.7.3 video-processing
```
If you don't know the Python version installed on your computer, run the following code. 
```
pyenv versions
```
Activate the environment
```
python activate video-processing
```

## Install dependencies
```
pip install -r requirements
```

## Install the face landmarks model
Download the dlib model from [here](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2) and uncompress the file with the next command.
```
bzip2 -d shape_predictor_68_face_landmarks.dat.bz2
```

## Run the experiments
```
python example1.py
```