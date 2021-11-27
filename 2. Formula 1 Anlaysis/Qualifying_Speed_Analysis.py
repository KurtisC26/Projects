"""
This script has the purpose of extracting telemetry from the F1 app.
Particularly from qualifing sessions and comparing the results between drivers

"""
# 1.Loading dependencies:
import F1_Qualifying_Functions as quali_functions
import cv2
import pytesseract
import numpy as np
import pandas as pd
import seaborn as sns
import tkinter as tk
from tkinter import filedialog
import os
import matplotlib.pyplot as plt
import sys
from fpdf import FPDF
from scipy.signal import find_peaks
pd.options.mode.chained_assignment = None

# 2.Drivers and tracks:
drivers = {1:["Lewis Hamilton", "Mercedes"],
           2:["Valtteri Bottas", "Mercedes"],
           3:["Max Verstappen", "Red Bull"],
           4:["Sergio Perez","Red Bull"],
           5:["Lando Norris","McLaren"],
           6:["Daniel Ricciardo","McLaren"],
           7:["Charles Leclerc","Ferrari"],
           8:["Carlos Sainz","Ferrari"],
           9:["Pierre Gasly", "AlphaTauri"],
           10:["Yuki Tsunoda","AlphaTauri"],
           11:["Sebastian Vettel","Aston Martin"],
           12:["Lance Stroll","Aston Martin"],
           13:["Esteban Ocon","Alpine"],
           14:["Fernando Alonso","Alpine"],
           15:["Kimi Raikkonen","Alfa Romeo"],
           16:["Antonio Giovinazzi","Alfa Romeo"],
           17:["George Russel","Williams"],
           18:["Nicholas Latifi","Williams"],
           19:["Mick Schumacher","Haas"],
           20:["Nikita Mazepin","Haas"]}

tracks = {1:["Albert Park", 5.303, "Australia"],
           2:["Algarve International Circuit", 4.653, "Portugal"],
           3:["Autódromo Hermanos Rodríguez", 4.304, "Mexico"],
           4:["Autodromo Internazionale Enzo e Dino Ferrari",4.909, "Italy"],
           5:["Autodromo Josè Carlos Pace",4.309,"Brasil"],
           6:["Autodromo Nazionale di Monza",5.793,"Italy"],
           7:["Bahrain International Circuit",5.412,"Bahrain"],
           8:["Baku City Circuit",6.003,"Azerbaijan"],
           9:["Circuit de Barcelona-Catalunya",4.675 ,"Spain"],
           10:["Circuit de Monaco",3.337,"Monaco"],          
           11:["Circuit de Spa-Francorchamps",7.004,"Belgium"],          
           12:["Circuit of the Americas",5.513,"United States"],
           13:["Circuit Paul Ricard",5.842,"France"],
           14:["Circuit Zandvoort",4.259,"Netherlands"],
           15:["Hungaroring",4.381,"Hungary"],          
           16:["Jeddah Street Circuit",6.175,"Saudi Arabia"],
           17:["Red Bull Ring",4.318,"Austria"],
           18:["Silverstone Circuit",5.891,"United Kingdom"],
           19:["Sochi Autodrom",5.848,"Russia"],
           20:["Suzuka Circuit",5.807,"Japan"],
           21:["Yas Marina Circuit",5.554,"United Arab Emirates"],
           22:["Circuit Gilles Villeneuve",4.361,"Canada"]}

# 3.Video Analysis:
os.system('cls' if os.name == 'nt' else 'clear')
laps = quali_functions.how_many_laps("\nHow many qualifying laps would you like to compare?")

os.system('cls' if os.name == 'nt' else 'clear')
quali_track = quali_functions.track_select("Indicate the track:")

os.system('cls' if os.name == 'nt' else 'clear')
collection_interval = quali_functions.frame_rate_choice("\n Select the data collection interval:")

cols = ['Frame','Speed', 'Gear','DRS','Driver','Track','Lap_Distance']
data = []

lap_recordings = []
lap_drivers = []
lap_track = []
lap_distance = []

while len(lap_recordings) < laps:
    os.system('cls' if os.name == 'nt' else 'clear')
    driver = quali_functions.driver_select("\nWhich driver completed this lap?")
    lap_drivers.append(drivers[driver][0])
    lap_track.append(tracks[quali_track][0])
    lap_distance.append(tracks[quali_track][1])

    root = tk.Tk()
    root.withdraw()    
    video = filedialog.askopenfilename()
    driver_lap = cv2.VideoCapture(video)
    lap_recordings.append(driver_lap)
    os.system('cls' if os.name == 'nt' else 'clear')
   
