import PySimpleGUI as sg
# import time

# now = time.strftime("%x")

date = sg.Text("Enter today's date: ")
date_box = sg.InputText(key="datekey")

mood = sg.Text("How would you rate your mood on a scale of 1 to 10? ")
mood_box = sg.InputText(key="moodkey")

thoughts = sg.Text("Let your thoughts flow: ")
thoughts_box = sg.InputText(key="tkey")

button = sg.Button("Submit")

window = sg.Window('My Journal', 
                   layout=[[date, date_box],
                           [mood, mood_box],
                           [thoughts, thoughts_box],
                           [button]])

while True:
    event, values = window.read()
    print(event)
    print(values)

    date = values["datekey"]
    mood = "My mood today is: " + values["moodkey"]
    # mood = values["moodkey"]
    thoughts = values["tkey"]
    match event:
        case "Submit":
            with open(f"{date}.txt", "w") as file:
                file.write(mood + 2 * '\n')
                file.write(thoughts)

