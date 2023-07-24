import PySimpleGUI as sg
import pandas as pd
import datetime as dt

sg.theme("Dark Blue 3")

# reading csv file
df = pd.read_csv('samplecsv.csv', index_col=[-1])

# what is what
rightnow = pd.Timestamp('now')
daytoday = pd.Timestamp.today()
new_df = pd.DataFrame([rightnow], [daytoday])

def addupdate():
     df = pd.concat([df, new_df], ignore_index=True, ignore_header=False)
  
# window layout
layout = [[sg.Button('Submit Update'), sg.Exit()],
          ]

window =sg.Window('Overtime logger',layout,size=(180,180))
   
# button stuff
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Submit Update':
       addupdate
       new_df.to_csv('samplecsv.csv', mode='a', index=True, header=False)
       sg.popup("Update submitted!")

window.close()  