for index, i in enumerate(lap_recordings, start=0):
    success,image = i.read()
    frame = 1
    # video characteristics:  
    fps = i.get(cv2.CAP_PROP_FPS)
    frame_count = i.get(cv2.CAP_PROP_FRAME_COUNT)
    width = i.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = i.get(cv2.CAP_PROP_FRAME_HEIGHT)

    frame_interval = round(fps * collection_interval)

    #Capturing data: 
    while success:
        try:
            #Driver    
            Driver = lap_drivers[index]
            Track = lap_track[index]
            Track_Distance = lap_distance[index]
            
            i.set(1,frame)
            success,image = i.read()
            ret, currentFrame = i.read()
            print(Driver,'Frame:',frame)
            # A. Speed in KM/H:
            Speed = currentFrame[round(height*0.6834):round(height*0.7296),round(width*0.5341):round(width*0.7048)]
            Speed = pytesseract.image_to_string(Speed,lang='F1r', config='--psm 6')
            # B. Gear:
            Gear = currentFrame[round(height*0.8220):round(height*0.8435),round(width*0.6277):round(width*0.671806167)]
            Gear = pytesseract.image_to_string(Gear,lang='F1r', config='--psm 6')
            # C. DRS open:
            DRS = currentFrame[round(height*0.7850):round(height*0.82),round(width*0.59):round(width*0.671806167)]
            greenMin = np.array([0, 116, 16], np.uint8)
            greenMax = np.array([62, 177, 88], np.uint8)
            thresh = cv2.inRange(DRS, greenMin, greenMax)
            count = np.sum(np.nonzero(thresh))
            if count == 0:
                DRS = 0
            else:
                DRS = 1
           
            # Populating data
            data.append([frame, Speed, Gear,DRS,Driver,Track,Track_Distance])
            df1 = pd.DataFrame(data, columns = cols)

            frame += frame_interval
        except:
            break

# 4.Data cleaning:
df1 = df1.replace('\n','', regex=True)
df1["Speed"] = df1["Speed"].astype(str).replace(' ', '')
df1["SpeedLength"] = df1['Speed'].astype(str).map(len)-1
df1 = df1[df1.SpeedLength > 0]
df1["Speed"] = np.where((df1.SpeedLength >= 4) ,df1.Speed.str[1:4],df1.Speed)
df1["Speed"] = df1["Speed"].astype(int)
df1 = df1[["Frame","Speed","Gear","DRS","Driver","Track","Lap_Distance"]]

drs_start = df1[df1.DRS == 1]
drs_start = drs_start.groupby(['Driver'])["Frame"].min()
data = pd.merge(df1,drs_start,how='left',on='Driver')

#Plot data:
data = data[data.Frame_x >= data.Frame_y]
data['Speed_m/s'] = data['Speed']/3.6
data['Speed_Lag'] = (data.groupby(['Driver'])['Speed'].shift(1))/3.6
data["speed_min"] = np.where(data["Speed_m/s"]<=data['Speed_Lag'],data["Speed_m/s"],data['Speed_Lag'])
data["Distance_M"] = (abs(data["Speed_m/s"]-data["Speed_Lag"])/2) + (data["speed_min"]*collection_interval)
            
data["Distance_Traveled"] = data.groupby('Driver')['Distance_M'].cumsum()
data = data[(data['Distance_Traveled']<=data['Lap_Distance']*1000) | pd.isnull(data["Distance_Traveled"])] 

data['RN'] = data.sort_values(['Driver','Frame_x'], ascending=[True,True]).groupby(['Driver']).cumcount() + 1

# 5.Export data to csv:
df1.to_csv('/Users/kurtis.campbell/Desktop/f1_data_test.csv')

# 6.Plotting telemetry:
sns.set_style("whitegrid")
sns.lineplot(x='RN', y='Speed', data = data, hue='Driver')
fig = plt.gcf()
fig.set_size_inches(15, 10)

plt.xlabel('Frame')
plt.ylabel('Speed (KM/H)')
plt.title('Qualifying Telemetry Analysis')
plt.savefig('/Users/kurtis.campbell/Desktop/seaborn_plot_testing.png')
plt.show()


# 7. Building a summary report:
print("Building Qulifying report")
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Automated Qualifying Report", ln=15, align="C")
pdf.cell(200, 10, txt="Lap comparison graph", ln=15, align="C")
pdf.image('/Users/kurtis.campbell/Desktop/seaborn_plot_testing.png',x = None, y = None, w = 200, h = 135, type = 'png')
pdf.output("/Users/kurtis.campbell/Desktop/test_f1_pdf.pdf")





#Building a PDF report:
#print("Building Qulifying report")

#pdf = FPDF()
#pdf.add_page()
#pdf.set_font("Arial", size=12)


#pdf.cell(200, 10, txt="Automated Qualifying Report", ln=15, align="C")
#pdf.cell(200, 10, txt=df1["Speed"], ln=15, align="C")

#pdf.cell(200, 10, txt="General Team Stats:", ln=15, align="L",)
#pdf.cell(200, 10, txt="Total Passes:"+ " "+str(Total_Passes), ln=2, align="L")
#pdf.cell(200, 10, txt="Possesions:"+ " "+str(Stints), ln=2, align="L")
#pdf.cell(200, 10, txt="Turnovers:"+ " "+str(TO), ln=2, align="L")
#pdf.cell(200, 10, txt="Passes Per Posession:"+ " "+str(Passes_Per_Stint), ln=2, align="L")
#pdf.cell(200, 10, txt="Passes Per Turnover:"+ " "+str(Passes_Per_TO), ln=2, align="L")

#pdf.set_font('arial', '', 12)
#pdf.output("/Users/kurtis.campbell/Desktop/test_f1_pdf.pdf")











