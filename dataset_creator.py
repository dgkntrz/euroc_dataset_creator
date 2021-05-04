import os
import sys
import cv2
import math
from PIL import Image
import csv

currentPath = str(os.path.dirname(os.path.abspath(__file__)))
extractionPath = currentPath + r"\result"

if len(sys.argv) != 4:
  print("Please launch the script as following:")
  print("python3 dataset_creator.py <<video name>> <<first timestamp>> <<last timestamp>>")
  sys.exit()

try:
    videoName = sys.argv[1]
    firstTimestamp = int(sys.argv[2])
    lastTimestamp = int(sys.argv[3])
except:
    print("Timestamps must be numbers!")

if os.path.exists(currentPath+r"\results") == False:
  os.mkdir(currentPath+r"\results")
if os.path.exists(currentPath+r"\resized_results") == False:
    os.mkdir(currentPath+r"\resized_results")
if os.path.exists(currentPath+r"\final_results") == False:
    os.mkdir(currentPath+r"\final_results")

print("Created directories: results, resized_results, final_results")

vidcap = cv2.VideoCapture(videoName)
success,image = vidcap.read()
count = 0

while success:
  cv2.imwrite("results\\%d.png" % count, image)     # save frame as JPEG file
  success, image = vidcap.read()
  count += 1

print("Video splitted into frames! Results are stored in \"results\" folder.")

for i in range(count):
    image = Image.open("results\\"+str(i)+".png")
    new_image = image.resize((752,480))
    new_image.save("resized_results\\" + str(i) + ".png")

print("Images are resized into 752x480! Results are stored in \"resized_results\" folder.")

increaseRate = math.floor((lastTimestamp - firstTimestamp) / count)

for i in range(count):
    image = cv2.imread("resized_results\\" + str(i) + ".png")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("final_results\\" + str(i*increaseRate + firstTimestamp) + ".png", gray)

print("Images are grayscaled and renamed! Results are stored in \"resized_results\" folder.")

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["#timestamp [ns]", "filename"])
    for i in range(count):
        writer.writerow([str(i*increaseRate + firstTimestamp), str(i*increaseRate + firstTimestamp)+".png"])

print("Timestamps are corresponding file names are stored in \"data.csv\" file.")
