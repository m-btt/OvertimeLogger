import PySimpleGUI as sg
import pandas as pd
 
sg.theme("Dark Blue 3")

# reading csv file
df = pd.read_csv('samplecsv.csv', index_col=[-1])

# what is what
new_df = pd.DataFrame(['-Startinput-'], ['-END-'])

# window layout
layout = [[sg.Text("Enter start time:"), sg.Input(readonly=True, do_not_clear=True, size=(20, 1), enable_events=True, key='-Startinput-'), sg.CalendarButton('Current start time', close_when_date_chosen=True, format='%H:%M:%S')],
          [sg.Text("Enter end time:"), sg.Input(readonly=True, key='-END-', do_not_clear=True, size=(20, 1), enable_events=True), sg.CalendarButton('Current end time', close_when_date_chosen=True, format='%H:%M:%S')],
          [sg.Button('Submit Update'), sg.Exit()],
          ]

window =sg.Window('Overtime logger',layout)
   
# button stuff
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Submit Update':
       new_df.to_csv('samplecsv.csv', mode='a', index=[-1], header=False)
       sg.popup("Update submitted!")

window.close()  