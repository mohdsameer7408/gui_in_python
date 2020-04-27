from tkinter import *
import requests
import json

root = Tk()
root.title("Static")
root.iconbitmap('images/logos/my-ic.ico')
root.geometry('600x100')


# zip lookup method
def zip_lookup():
    # my_zip.get()
    # zip_label = Label(root, text=my_zip.get())
    # zip_label.grid(row=1, column=0, columnspan=2)

    try:
        api_request = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/'
                                   'json&zipCode=' + my_zip.get() + '&distance=5&API_'
                                                                    'KEY=3AE54B7E-883C-4333-B860-863545788B0D')
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        weather_color = '#0C0'
        if category == 'Good':
            weather_color = '#0C0'
        elif category == 'Moderate':
            weather_color = '#FFFF00'
        elif category == 'Unhealthy for Sensitive Groups':
            weather_color = '#ff9900'
        elif category == 'Unhealthy':
            weather_color = '#FF0000'
        elif category == 'Very Unhealthy':
            weather_color = '#990066'
        elif category == 'Hazardous':
            weather_color = '#660000'

        root.configure(background=weather_color)

        my_label = Label(root, text=city + ' Air Quality ' + str(quality) + ' ' + category,
                         font=('Helvetica', 20), background=weather_color)
        my_label.grid(row=1, column=0, columnspan=2)
    except EXCEPTION as e:
        api = 'Error...'


my_zip = Entry(root)
my_zip.grid(row=0, column=0, sticky=W+E+N+S)

zip_button = Button(root, text='LookUp ZipCode', command=zip_lookup)
zip_button.grid(row=0, column=1)

root.mainloop()
