"""
Python Script is made to watch a screen recording of the F1 timing app, extract the basic telemetry data, and
produce a telemtry plot for one driver.

by: Kurtis Campbell
Last updateed: 05-2021
"""

# 1. Load dependencies:
import numpy as np
import pandas as pd
from os import listdir
import cv2
import pytesseract
import openpyxl
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
import argparse
import sys
from PIL import *
import matplotlib.pyplot as plt
import seaborn as sns


# Select a video,
# Reads the video and extracts the data
# Saves the data as a csv in the same folder as the video
# builds a pdf report on breaking, max speeds and
# Maybe a comparison of two drivers

# 2. Import the screen recording of the lap(s):
#Option 1: Python will prompt you to select a file:
root = tk.Tk()
root.withdraw()
video = filedialog.askopenfilename() ## -->Option 2: Indicate the path of the video
videocap = cv2.VideoCapture(video)

# 3. Establsihing the video characteristics:
fps = videocap.get(cv2.CAP_PROP_FPS)
frame_count = videocap.get(cv2.CAP_PROP_FRAME_COUNT)
width = videocap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = videocap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# 4. Initiate the video reading:
success,image = videocap.read()
frame = 1

# 5. Set up a the raw information for the data table:
cols = ['Frame','Speed', 'Gear', 'RPM','Tyre_Life','Tyre_Choice','DRS']
data = []

# 6. Loop through the video to collect data:
while success:
    try:
        videocap.set(1,frame)
        success,image = videocap.read()
        ret, currentFrame = videocap.read()
        print('New Frame:', success, frame)

        # A. Extracting the car speed in KM/H:
        Speed = currentFrame[round(height*0.6834):round(height*0.7296),round(width*0.5341):round(width*0.7048)]
        Speed = pytesseract.image_to_string(Speed,lang='F1r', config='--psm 6')
        print(Speed)

        # B. Extrating the gear:
        Gear = currentFrame[round(height*0.8220):round(height*0.8435),round(width*0.6277):round(width*0.671806167)]
        Gear = pytesseract.image_to_string(Gear,lang='F1r', config='--psm 6')
        print(Gear)

        # C. Extrating the RPM:
        RPM = currentFrame[round(height*0.7419):round(height*0.7697),round(width*0.5396):round(width*0.6993)]
        RPM = pytesseract.image_to_string(RPM,lang='F1r', config='--psm 6')
        print(RPM)

        # D. Tyre life:
        Tyre_Life = currentFrame[round(height*0.6126):round(height*0.6527),round(width*0.8710):round(width*0.9300)]
        Tyre_Life = pytesseract.image_to_string(Tyre_Life,lang='F1r', config='--psm 6')
        print(Tyre_Life)

        # E. Tyre choice:
        Tyre_Choice = currentFrame[round(height*0.6126):round(height*0.6527),round(width*0.910):round(width*0.9850)]
        Tyre_Choice = pytesseract.image_to_string(Tyre_Choice,lang='F1r', config='--psm 6')
        print(Tyre_Choice)

        # G. Throttle percentage:         # H. Brake percentage
        
        # I. DRS open:
        DRS = currentFrame[round(height*0.7850):round(height*0.82),round(width*0.59):round(width*0.671806167)]
    
        greenMin = np.array([0, 116, 16], np.uint8)
        greenMax = np.array([62, 177, 88], np.uint8)

        thresh = cv2.inRange(DRS, greenMin, greenMax)
        count = np.sum(np.nonzero(thresh))
        print("count =",count)
        if count == 0:
            DRS = 0
        else:
            DRS = 1
        print("")
        
        # Driver Being Tracked:
        Driver = currentFrame[round(height*0.53):round(height*0.61),round(width*0.23):round(width*0.85)]

        data.append([frame, Speed, Gear, RPM, Tyre_Life,Tyre_Choice,DRS])
        df1 = pd.DataFrame(data, columns = cols)


        # Initiate the sequence in the loop of collecting data:
        frame += 1000
        
    except:
        break




# 7. Build/clean data table
df1 = df1.replace('\n','', regex=True)
df1["Speed"] = df1["Speed"].astype(str).replace(' ', '')
df1["SpeedLength"] = df1['Speed'].astype(str).map(len)-1
df1 = df1[df1.SpeedLength > 0]
df1["Speed"] = np.where((df1.SpeedLength >= 4) ,df1.Speed.str[1:4],df1.Speed)
df1["Speed"] = df1["Speed"] .astype(int)








# 8. Build a telemetry analysis:
plot_data = df1[["Frame","Speed","DRS"]]
fig_dims = (16, 7)
sns.relplot(x='Frame', y='Speed', data=plot_data, hue='DRS')
fig = plt.gcf()
fig.set_size_inches(15, 10)

# # naming the x axis
plt.xlabel('Frame')
# # naming the y axis
plt.ylabel('Speed KM/H')
  
# # giving a title to my graph
plt.title('Speed over Frame number')
plt.show()



#df1.to_csv('/Users/kurtis.campbell/Desktop/f1_data_test.csv')

print("Script has successfully run")
