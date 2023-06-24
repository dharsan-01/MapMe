import tkinter as tk
import geocoder
import folium


def generate_map():
    ip_address = entry.get()

    try:
        ipee = geocoder.ip(ip_address)
        coordinates = ipee.latlng
        print("Coordinates: ", coordinates)

        map = folium.Map(location=coordinates, zoom_start=20)
        folium.Marker(coordinates).add_to(map)
        map.save('map1.html')

        status_label.config(text="Map generated successfully!")
    except:
        status_label.config(text="Invalid IP address")


window = tk.Tk()
window.title("IP Geolocation Map")
window.geometry("400x200")

label = tk.Label(window, text="Enter IPv4 address:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Generate Map", command=generate_map)
button.pack()

status_label = tk.Label(window, text="")
status_label.pack()

window.mainloop()
