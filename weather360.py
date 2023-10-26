import tkinter as tk
import requests

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def get_weather():
    city = entry.get()
    api_key = 'OPENWEATHERMAP_API' 
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()

    if 'main' in data and 'temp' in data['main'] and 'weather' in data and len(data['weather']) > 0 and 'main' in data['weather'][0]:
        temperature_kelvin = data['main']['temp']
        temperature_fahrenheit = kelvin_to_fahrenheit(temperature_kelvin)
        weather = data['weather'][0]['main']
        result_label.config(text=f'Temperature: {temperature_fahrenheit:.2f}°F, Weather: {weather}')
    else:
        result_label.config(text='City not found or data not available')

app = tk.Tk()
app.title("Weather 360")

app.geometry("400x200")  

label = tk.Label(app, text="Enter city:", font=("Georgia", 16))
label.pack()

entry = tk.Entry(app, font=("Helvetica", 14))
entry.pack()

button = tk.Button(app, text="Get Weather", command=get_weather, font=("Georgia", 14), bg="blue", fg="white")
button.pack()

result_label = tk.Label(app, text="", font=("Helvetica", 14))
result_label.pack()

app.mainloop()
