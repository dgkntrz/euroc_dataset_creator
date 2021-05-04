# euroc_dataset_creator
A script dedicated to convert a video into a EuRoC dataset

## How does it work?

This script takes an input video, first timestamp and last timestamp, splits video into frames as well as labeling them. To create ground truth and IMU data, you will be needing to collect data from your sensor while recording. Check the tutorial below for collecting data about your sensors:

https://medium.com/analytics-vidhya/exploring-data-acquisition-and-trajectory-tracking-with-android-devices-and-python-9fdef38f25ee 

## Usage

### Dependencies

#### Pillow
python3 -m pip install --upgrade Pillow

#### Opencv
pip install opencv-python

### How to run?

python3 dataset_creator.py "video name" "first timestamp" "last timestamp"

python3 dataset_creator.py video.mp4 1000000000500000000 1000000090000000000
