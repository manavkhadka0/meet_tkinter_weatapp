# tkinter
import tkinter as tk
import requests
import json

# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
APPID = "c2ccfd9d1c994c584962e12bbafbf022"

def write_into_file(data):
    with open('data.json','w') as file:
        json.dump(data,file)



def getWeather(window):
    city = textField.get()
    api_response_url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + APPID
    response = requests.get(api_response_url)
    response_data = response.json()
    write_into_file(response_data)


window = tk.Tk()
window.title("Weather App")
window.geometry("800x800")
# textflied added
textField = tk.Entry(window,bg='#fafafa',justify='center',font=('poppins',35,'italic'),width=20)
textField.pack(pady=20)


# button added

button = tk.Button(window,text="Get Weather")
button.pack()
button.bind('<Button>',getWeather)

window.mainloop()
