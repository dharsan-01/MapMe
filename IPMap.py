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


# Create the main window
window = tk.Tk()
window.title("IP Geolocation Map")
window.geometry("400x200")

# Create a label and an entry field for IP address input
label = tk.Label(window, text="Enter IPv4 address:")
label.pack()

entry = tk.Entry(window)
entry.pack()

# Create a button to generate the map
button = tk.Button(window, text="Generate Map", command=generate_map)
button.pack()

# Create a label to display the status
status_label = tk.Label(window, text="")
status_label.pack()

# Start the main loop
window.mainloop()
