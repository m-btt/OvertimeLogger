import PySimpleGUI as sg
import pandas as pd
 
# reading csv file
df = pd.read_csv('samplecsv.csv', header=[0])
print(df)

# what is what
new_df = pd.DataFrame(['-START-'], ['-END-'])
df.to_csv('samplecsv.csv', mode='a', header=True, index=False)

# window layout
layout = [[sg.Text("Enter start time:"), sg.Input(key='-START-', do_not_clear=True, size=(20, 1), enable_events=True), sg.CalendarButton('Current time')],
          [sg.Text("Enter end time:"), sg.Input(key='-END-', do_not_clear=True, size=(20, 1), enable_events=True), sg.CalendarButton('Current time')],
          [sg.Button('Submit Update'), sg.Exit()],
          ]

window =sg.Window('Overtime logger',layout)

def add_entry():
    df = pd.concat([df, new_df], ignore_index=True)
    return

def save_to_csv():
# save to csv
    new_df.to_csv('samplecsv.csv', encoding='UTF-8', header=None, index=False, mode='a')

# button stuff
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Submit Update':
       add_entry
       print(new_df)
       sg.popup("Update submitted!")
    elif event == 'Calendar':
        window['_CALENDAR_'](disabled=True)

window.close()  