**[Coquii STT](https://stt.readthedocs.io/en/latest/index.html) is an open-source deep-learning toolkit for training and deploying speech-to-text models.**

## Prerequisites
- python 3.6, 3.7 or 3.8
- Mac or Linux environment
- CUDA 10.0 and CuDNN v7.6

## Clone the STT repo from Github: 
`git clone https://github.com/coqui-ai/STT`

## Set up virtual environment
`python -m venv venv` <br>
`source venv/bin/activate`

## Install Dependencies
`python -m pip install --upgrade pip wheel setuptools` <br>
`pip install coqui_stt_training` <br>
`sudo apt-get install sox libsox-fmt-mp3 libopusfile0 libopus-dev libopusfile-dev`

## Follow the sequence of steps:
1. Prepare Dataset
2. Transfer Learn the Model
3. Build Language Model
4. Test the Model


