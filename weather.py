# tkinter
import tkinter as tk
import requests
from PIL import Image,ImageTk
import json
from io import BytesIO
import datetime

# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
APPID = "c2ccfd9d1c994c584962e12bbafbf022" #YOUR API KEY

def write_into_file(data):
    with open('data.json','w') as file:
        json.dump(data,file)



def getWeather(window):
    city = textField.get()
    api_response_url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + APPID
    response = requests.get(api_response_url)
    response_data = response.json()
    write_into_file(response_data)

    # take data from the response
    try:
        # incons Api
        icons_url = f"http://openweathermap.org/img/wn/{response_data['weather'][0]['icon']}@2x.png"
        icon_response = requests.get(icons_url)
        icon_data = icon_response.content
        icon_image = ImageTk.PhotoImage(Image.open(BytesIO(icon_data)))



        condition= response_data['weather'][0]['main']

        # Changing background Image, Image lai read gareko
        bg_image_data = Image.open('./images/'+condition+'.jpg')
        resized_image_data = bg_image_data.resize((800,800),Image.ANTIALIAS)
        bg_image = ImageTk.PhotoImage(resized_image_data)

        temp = int(response_data['main']['temp']-273)
        temp_min = int(response_data['main']['temp_min']-273)
        temp_max = int(response_data['main']['temp_max']-273)
        pressure = response_data['main']['pressure']
        humidity = response_data['main']['humidity']
        wind = response_data['wind']['speed']
        sunrise_unix = response_data['sys']['sunrise']
        sunrise_readable = datetime.datetime.fromtimestamp(sunrise_unix)
        sunset_unix = response_data['sys']['sunset']
        sunset_readable = datetime.datetime.fromtimestamp(sunset_unix)
        final_data = f"{condition} \n {temp} °C"
        final_info = f'Min Temp: {temp_min}°C \n Max Temp: {temp_max}°C \n Pressure: {pressure} \n Humidity: {humidity} \n wind: {wind} \n Sunrise: {sunrise_readable} \n Sunset: {sunset_readable}'
        label1.config(text=final_data)
        label2.config(text=final_info)
        # image lai haleko
        label3.configure(image=bg_image)
        label3.image = (bg_image)
        icons_label.configure(image=icon_image)
        icons_label.image = (icon_image)
    except KeyError:
        label1.config(text= response_data['message'])
        label2.config(text = response_data['cod'])
    













window = tk.Tk()
window.title("Weather App")
window.geometry("800x800")

bg_image_data = Image.open('./images/bg.jpg')
resized_image_data = bg_image_data.resize((800,800),Image.ANTIALIAS)
bg_image = ImageTk.PhotoImage(resized_image_data)
label3 = tk.Label(window,image=bg_image)
label3.place(x=0,y=0)


# textflied added
textField = tk.Entry(window,bg='#fafafa',justify='center',font=('poppins',35,'italic'),width=20)
textField.pack(pady=20)


# button added

button = tk.Button(window,text="Get Weather")
button.pack()
button.bind('<Button>',getWeather)


icons_label = tk.Label(window,bg='#afafaf')
icons_label.pack()
label1 = tk.Label(window,bg='#afafaf',font=('poppins',20,'italic'))
label1.pack()
label2 = tk.Label(window,bg='#afafaf',font=('poppins',20,'italic'))
label2.pack()





window.mainloop()
