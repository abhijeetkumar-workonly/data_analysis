from datetime import datetime
import math
import tkinter
from matplotlib import dates
from matplotlib.ticker import FormatStrFormatter
import numpy as np
import ttkbootstrap as ttk
from tkinter import filedialog 
from tkinter import messagebox
import matplotlib.pyplot as plt
import mplcursors
import os



status_dropdown_visible = False
y_dropdown_2_visible = False
y_dropdown_3_visible = False
y_dropdown_4_visible = False
combine_subplots_on = False
subplots_dropdown_on = False



status_dropdown_s_visible = False
y_dropdown_2_s_visible = False
y_dropdown_3_s_visible = False
y_dropdown_4_s_visible = False
combine_subplots_s_on = False
subplots_dropdown_s_on = False

combine_primary_secondary_on = False
compare_primary_secondary_on = False

packet_size = 00000
corrupted_packets = 000

odd_frame_id_byte_position = 0000
even_frame_id_byte_position = 0000

lon_gcs = 000000
lat_gcs = 0000000

lon_gdt2 = 00000000000
lat_gdt2  = 00000000000
                

def update_dropdowns():
    global subplots_dropdown_on
    if y_dropdown_2_visible or y_dropdown_3_visible or y_dropdown_4_visible:
        subplots_dropdown_on = True
        combine_plots.config(state="enabled")
        status_dropdown_toggle.config(state='disabled')
    else:
        subplots_dropdown_on = False
        combine_plots.config(state="disabled")
        status_dropdown_toggle.config(state='enabled')
     
    if combine_primary_secondary_on or compare_primary_secondary_on:        
        function_button.config(state='disabled')
        function_button_s.config(state='disabled')
        special_plotter.config(state='enabled')
    else:
        function_button.config(state='enabled')
        function_button_s.config(state='enabled')
        special_plotter.config(state='disabled')
    
    if combine_primary_secondary_on:
        compare_primary_secondary.config(state='disabled')
    else:
        compare_primary_secondary.config(state='enabled')
        
    if compare_primary_secondary_on:
        combine_primary_secondary.config(state='disabled')
    else:
        combine_primary_secondary.config(state='enabled')

    
    if y_dropdown_2_visible:
        y_dropdown_2.grid(row=4, column=1, padx=5, pady=5)
        y_dropdown_2_toggle.grid(row=4, column=0, padx=5, pady=5)
        y_dropdown_2_toggle.config(text="➖", bootstyle = "danger outline")
    else:
        y_dropdown_2.grid_forget()
        y_dropdown_2_toggle.grid(row=4, column=1, padx=5, pady=5)
        y_dropdown_2_toggle.config(text="➕", bootstyle = "success outline")

    if y_dropdown_3_visible:
        y_dropdown_3.grid(row=5, column=1, padx=5, pady=5)
        y_dropdown_3_toggle.grid(row=5, column=0, padx=5, pady=5)
        y_dropdown_3_toggle.config(text="➖", bootstyle = "danger outline")
    else:
        y_dropdown_3.grid_forget()
        y_dropdown_3_toggle.grid(row=5, column=1, padx=5, pady=5)
        y_dropdown_3_toggle.config(text="➕", bootstyle = "success outline")

    if y_dropdown_4_visible:
        y_dropdown_4.grid(row=6, column=1, padx=5, pady=5)
        y_dropdown_4_toggle.grid(row=6, column=0, padx=5, pady=5)
        y_dropdown_4_toggle.config(text="➖", bootstyle = "danger outline")
    else:
        y_dropdown_4.grid_forget()
        y_dropdown_4_toggle.grid(row=6, column=1, padx=5, pady=5)
        y_dropdown_4_toggle.config(text="➕", bootstyle = "success outline")
    if status_dropdown_visible:
        status_dropdown.grid(row=7, column=1, padx=5, pady=5)
        status_dropdown_toggle.grid(row=7, column=0, columnspan=1, padx=5, pady=5)
        status_dropdown_toggle.config(text="Hide Status Dropdown", bootstyle = "danger outline")
    else:
        status_dropdown.grid_forget()
        status_dropdown_toggle.grid(row=7, columnspan=2, padx=5, pady=5)
        status_dropdown_toggle.config(text="Show Status Dropdown", bootstyle = "warning outline")

def update_dropdowns_s():
    global subplots_dropdown_s_on
    if y_dropdown_2_s_visible or y_dropdown_3_s_visible or y_dropdown_4_s_visible:
        subplots_dropdown_s_on = True
        combine_plots_s.config(state='enabled')
        status_dropdown_toggle_s.config(state='disabled')
    else:
        subplots_dropdown_s_on = False
        combine_plots_s.config(state='disabled')
        status_dropdown_toggle_s.config(state='enabled')
     
    if combine_primary_secondary_on or compare_primary_secondary_on:        
        function_button.config(state='disabled')
        function_button_s.config(state='disabled')
        special_plotter.config(state='enabled')
    else:
        function_button.config(state='enabled')
        function_button_s.config(state='enabled')
        special_plotter.config(state='disabled')
    
    if combine_primary_secondary_on:
        compare_primary_secondary.config(state='disabled')
    else:
        compare_primary_secondary.config(state='enabled')
        
    if compare_primary_secondary_on:
        combine_primary_secondary.config(state='disabled')
    else:
        combine_primary_secondary.config(state='enabled')
    if y_dropdown_2_s_visible:
        y_dropdown_2_s.grid(row=4, column=1, padx=5, pady=5)
        y_dropdown_2_toggle_s.grid(row=4, column=0, padx=5, pady=5)
        y_dropdown_2_toggle_s.config(text='➖', bootstyle = 'danger outline')
    else:
        y_dropdown_2_s.grid_forget()
        y_dropdown_2_toggle_s.grid(row=4, column=1, padx=5, pady=5)
        y_dropdown_2_toggle_s.config(text='➕', bootstyle = 'success outline')
    if y_dropdown_3_s_visible:
        y_dropdown_3_s.grid(row=5, column=1, padx=5, pady=5)
        y_dropdown_3_toggle_s.grid(row=5, column=0 ,padx=5, pady=5)
        y_dropdown_3_toggle_s.config(text='➖', bootstyle = 'danger outline')
    else:
        y_dropdown_3_s.grid_forget()
        y_dropdown_3_toggle_s.grid(row=5, column=1, padx=5, pady=5)
        y_dropdown_3_toggle_s.config(text='➕', bootstyle = 'success outline')
    if y_dropdown_4_s_visible:
        y_dropdown_4_s.grid(row=6, column=1, padx=5, pady=5)
        y_dropdown_4_toggle_s.grid(row=6, column=0, padx=5, pady=5)
        y_dropdown_4_toggle_s.config(text='➖', bootstyle = 'danger outline')
    else:
        y_dropdown_4_s.grid_forget()
        y_dropdown_4_toggle_s.grid(row=6, column=1, padx=5, pady=5)
        y_dropdown_4_toggle_s.config(text='➕', bootstyle = 'success outline')
    if status_dropdown_s_visible:
        status_dropdown_s.grid(row=7, column=1, padx=5, pady=5)
        status_dropdown_toggle_s.grid(row=7, column=0, columnspan=1, padx=5, pady=5)
        status_dropdown_toggle_s.config(text='Hide Status Dropdown', bootstyle = 'danger outline')
    else:
        status_dropdown_s.grid_forget()
        status_dropdown_toggle_s.grid(row=7, columnspan=2, padx=5, pady=5)
        status_dropdown_toggle_s.config(text="Show Status Dropdown", bootstyle = 'warning outline')

def y_2_toggle():
    global y_dropdown_2_visible
    y_dropdown_2_visible = not y_dropdown_2_visible
    update_dropdowns()
def y_3_toggle():
    global y_dropdown_3_visible
    y_dropdown_3_visible = not y_dropdown_3_visible
    update_dropdowns()
def y_4_toggle():
    global y_dropdown_4_visible
    y_dropdown_4_visible = not y_dropdown_4_visible
    update_dropdowns()
def status_toggle():
    global status_dropdown_visible
    status_dropdown_visible = not status_dropdown_visible
    update_dropdowns()
def combine_subplots():
    global combine_subplots_on
    combine_subplots_on = not combine_subplots_on
    update_dropdowns()

def y_2_s_toggle():
    global y_dropdown_2_s_visible
    y_dropdown_2_s_visible = not y_dropdown_2_s_visible
    update_dropdowns_s()
def y_3_s_toggle():
    global y_dropdown_3_s_visible
    y_dropdown_3_s_visible = not y_dropdown_3_s_visible
    update_dropdowns_s()
def y_4_s_toggle():
    global y_dropdown_4_s_visible
    y_dropdown_4_s_visible = not y_dropdown_4_s_visible
    update_dropdowns_s()
def status_s_toggle():
    global status_dropdown_s_visible
    status_dropdown_s_visible = not status_dropdown_s_visible
    update_dropdowns_s()
def combine_subplots_s():
    global combine_subplots_s_on
    combine_subplots_s_on = not combine_subplots_s_on
    update_dropdowns_s()


def combine_pri_sec():
    global combine_primary_secondary_on
    combine_primary_secondary_on = not combine_primary_secondary_on
    update_dropdowns()
    update_dropdowns_s()
def compare_pri_sec():
    global compare_primary_secondary_on
    compare_primary_secondary_on = not compare_primary_secondary_on
    update_dropdowns()
    update_dropdowns_s()

# Browse For File IInd data
def browse_file_s():
    global file_path_s
    file_path_s = filedialog.askopenfilename(filetypes=[("Binary File", "*.bin")])
    if file_path_s:
        file_name_s = os.path.basename(file_path_s)
        file_label_s.config(text='Plesae Wait Reading Data.............', bootstyle= 'danger')
        root.update()
        function_button_s.config(state="enabled")
        x_dropdown_s.config(values=options)
        y_dropdown_s.config(values=options)
        y_dropdown_2_s.config(values=options)
        y_dropdown_3_s.config(values=options)
        y_dropdown_4_s.config(values=options)
        status_dropdown_s.config(values=status_options)
        file_label_s.config(text=f'Selected File : {file_name_s}', bootstyle = 'primary')
    else:
        file_label_s.config(text="No File Selected")

#  select file  First Data 
def browse_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Binary File", "*.bin")])
    if file_path:
        file_name = os.path.basename(file_path)
        file_label.config(text="Please Wait Reading Data...............", bootstyle = 'danger')
        root.update()
        function_button.config(state="enabled")
        x_dropdown.config(values=options)
        y_dropdown.config(values=options)
        y_dropdown_2.config(values=options)
        y_dropdown_3.config(values=options)
        y_dropdown_4.config(values=options)
        status_dropdown.config(values=status_options)
        file_label.config(text=f'Selected File : {file_name}', bootstyle = 'primary')
    else:
        file_label.config(text="No File Selected")

############################################################################################



options = ['']

status_options = ['']
########################################################################################################    


# FOR PRESET Plotting ########################################################
def lat_lon(bin_file):
    lon = []
    lat = []
    return lon, lat

def annotation(bin_file):

    roll_data = []
    pitch_data = []
    range_data = []
    hdg_data = []
    elev_data = []

    return roll_data, pitch_data, range_data, hdg_data, elev_data

#### 3D Plotting #############################################################
def func_3d():
    try:
        lon, lat = lat_lon(file_path)
        alt_amsl =[]
        x = lat
        y = lon
        z = alt_amsl
        fig = plt.figure()
        ax = plt.axes (projection = '3d')
        ax.plot3D(x, y, z, marker=',')
        ax.scatter(x[0], y[0],z[0], marker = "D", color = "green")
        ax.scatter(x[-1], y[-1],z[-1], marker = "d", color = "black")
        ax.set_xlabel("LONGITUDE")
        ax.set_ylabel("LATITUDE")
        ax.set_zlabel("ALTITUDE ABOVE Sea (FEET)")
        ax.set_title(f"Longitude vs Latitude vs Altitude-AMSL(FEET)")
        ax.grid(True)
        plt.show()
    except :
        messagebox.showerror("ERROR", "Please Select A Valid Flight Data First!!")
        
def func_3d_s():
    try:
        lon, lat = lat_lon(file_path_s)
        alt_amsl = []
        x = lat
        y = lon
        z = alt_amsl
        fig = plt.figure()
        ax = plt.axes (projection = '3d')
        ax.plot3D(x, y, z, marker=',')
        ax.scatter(x[0], y[0],z[0], marker = "D", color = "green")
        ax.scatter(x[-1], y[-1],z[-1], marker = "d", color = "black")
        ax.set_xlabel("LONGITUDE")
        ax.set_ylabel("LATITUDE")
        ax.set_zlabel("ALTITUDE ABOVE Sea (FEET)")
        ax.set_title(f"Longitude vs Latitude vs Altitude-AMSL(FEET)")
        ax.grid(True)
        plt.show()
    except :
        messagebox.showerror("ERROR", "Please Select A Valid Flight Data First!!")
##################################################################################


# Primary Preset Plottings #################################################

def uhf_plot():
    try: 
        lon, lat= lat_lon(file_path)
        lon = lon
        lat = lat
        elev_cbar = []
        elev_cbar = elev_cbar

        uhf = []
        uhf = uhf                

        roll_data, pitch_data, range_data, hdg_data, elev_data = annotation(file_path)
        azm_data = []
        
        
        max_elev = max(elev_cbar)
        min_elev = min(elev_cbar)

        elev_ticks = np.linspace(min_elev, max_elev, 6)
    
        roll_data = roll_data
        pitch_data = pitch_data
        range_data = range_data
        hdg_data = hdg_data
        azm_data = azm_data

        def show_annotations(sel):
            ind = int(sel.index)
            roll = roll_data[ind]
            pitch = pitch_data[ind]
            range_e = range_data[ind]
            hdg = hdg_data[ind]
            azm = azm_data[ind]

            x,y = sel.target
            sel.annotation.set_text(f'X: {x:.2f}\nY: {y:.2f}\nRoll: {roll:.2f} Deg\nPitch: {pitch:.2f} Deg\nRange: {range_e:.2f} KM\nHeading: {hdg:.2f} Deg\nAZM: {azm}Deg')

        nok_indicies = [i for i, status in enumerate(uhf) if status == "NOK"]
        nok_percentage = len(nok_indicies)/len(lat)*100

        plt.figure()
        line = plt.plot(lon, lat, linewidth=0.1)
        plt.scatter(lon, lat, c=elev_cbar, cmap='YlGnBu_r', marker='.')
        colorbar = plt.colorbar()
        colorbar.set_label('Elevation')
        colorbar.set_ticks(elev_ticks)
        mplcursors.cursor(line, multiple = True).connect("add", show_annotations)
        plt.scatter([lon[i] for i in nok_indicies], [lat[i] for i in nok_indicies], color='red', marker='o', label=f'UHF Link Out: {nok_percentage:.4f}%')
        plt.scatter(lon_gcs, lat_gcs, marker='s', color='#00ffff')
        plt.scatter(lon_gdt2, lat_gdt2, marker='s', color='#000000')
        plt.title("Longitude vs Latitude with UHF Link Sts")
        plt.xlabel("Longitude")      
        plt.ylabel("Latitude")
        plt.legend()
        plt.grid(True)
        plt.show()
    except :
        messagebox.showerror("Error", "Select Flight Data First")
        
def c_plot():
    try: 
        lon, lat= lat_lon(file_path)
        lon = lon
        lat = lat
        elev_cbar = []
        elev_cbar = elev_cbar

        c = []
        c = c                

        roll_data, pitch_data, range_data, hdg_data, elev_data = annotation(file_path)

        max_elev = max(elev_cbar)
        min_elev = min(elev_cbar)
        elev_ticks = np.linspace(min_elev, max_elev, 6)
    
        roll_data = roll_data
        pitch_data = pitch_data
        range_data = range_data
        hdg_data = hdg_data

        def show_annotations(sel):
            ind = int(sel.index)
            roll = roll_data[ind]
            pitch = pitch_data[ind]
            range_e = range_data[ind]
            hdg = hdg_data[ind]

            x,y = sel.target
            sel.annotation.set_text(f'X: {x:.2f}\nY: {y:.2f}\nRoll: {roll:.2f} Deg\nPitch: {pitch:.2f} Deg\nRange: {range_e:.2f} KM\nHeading: {hdg:.2f} Deg')

        nok_indicies = [i for i, status in enumerate(c) if status == "NOK"]
        nok_percentage = len(nok_indicies)/len(lat)*100

        plt.figure()
        line = plt.plot(lon, lat, linewidth=0.1)
        plt.scatter(lon, lat, c=elev_cbar, cmap='YlGnBu_r', marker='.')
        colorbar = plt.colorbar()
        colorbar.set_label('Elevation')
        colorbar.set_ticks(elev_ticks)
        mplcursors.cursor(line, multiple = True).connect("add", show_annotations)
        plt.scatter([lon[i] for i in nok_indicies], [lat[i] for i in nok_indicies], color='red', marker='o', label=f'C Link Out: {nok_percentage:.4f}%')
        plt.scatter(lon_gcs, lat_gcs, marker='s', color='#00ffff')
        plt.scatter(lon_gdt2, lat_gdt2, marker='s', color='#000000')
        plt.title("Longitude vs Latitude with C Link Sts")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.legend()
        plt.grid(True)
        plt.show()
    except :
        messagebox.showerror("Error", "Select Flight Data First")

def sat_plot():
    try: 
        lon, lat= lat_lon(file_path)
        lon = lon
        lat = lat
        elev_cbar = []
        elev_cbar = elev_cbar

        sat = []
        sat = sat                

        roll_data, pitch_data, range_data, hdg_data, elev_data  = annotation(file_path)
    
        roll_data = roll_data
        pitch_data = pitch_data
        range_data = range_data
        hdg_data = hdg_data
        
        max_elev = max(elev_cbar)
        min_elev = min(elev_cbar)
        elev_ticks = np.linspace(min_elev, max_elev, 6)

        def show_annotations(sel):
            ind = int(sel.index)
            roll = roll_data[ind]
            pitch = pitch_data[ind]
            range_e = range_data[ind]
            hdg = hdg_data[ind]

            x,y = sel.target
            sel.annotation.set_text(f'X: {x:.2f}\nY: {y:.2f}\nRoll: {roll:.2f} Deg\nPitch: {pitch:.2f} Deg\nRange: {range_e:.2f} KM\nHeading: {hdg:.2f} Deg')

        nok_indicies = [i for i, status in enumerate(sat) if status == "NOK"]
        nok_percentage = len(nok_indicies)/len(lat)*100

        plt.figure()
        line = plt.plot(lon, lat, linewidth=0.1)
        plt.scatter(lon, lat, c=elev_cbar, cmap='YlGnBu_r', marker='.')
        colorbar = plt.colorbar()
        colorbar.set_label('Elevation')
        colorbar.set_ticks(elev_ticks)
        mplcursors.cursor(line, multiple = True).connect("add", show_annotations)
        plt.scatter([lon[i] for i in nok_indicies], [lat[i] for i in nok_indicies], color='red', marker='o', label=f'SAT Link Out: {nok_percentage:.4f}%')
        plt.scatter(lon_gcs, lat_gcs, marker='s', color='#00ffff')
        plt.scatter(lon_gdt2, lat_gdt2, marker='s', color='#000000')
        plt.title("Longitude vs Latitude with SAT Link Sts")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.legend()
        plt.grid(True)
        plt.show()
    except :
        messagebox.showerror("Error", "Select Flight Data First")

def cmd_plot():
    try: 
        lon, lat= lat_lon(file_path)
        lon = lon
        lat = lat
        elev_cbar = []
        elev_cbar = elev_cbar

        cmd = []
        cmd = cmd                

        roll_data, pitch_data, range_data, hdg_data, elev_data  = annotation(file_path)
    
        roll_data = roll_data
        pitch_data = pitch_data
        range_data = range_data
        hdg_data = hdg_data
        
        max_elev = max(elev_cbar)
        min_elev = min(elev_cbar)
        elev_ticks = np.linspace(min_elev, max_elev, 6)

        def show_annotations(sel):
            ind = int(sel.index)
            roll = roll_data[ind]
            pitch = pitch_data[ind]
            range_e = range_data[ind]
            hdg = hdg_data[ind]

            x,y = sel.target
            sel.annotation.set_text(f'X: {x:.2f}\nY: {y:.2f}\nRoll: {roll:.2f} Deg\nPitch: {pitch:.2f} Deg\nRange: {range_e:.2f} KM\nHeading: {hdg:.2f} Deg')

        nok_indicies = [i for i, status in enumerate(cmd) if status == "NOK"]
        nok_percentage = len(nok_indicies)/len(lat)*100

        plt.figure()
        line = plt.plot(lon, lat, linewidth=0.1)
        plt.scatter(lon, lat, c=elev_cbar, cmap='YlGnBu_r', marker='.')
        colorbar = plt.colorbar()
        colorbar.set_label('Elevation')
        colorbar.set_ticks(elev_ticks)
        mplcursors.cursor(line, multiple = True).connect("add", show_annotations)
        plt.scatter([lon[i] for i in nok_indicies], [lat[i] for i in nok_indicies], color='red', marker='o', label=f'CMD Link Out: {nok_percentage:.4f}%')
        plt.scatter(lon_gcs, lat_gcs, marker='s', color='#00ffff')
        plt.scatter(lon_gdt2, lat_gdt2, marker='s', color='#000000')
        plt.title("Longitude vs Latitude with CMD Link Sts")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.legend()
        plt.grid(True)
        plt.show()
    except :
        messagebox.showerror("Error", "Select Flight Data First")
    
# Secondary Preset PLotting ################################################
 
def uhf_plot_s():
    try: 
        lon, lat = lat_lon(file_path_s)

        lon = lon
        lat = lat

        uhf = []
        uhf = uhf             

        roll_data, pitch_data, range_data, hdg_data, elev_data  = annotation(file_path_s)
    
        roll_data = roll_data
        pitch_data = pitch_data
        range_data = range_data
        hdg_data = hdg_data

        def show_annotations(sel):
            ind = int(sel.index)
            roll = roll_data[ind]
            pitch = pitch_data[ind]
            range_e = range_data[ind]
            hdg = hdg_data[ind]

            x,y = sel.target
            sel.annotation.set_text(f'X: {x:.2f}\nY: {y:.2f}\nRoll: {roll:.2f} Deg\nPitch: {pitch:.2f} Deg\nRange: {range_e:.2f} KM\nHeading: {hdg:.2f} Deg')

        nok_indicies = [i for i, status in enumerate(uhf) if status == "NOK"]
        nok_percentage = len(nok_indicies)/len(lat)*100

        fig, ax = plt.subplots()
        line = ax.plot(lon, lat, marker=',')
        mplcursors.cursor(line, multiple = True).connect("add", show_annotations)
        ax.scatter([lon[i] for i in nok_indicies], [lat[i] for i in nok_indicies], color='red', marker='o', label=f'UHF Link Out: {nok_percentage:.4f}%')
        ax.scatter(lon[0], lat[0], marker='D', color='green')
        ax.scatter(lon[-1], lat[-1], marker='d', color='black')
        ax.set_title("Longitude vs Latitude with UHF Link Sts")
        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")
        ax.legend()
        plt.grid(True)
        plt.show()
    except :
        messagebox.showerror("Error", "Select Flight Data First")

def c_plot_s():
    try:
        lon, lat = lat_lon(file_path_s)

        lon = lon
        lat = lat

        c = []
        c = c               

        roll_data, pitch_data, range_data, hdg_data, elev_data  = annotation(file_path_s)
    
        roll_data = roll_data
        pitch_data = pitch_data
        range_data = range_data
        hdg_data = hdg_data

        def show_annotations(sel):
            ind = int(sel.index)
            roll = roll_data[ind]
            pitch = pitch_data[ind]
            range_e = range_data[ind]
            hdg = hdg_data[ind]

            x,y = sel.target
            sel.annotation.set_text(f'X: {x:.2f}\nY: {y:.2f}\nRoll: {roll:.2f} Deg\nPitch: {pitch:.2f} Deg\nRange: {range_e:.2f} KM\nHeading: {hdg:.2f} Deg')

        nok_indicies = [i for i, status in enumerate(c) if status == "NOK"]
        nok_percentage = len(nok_indicies)/len(lat)*100

        fig, ax = plt.subplots()
        line = ax.plot(lon, lat, marker=',')
        mplcursors.cursor(line, multiple = True).connect("add", show_annotations)
        ax.scatter([lon[i] for i in nok_indicies], [lat[i] for i in nok_indicies], color='red', marker='o', label=f'C Link Out: {nok_percentage:.4f}%')
        ax.scatter(lon[0], lat[0], marker='D', color='green')
        ax.scatter(lon[-1], lat[-1], marker='d', color='black')
        ax.set_title("Longitude vs Latitude with C Link Sts")
        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")
        ax.legend()
        plt.grid(True)
        plt.show()
    except :
        messagebox.showerror("Error", "Select Flight Data First")

def sat_plot_s():
    try:
        lon, lat = lat_lon(file_path_s)

        lon = lon
        lat = lat

        sat = []
        sat = sat            

        roll_data, pitch_data, range_data, hdg_data, elev_data  = annotation(file_path_s)
    
        roll_data = roll_data
        pitch_data = pitch_data
        range_data = range_data
        hdg_data = hdg_data

        def show_annotations(sel):
            ind = int(sel.index)
            roll = roll_data[ind]
            pitch = pitch_data[ind]
            range_e = range_data[ind]
            hdg = hdg_data[ind]

            x,y = sel.target
            sel.annotation.set_text(f'X: {x:.2f}\nY: {y:.2f}\nRoll: {roll:.2f} Deg\nPitch: {pitch:.2f} Deg\nRange: {range_e:.2f} KM\nHeading: {hdg:.2f} Deg')

        nok_indicies = [i for i, status in enumerate(sat) if status == "NOK"]
        nok_percentage = len(nok_indicies)/len(lat)*100

        fig, ax = plt.subplots()
        line = ax.plot(lon, lat, marker=',')
        mplcursors.cursor(line, multiple = True).connect("add", show_annotations)
        ax.scatter([lon[i] for i in nok_indicies], [lat[i] for i in nok_indicies], color='red', marker='o', label=f'SAT Link Out: {nok_percentage:.4f}%')
        ax.scatter(lon[0], lat[0], marker='D', color='green')
        ax.scatter(lon[-1], lat[-1], marker='d', color='black')
        ax.set_title("Longitude vs Latitude with SAT Link Sts")
        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")
        ax.legend()
        plt.grid(True)
        plt.show()
    except :
        messagebox.showerror("Error", "Select Flight Data First")

def cmd_plot_s():
    try:
        lon, lat = lat_lon(file_path_s)

        lon = lon
        lat = lat

        cmd = []
        cmd = cmd             

        roll_data, pitch_data, range_data, hdg_data, elev_data  = annotation(file_path_s)
    
        roll_data = roll_data
        pitch_data = pitch_data
        range_data = range_data
        hdg_data = hdg_data

        def show_annotations(sel):
            ind = int(sel.index)
            roll = roll_data[ind]
            pitch = pitch_data[ind]
            range_e = range_data[ind]
            hdg = hdg_data[ind]

            x,y = sel.target
            sel.annotation.set_text(f'X: {x:.2f}\nY: {y:.2f}\nRoll: {roll:.2f} Deg\nPitch: {pitch:.2f} Deg\nRange: {range_e:.2f} KM\nHeading: {hdg:.2f} Deg')

        nok_indicies = [i for i, status in enumerate(cmd) if status == "NOK"]
        nok_percentage = len(nok_indicies)/len(lat)*100

        fig, ax = plt.subplots()
        line = ax.plot(lon, lat, marker=',')
        mplcursors.cursor(line, multiple = True).connect("add", show_annotations)
        ax.scatter([lon[i] for i in nok_indicies], [lat[i] for i in nok_indicies], color='red', marker='o', label=f'CMD Link Out: {nok_percentage:.4f}%')
        ax.scatter(lon[0], lat[0], marker='D', color='green')
        ax.scatter(lon[-1], lat[-1], marker='d', color='black')
        ax.set_title("Longitude vs Latitude with CMD Link Sts")
        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")
        ax.legend()
        plt.grid(True)
        plt.show()
    except :
        messagebox.showerror("Error", "Select Flight Data First")
##########################################################################################



def function_btn():
    flight_msn_date = []

    x = globals().get(x_dropdown.get().lower())
    y = globals().get(y_dropdown.get().lower())
    if y and callable(y) and x and callable(x):
        x_axis = x(file_path)
        y_axis = y(file_path)

        x_axis = x_axis
        y_axis = y_axis
        if status_dropdown_visible and status_dropdown.get() != '':
            status_name = status_dropdown.get()
            status_data = globals().get(status_dropdown.get().lower())
            if status_data and callable(status_data):
                status_values = status_data(file_path)

                roll_data, pitch_data, range_data, hdg_data, elev_data = annotation(file_path)
                ias_data = []
                gnd_data = []
                plagc_gdt1_data = []
                azm_gdt1_data = []
                alt_amsl_data = []
                # alt_data = alt_rm_amsl_meter(file_path)
                time_data = []

                roll_data = roll_data
                pitch_data = pitch_data
                range_data = range_data
                hdg_data = hdg_data
                elev_data = elev_data
                ias_data = ias_data
                gnd_data = gnd_data
                plagc_gdt1_data = plagc_gdt1_data
                azm_gdt1_data = azm_gdt1_data
                alt_amsl_data = alt_amsl_data
                # alt_data = alt_data
                time_data = time_data

                def show_annotations(sel):
                    ind = int(sel.index)
                    # roll = roll_data[ind]      # For special plots
                    # pitch = pitch_data[ind]
                    range_e = range_data[ind]
                    hdg = hdg_data[ind]
                    elev = elev_data[ind]
                    ias = ias_data[ind]
                    gnd = gnd_data[ind]
                    plagc_gdt1 = plagc_gdt1_data[ind]
                    azm_gdt1 = azm_gdt1_data[ind]
                    alt_amsl = alt_amsl_data[ind]
                    # alt = alt_data[ind]
                    dayTime = time_data[ind]
                    dayTime = str(dayTime).removeprefix("1900-01-01 ")
                    x,y = sel.target
                    sel.annotation.set_text(f'X: {x:.4f}\nY: {y:.4f}\nRange: {range_e:.2f} KM\nHeading: {hdg:.2f} Deg\nElevation: {elev:.2f} Deg\nIAS_Speed: {ias:.2f} kts\nGND_Speed: {gnd:.2f} kts\nPL_AGC_GDT1: {plagc_gdt1:.2f} dBm\nAZM_GDT1: {azm_gdt1:.2f} deg\nALT_AMSL: {alt_amsl:.2f} feet\nTime: {dayTime}')
        
        
# For Combined Plots within one Graph ##########################################################################
        if combine_subplots_on:
            fig, ax = plt.subplots(figsize=(8, 6))
            
            line_0 = ax.plot(x_axis, y_axis, marker=',', label=y_dropdown.get())
            mplcursors.cursor(line_0)
            ax.scatter(x_axis[0], y_axis[0], color='green', marker='D')
            ax.scatter(x_axis[-1], y_axis[-1], color='k', marker='d')
            
            line_count = 1
            
            if y_dropdown_2_visible and y_dropdown_2.get()!= '':
                y_2 = globals().get(y_dropdown_2.get().lower())
                if y_2 and callable(y_2):
                    y_2_axis = y_2(file_path)
                    
                y_2_axis = y_2_axis

                line_1 = ax.plot(x_axis, y_2_axis, marker=',', label=y_dropdown_2.get())
                mplcursors.cursor(line_1, multiple = True)
                line_count += 1
                ax.set_ylabel(f"{y_dropdown_2.get()} -- {y_dropdown.get()}")
                ax.scatter(x_axis[0], y_2_axis[0], color='green', marker='D')
                ax.scatter(x_axis[-1], y_2_axis[-1], color='k', marker='d')
                
            if y_dropdown_3_visible and y_dropdown_3.get()!='':
                y_3 = globals().get(y_dropdown_3.get().lower())
                if y_3 and callable(y_3):
                    y_3_axis = y_3(file_path)
                y_3_axis = y_3_axis

                line_2 = ax.plot(x_axis, y_3_axis, marker =',', label = y_dropdown_3.get())
                mplcursors.cursor(line_2, multiple = True)
                line_count += 1
                ax.set_ylabel(f'{y_dropdown_3.get()} -- {y_dropdown_2.get()} -- {y_dropdown.get()}')
                ax.scatter(x_axis[0], y_3_axis[0], color = 'green', marker="D")
                ax.scatter(x_axis[-1], y_3_axis[-1], color = 'black', marker="d")
            
            if y_dropdown_4_visible and y_dropdown_4.get()!= '':
                y_4 = globals().get(y_dropdown_4.get().lower())
                if y_4 and callable(y_4):
                    y_4_axis = y_4(file_path)
                y_4_axis = y_4_axis

                line_3 = ax.plot(x_axis, y_4_axis, marker = ',', label = y_dropdown_4.get())
                mplcursors.cursor(line_3, multiple = True)
                line_count += 1
                ax.set_ylabel(f'{y_dropdown_4.get()} -- {y_dropdown_3.get()} -- {y_dropdown_2.get()} -- {y_dropdown.get()}')
                ax.scatter(x_axis[0], y_4_axis[0], marker='D', color = 'green')
                ax.scatter(x_axis[-1], y_4_axis[-1], marker='d', color = 'black')
            
            if all(isinstance(val, datetime) for val in x_axis):
                ax.xaxis.set_major_formatter(dates.DateFormatter('%H:%M:%S'))
            else:
                ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))   
                
            ax.set_title(f'Flight Date: {flight_msn_date}')
            ax.set_xlabel(x_dropdown.get())
            # Add legends for all lines
            ax.legend()
            # Add grid
            ax.grid(True)
            # Show the plot
            plt.tight_layout()
            plt.show()
#################################################################################################################           
        elif subplots_dropdown_on and not combine_subplots_on:
            num_subplots = 0
            if y_dropdown_2_visible:
                num_subplots += 1
            if y_dropdown_3_visible:
                num_subplots += 1
            if y_dropdown_4_visible:
                num_subplots += 1
                
            if num_subplots > 0:
                fig, axes = plt.subplots(num_subplots + 1, 1, figsize=(8, 6), sharex = True)
                
                line0 = axes[0].plot(x_axis, y_axis, marker=',', label=y_dropdown.get())
                mplcursors.cursor(line0, multiple = True)
                axes[0].scatter(x_axis[0], y_axis[0], color='green', marker='D')
                axes[0].scatter(x_axis[-1], y_axis[-1], color='k', marker='d')
                axes[0].set_ylabel(y_dropdown.get())
                axes[0].grid(True)

                # Counter for subplots
                subplot_count = 1
                if y_dropdown_2_visible and y_dropdown_2.get() != '':
                    y_2 = globals().get(y_dropdown_2.get().lower())
                    if y_2 and callable(y_2):
                        y_2_axis = y_2(file_path)
                        
                    y_2_axis = y_2_axis
                    
                    line1 = axes[subplot_count].plot(x_axis, y_2_axis, marker=',', label=y_dropdown_2.get())
                    mplcursors.cursor(line1, multiple = True)
                    axes[subplot_count].set_ylabel(y_dropdown_2.get())
                    axes[subplot_count].grid(True)
                    axes[subplot_count].scatter(x_axis[0], y_2_axis[0], color='green', marker='D')
                    axes[subplot_count].scatter(x_axis[-1], y_2_axis[-1], color='k', marker='d')
                    subplot_count += 1

                if y_dropdown_3_visible and y_dropdown_3.get() != '':
                    y_3 = globals().get(y_dropdown_3.get().lower())
                    if y_3 and callable(y_3):
                        y_3_axis = y_3(file_path)
                    y_3_axis = y_3_axis
                    line2 = axes[subplot_count].plot(x_axis, y_3_axis, marker=',', label=y_dropdown_3.get())
                    mplcursors.cursor(line2, multiple = True)
                    axes[subplot_count].set_ylabel(y_dropdown_3.get())
                    axes[subplot_count].grid(True)
                    axes[subplot_count].scatter(x_axis[0], y_3_axis[0], color='green', marker='D')
                    axes[subplot_count].scatter(x_axis[-1], y_3_axis[-1], color='k', marker='d')
                    subplot_count += 1

                if y_dropdown_4_visible and y_dropdown_4.get() != '':
                    y_4 = globals().get(y_dropdown_4.get().lower())
                    if y_4 and callable(y_4):
                        y_4_axis = y_4(file_path)
                    y_4_axis = y_4_axis
                    line3 = axes[subplot_count].plot(x_axis, y_4_axis, marker=',', label=y_dropdown_4.get())
                    mplcursors.cursor(line3, multiple = True)
                    axes[subplot_count].set_ylabel(y_dropdown_4.get())
                    axes[subplot_count].grid(True)
                    axes[subplot_count].scatter(x_axis[0], y_4_axis[0], color='green', marker='D')
                    axes[subplot_count].scatter(x_axis[-1], y_4_axis[-1], color='k', marker='d')

                if all(isinstance(val, datetime) for val in x_axis):
                    for ax in axes:
                        ax.xaxis.set_major_formatter(dates.DateFormatter('%H:%M:%S'))
                else:
                    for ax in axes:
                        ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))

                if num_subplots > 0:
                    axes[-1].set_xlabel(x_dropdown.get())
                else:
                    ax.set_xlabel(x_dropdown.get())
                plt.xlabel(x_dropdown.get())
                for ax in axes:
                    ax.legend()
                
                plt.tight_layout()
                plt.show()
                       
        else:
            if status_dropdown_visible and status_dropdown.get() != '':
                elev_cbar = []
                elev_cbar = elev_cbar
                
                max_elev = max(elev_cbar)
                min_elev = min(elev_cbar)

                elev_ticks = np.linspace(min_elev, max_elev, 6)

                plt.figure()
                line = plt.plot(x_axis, y_axis, linewidth=0.1, label=y_dropdown.get())
                plt.scatter(x_axis, y_axis, c=elev_cbar, cmap='YlGnBu_r', marker='.')
                colorbar = plt.colorbar()
                colorbar.set_label('Elevation')
                colorbar.set_ticks(elev_ticks)
                plt.xlabel(x_dropdown.get())
                plt.ylabel(y_dropdown.get())
                nok_indicies = [i for i, status in enumerate(status_values) if status == 'NOK']
                nok_percentage = (len(nok_indicies)/len(y_axis))*100 if len(y_axis) > 0 else 0
                plt.scatter([x_axis[i] for i in nok_indicies], [y_axis[i] for i in nok_indicies], marker='.', color = "red", label = f'Link Outage ({nok_percentage:.4f}%)', linewidths=0.5)
                plt.title(f"Flight Date: {flight_msn_date}\n {x_dropdown.get()} vs {y_dropdown.get()} with {status_name}")
                mplcursors.cursor(line, multiple = True).connect("add", show_annotations)
                plt.scatter(lon_gcs, lat_gcs, marker='s', color='#00ffff')
                plt.scatter(lon_gdt2, lat_gdt2, marker='s', color='#000000')
                plt.subplots_adjust(left=0.07, right=1)
                
                plt.legend()
                plt.grid(True)
                plt.show()
            else:
                fig, ax = plt.subplots()
                if x_dropdown.get()=="AV_LONGITUDE" or x_dropdown.get()=="AV_LATITUDE":    
                    line = ax.scatter(x_axis, y_axis, marker='.', label=y_dropdown.get())
                else:
                    line = ax.plot(x_axis, y_axis, marker=',', label=y_dropdown.get())
                ax.set_xlabel(x_dropdown.get())
                ax.set_ylabel(y_dropdown.get())
                if status_dropdown_visible and status_dropdown.get() != '':
                    nok_indicies = [i for i, status in enumerate(status_values) if status == 'NOK']
                    nok_percentage = (len(nok_indicies)/len(y_axis))*100 if len(y_axis) > 0 else 0
                    ax.scatter([x_axis[i] for i in nok_indicies], [y_axis[i] for i in nok_indicies], color = "red", marker='o', label = f'Link Outage ({nok_percentage:.4f}%)')
                    ax.set_title(f"Flight Date: {flight_msn_date}\n {x_dropdown.get()} vs {y_dropdown.get()} with {status_name}")
                    mplcursors.cursor(line, multiple = True).connect("add", show_annotations)
                else:
                    ax.set_title(f"Flight Date: {flight_msn_date}\n {x_dropdown.get()} vs {y_dropdown.get()}")
                    mplcursors.cursor(line, multiple = True)
                # ax.scatter(lon_gcs, lat_gcs, marker='s', color='#00ffff')
                # ax.scatter(lon_gdt2, lat_gdt2, marker='s', color='#000000')
                if all(isinstance(val, datetime) for val in x_axis):
                    ax.xaxis.set_major_formatter(dates.DateFormatter('%H:%M:%S'))
                else:
                    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
                
                ax.legend()
                plt.grid(True)
                plt.show()

def function_btn_s():
    flight_msn_date = []
    x = globals().get(x_dropdown_s.get().lower())
    y = globals().get(y_dropdown_s.get().lower())
    if y and callable(y) and x and callable(x):
        x_axis = x(file_path_s)
        y_axis = y(file_path_s)

        x_axis = x_axis
        y_axis = y_axis
        if status_dropdown_s_visible and status_dropdown_s.get()!='':
            status_name = status_dropdown_s.get()
            status_data = globals().get(status_dropdown_s.get().lower())
            if status_data and callable(status_data):
                status_values = status_data(file_path_s)

                roll_data, pitch_data, range_data, hdg_data = annotation(file_path_s)
                
                roll_data = roll_data
                pitch_data = pitch_data
                range_data = range_data
                hdg_data = hdg_data

                def show_annotations(sel):
                    ind = int(sel.index)
                    roll = roll_data[ind]
                    pitch = pitch_data[ind]
                    range_e = range_data[ind]
                    hdg = hdg_data[ind]

                    x,y = sel.target
                    sel.annotation.set_text(f'X: {x:.2f}\nY: {y:.2f}\nRoll: {roll:.2f} Deg\nPitch: {pitch:.2f} Deg\nRange: {range_e:.2f} KM\nHeading: {hdg:.2f} Deg')
# For combined Plots within one graph ########################
        if combine_subplots_s_on:
            fig, ax = plt.subplots(figsize = (8,6))

            line_0 = ax.plot(x_axis, y_axis, marker = ',', label = y_dropdown_s.get())
            mplcursors.cursor(line_0, multiple = True)
            ax.scatter(x_axis[0], y_axis[0], color = 'green', marker = 'D')
            ax.scatter(x_axis[-1], y_axis[-1], color = 'k', marker='d')

            line_count = 1
            
            if y_dropdown_2_s_visible and y_dropdown_2_s.get()!='':
                y_2 = globals().get(y_dropdown_2_s.get().lower())
                if y_2 and callable(y_2):
                    y_2_axis = y_2(file_path_s)
                y_2_axis = y_2_axis

                line_1 = ax.plot(x_axis, y_2_axis, marker=',', label = y_dropdown_2_s.get())
                mplcursors.cursor(line_1, multiple = True)
                line_count += 1
                ax.set_ylabel(f"{y_dropdown_2_s.get()} -- {y_dropdown_s.get()}")
                ax.scatter(x_axis[0], y_2_axis[0], color = 'green', marker='D')
                ax.scatter(x_axis[-1], y_2_axis[-1], color='k', marker='d')

            if y_dropdown_3_s_visible and y_dropdown_3_s.get()!='':
                y_3 = globals().get(y_dropdown_3_s.get().lower())
                if y_3 and callable(y_3):
                    y_3_axis = y_3(file_path_s)
                y_3_axis = y_3_axis
                line_2 = ax.plot(x_axis, y_3_axis, marker = ',', label = y_dropdown_3_s.get())
                mplcursors.cursor(line_2, multiple = True)
                line_count += 1
                ax.set_ylabel(f'{y_dropdown_3_s.get()} -- {y_dropdown_2_s.get()} -- {y_dropdown_s.get()}')
                ax.scatter(x_axis[0], y_3_axis[0], color = 'green', marker='D')
                ax.scatter(x_axis[-1], y_3_axis[-1], color = 'k', marker='d')

            if y_dropdown_4_s_visible and y_dropdown_4_s.get()!='':
                y_4 = globals().get(y_dropdown_4_s.get().lower())
                if y_4 and callable(y_4):
                    y_4_axis = y_4(file_path_s)
                y_4_axis = y_4_axis

                line_3 = ax.plot(x_axis, y_4_axis, marker =',', label = y_dropdown_4_s.get())
                mplcursors.cursor(line_3, multiple = True)
                line_count += 1
                ax.set_ylabel(f'{y_dropdown_4_s.get()} -- {y_dropdown_3_s.get()} -- {y_dropdown_2_s.get()} -- {y_dropdown_s.get()}')
                ax.scatter(x_axis[0], y_axis[0], marker='D', color = 'green')
                ax.scatter(x_axis[-1], y_4_axis[-1], marker='d', color = 'k')
            
            if all(isinstance(val, datetime) for val in x_axis):
                ax.xaxis.set_major_formatter(dates.DateFormatter('%H:%M'))
            else:
                ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f')) 
            ax.set_title(f'Flight Date: {flight_msn_date}')
            ax.set_xlabel(x_dropdown_s.get())
            ax.legend()
            ax.grid(True)
            plt.tight_layout()
            plt.show()
        elif subplots_dropdown_s_on and not combine_subplots_s_on:
            num_subplots = 0
            if y_dropdown_2_s_visible:
                num_subplots += 1
            if y_dropdown_3_s_visible:
                num_subplots += 1
            if y_dropdown_4_s_visible:
                num_subplots += 1
                
            if num_subplots > 0:
                fig, axes = plt.subplots(num_subplots +1, 1, figsize=(8,6), sharex=True)

                line0 = axes[0].plot(x_axis, y_axis, marker=',', label = y_dropdown_s.get())
                mplcursors.cursor(line0, multiple = True)
                axes[0].scatter(x_axis[0], y_axis[0], color = 'green', marker = 'D')
                axes[0].scatter(x_axis[-1], y_axis[-1], color = 'k', marker = 'd')
                axes[0].set_ylabel(y_dropdown_s.get())
                axes[0].grid(True)

                subplot_count = 1
                if y_dropdown_2_s_visible and y_dropdown_2_s.get()!='':
                    y_2 = globals().get(y_dropdown_2_s.get().lower())
                    if y_2 and callable(y_2):
                        y_2_axis = y_2(file_path_s)
                    y_2_axis = y_2_axis

                    line1 = axes[subplot_count].plot(x_axis, y_2_axis, marker = ',', label = y_dropdown_2_s.get())
                    mplcursors.cursor(line1, multiple = True)
                    axes[subplot_count].set_ylabel(y_dropdown_2_s.get())
                    axes[subplot_count].grid(True)
                    axes[subplot_count].scatter(x_axis[0], y_2_axis[0], color='green', marker='D')
                    axes[subplot_count].scatter(x_axis[-1], y_2_axis[-1], color='k', marker='d')
                    subplot_count += 1

                if y_dropdown_3_s_visible and y_dropdown_3_s.get() != '':
                    y_3 = globals().get(y_dropdown_3_s.get().lower())
                    if y_3 and callable(y_3):
                        y_3_axis = y_3(file_path_s)
                    y_3_axis = y_3_axis
                    line2 = axes[subplot_count].plot(x_axis, y_3_axis, marker=',', label=y_dropdown_3_s.get())
                    mplcursors.cursor(line2, multiple = True)
                    axes[subplot_count].set_ylabel(y_dropdown_3_s.get())
                    axes[subplot_count].grid(True)
                    axes[subplot_count].scatter(x_axis[0], y_3_axis[0], color='green', marker='D')
                    axes[subplot_count].scatter(x_axis[-1], y_3_axis[-1], color='k', marker='d')
                    subplot_count += 1

                if y_dropdown_4_s_visible and y_dropdown_4_s.get() != '':
                    y_4 = globals().get(y_dropdown_4_s.get().lower())
                    if y_4 and callable(y_4):
                        y_4_axis = y_4(file_path_s)
                    y_4_axis = y_4_axis
                    line3 = axes[subplot_count].plot(x_axis, y_4_axis, marker=',', label=y_dropdown_4_s.get())
                    mplcursors.cursor(line3, multiple = True)
                    axes[subplot_count].set_ylabel(y_dropdown_4_s.get())
                    axes[subplot_count].grid(True)
                    axes[subplot_count].scatter(x_axis[0], y_4_axis[0], color='green', marker='D')
                    axes[subplot_count].scatter(x_axis[-1], y_4_axis[-1], color='k', marker='d')

                if all(isinstance(val, datetime) for val in x_axis):
                    for ax in axes:
                        ax.xaxis.set_major_formatter(dates.DateFormatter('%H:%M'))
                else:
                    for ax in axes:
                        ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))

                if num_subplots > 0:
                    axes[-1].set_xlabel(x_dropdown_s.get())
                else:
                    ax.set_xlabel(x_dropdown_s.get())
                plt.xlabel(x_dropdown_s.get())
                for ax in axes:
                    ax.legend()
                plt.tight_layout()
                plt.show()
                       
        else:
            fig, ax = plt.subplots()     
            line = ax.plot(x_axis, y_axis, marker=',', label=y_dropdown_s.get())
            ax.set_xlabel(x_dropdown_s.get())
            ax.set_ylabel(y_dropdown_s.get())
            if status_dropdown_s_visible and status_dropdown_s.get() != '':
                nok_indicies = [i for i, status in enumerate(status_values) if status == 'NOK']
                nok_percentage = (len(nok_indicies)/len(y_axis))*100 if len(y_axis) > 0 else 0
                ax.scatter([x_axis[i] for i in nok_indicies], [y_axis[i] for i in nok_indicies], color = "red", marker='o', label = f'Link Outage ({nok_percentage:.4f}%)')
                ax.set_title(f"Flight Date: {flight_msn_date}\n {x_dropdown_s.get()} vs {y_dropdown_s.get()} with {status_name}")
                mplcursors.cursor(line, multiple = True).connect("add", show_annotations)
            else:
                ax.set_title(f"Flight Date: {flight_msn_date}\n {x_dropdown_s.get()} vs {y_dropdown_s.get()}")
                mplcursors.cursor(line, multiple = True)
            ax.scatter(lon_gcs, lat_gcs, marker='s', color='#00ffff')
            ax.scatter(lon_gdt2, lat_gdt2, marker='s', color='#000000')
            if all(isinstance(val, datetime) for val in x_axis):
                ax.xaxis.set_major_formatter(dates.DateFormatter('%H:%M'))
            else:
                ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
            
            ax.legend()
            plt.grid(True)
            plt.show()

def special_plotter_fnc():

     #### First File ############################################
    x1 = globals().get(x_dropdown.get().lower())
    y1 = globals().get(y_dropdown.get().lower())
    if y_dropdown_2_visible:
        y1_2 = globals().get(y_dropdown_2.get().lower())
    if y_dropdown_3_visible:
        y1_3 = globals().get(y_dropdown_3.get().lower())

    if y1 and callable(y1) and x1 and callable(x1):
        x_axis_1 = x1(file_path)
        y_axis_1 = y1(file_path)
        if y_dropdown_2_visible:
            if y1_2 and callable(y1_2):
                y_axis_1_2 = y1_2(file_path)
        if y_dropdown_3_visible:
            if y1_3 and callable(y1_3):
                y_axis_1_3 = y1_3(file_path)

        start_index = 0
        for i in range(len(y_axis_1)):
            if y_axis_1[i] != 0:
                start_index = i
                break
        stop_index = len(x_axis_1)

        x_axis_1 = x_axis_1[start_index:stop_index]
        y_axis_1 = y_axis_1[start_index:stop_index]
        if y_dropdown_2_visible:
            y_axis_1_2 = y_axis_1_2[start_index:stop_index]
        if y_dropdown_3_visible:
            y_axis_1_3 = y_axis_1_3[start_index:stop_index]

 #### Second File ############################################
    x2 = globals().get(x_dropdown_s.get().lower())
    y2 = globals().get(y_dropdown_s.get().lower())
    if y_dropdown_2_s_visible:
        y2_2 = globals().get(y_dropdown_2_s.get().lower())
    if y_dropdown_3_s_visible:
        y2_3 = globals().get(y_dropdown_3_s.get().lower())

    if y2 and callable(y2) and x2 and callable(x2):
        x_axis_2 = x2(file_path_s)
        y_axis_2 = y2(file_path_s)
        if y_dropdown_2_s_visible:
            if y2_2 and callable(y2_2):
                y_axis_2_2 = y2_2(file_path_s)
        if y_dropdown_3_s_visible:
            if y2_3 and callable(y2_3):
                y_axis_2_3 = y2_3(file_path_s)

        start_index_2 = 0
        for j in range(len(y_axis_2)):
            if y_axis_2[j] != 0:
                start_index_2 = j
                break
        stop_index_2 = len(x_axis_2)

        x_axis_2 = x_axis_2[start_index_2:stop_index_2]
        y_axis_2 = y_axis_2[start_index_2:stop_index_2]
        if y_dropdown_2_s_visible:
            y_axis_2_2 = y_axis_2_2[start_index_2:stop_index_2]
        if y_dropdown_3_s_visible:
            y_axis_2_3 = y_axis_2_3[start_index_2:stop_index_2]

        subplot_cnt = 0

        if compare_primary_secondary_on:
            subplots_num = 2
            if y_dropdown_2_visible:
                subplots_num += 1
            if y_dropdown_3_visible:
                subplots_num += 1
            if y_dropdown_2_s_visible:
                subplots_num += 1
            if y_dropdown_3_s_visible:
                subplots_num += 1

            fig, axes = plt.subplots(subplots_num,1, sharex=True)
            line_1 = axes[0].plot(x_axis_1, y_axis_1, marker = ',', label = f'MAIN - {y_dropdown.get()}')
            axes[0].scatter(x_axis_1[0], y_axis_1[0], marker = 'D', color = 'green')
            axes[0].scatter(x_axis_1[-1], y_axis_1[-1], marker = 'd', color = 'black')
            mplcursors.cursor(line_1, multiple = True)
            axes[0].grid(True)
            axes[0].legend()
            axes[0].set_xlabel(x_dropdown.get())
            axes[0].set_ylabel(y_dropdown.get())
            subplot_cnt += 1

            if y_dropdown_2_visible:
                line_3 = axes[subplot_cnt].plot(x_axis_1, y_axis_1_2, marker = ',', label = f'MAIN - {y_dropdown_2.get()}')
                axes[subplot_cnt].scatter(x_axis_1[0], y_axis_1_2[0], marker = 'D', color = 'green')
                axes[subplot_cnt].scatter(x_axis_1[-1], y_axis_1_2[-1], marker = 'd', color = 'black')
                mplcursors.cursor(line_3, multiple = True)
                axes[subplot_cnt].grid(True)
                axes[subplot_cnt].legend()
                axes[subplot_cnt].set_xlabel(x_dropdown.get())
                axes[subplot_cnt].set_ylabel(y_dropdown_2.get())
                subplot_cnt += 1

            if y_dropdown_3_visible:
                line_5 = axes[subplot_cnt].plot(x_axis_1, y_axis_1_3, marker = ',', label = f'MAIN - {y_dropdown_3.get()}')
                axes[subplot_cnt].scatter(x_axis_1[0], y_axis_1_3[0], marker = 'D', color = 'green')
                axes[subplot_cnt].scatter(x_axis_1[-1], y_axis_1_3[-1], marker = 'd', color = 'black')
                mplcursors.cursor(line_5, multiple = True)
                axes[subplot_cnt].grid(True)
                axes[subplot_cnt].legend()
                axes[subplot_cnt].set_xlabel(x_dropdown.get())
                axes[subplot_cnt].set_ylabel(y_dropdown_3.get())
                subplot_cnt += 1

            line_2 = axes[subplot_cnt].plot(x_axis_2, y_axis_2, marker = ',', label = f'STNDBY - {y_dropdown_s.get()}')
            axes[subplot_cnt].scatter(x_axis_2[0], y_axis_2[0], marker = 'D', color='green')
            axes[subplot_cnt].scatter(x_axis_2[-1], y_axis_2[-1], marker='d', color='black')
            mplcursors.cursor(line_2, multiple= True)
            axes[subplot_cnt].grid(True)
            axes[subplot_cnt].legend()
            axes[subplot_cnt].set_xlabel(x_dropdown_s.get())
            axes[subplot_cnt].set_ylabel(y_dropdown_s.get())
            subplot_cnt += 1

            if y_dropdown_2_s_visible:
                line_4 = axes[subplot_cnt].plot(x_axis_2, y_axis_2_2, marker = ',', label = f'STNDBY - {y_dropdown_2_s.get()}')
                axes[subplot_cnt].scatter(x_axis_2[0], y_axis_2_2[0], marker = 'D', color = 'green')
                axes[subplot_cnt].scatter(x_axis_2[-1], y_axis_2_2[-1], marker = 'd', color = 'black')
                mplcursors.cursor(line_4, multiple = True)
                axes[subplot_cnt].grid(True)
                axes[subplot_cnt].legend()
                axes[subplot_cnt].set_xlabel(x_dropdown.get())
                axes[subplot_cnt].set_ylabel(y_dropdown_2_s.get())
                subplot_cnt += 1

            if y_dropdown_3_s_visible:
                line_6 = axes[subplot_cnt].plot(x_axis_2, y_axis_2_3, marker = ',', label = f'STNDBY - {y_dropdown_3_s.get()}')
                axes[subplot_cnt].scatter(x_axis_2[0], y_axis_2_3[0], marker = 'D', color = 'green')
                axes[subplot_cnt].scatter(x_axis_2[-1], y_axis_2_3[-1], marker = 'd', color = 'black')
                mplcursors.cursor(line_6, multiple = True)
                axes[subplot_cnt].grid(True)
                axes[subplot_cnt].legend()
                axes[subplot_cnt].set_xlabel(x_dropdown.get())
                axes[subplot_cnt].set_ylabel(y_dropdown_3_s.get())
                     
            if all(isinstance(val, datetime) for val in x_axis_1 and x_axis_2):
                axes[0].xaxis.set_major_formatter(dates.DateFormatter('%H:%M:%S'))
                axes[1].xaxis.set_major_formatter(dates.DateFormatter('%H:%M:%S'))
            else:
                axes[0].xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
                axes[1].xaxis.set_major_formatter(FormatStrFormatter('%.2f'))

        else:
            fig,ax = plt.subplots()
            line_3 = ax.plot(x_axis_1, y_axis_1, marker=',', label = f'Primary - {y_dropdown.get()}')
            ax.scatter(x_axis_1[0], y_axis_1[0], marker='D', color = 'green')
            ax.scatter(x_axis_1[-1], y_axis_1[-1], marker='d', color='black')
            mplcursors.cursor(line_3, multiple=True)

            line_4 = ax.plot(x_axis_2, y_axis_2, marker=',', label=f'Secondary - {y_dropdown_s.get()}')
            ax.scatter(x_axis_2[0], y_axis_2[0], marker='D', color='green')
            ax.scatter(x_axis_2[-1], y_axis_2[-1], marker='d', color='black')
            mplcursors.cursor(line_4, multiple=True)
            if all(isinstance(val, datetime) for val in x_axis_1 and x_axis_2):
                ax.xaxis.set_major_formatter(dates.DateFormatter('%H:%M'))
            else:
                ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
            ax.grid(True)
            ax.legend()
    plt.tight_layout()
    plt.show()

def loss_table():
    try:
        lat = []
        uhf_upl = []
        c_upl = []
        sat_upl = []
        all_upl = []
        
        c_dnl = []
        sat_dnl = []
        all_dnl = []
        
        lat = lat
        uhf_upl = uhf_upl
        c_upl = c_upl
        sat_upl = sat_upl
        all_upl = all_upl
        
        c_dnl = c_dnl
        sat_dnl = sat_dnl
        all_dnl = all_dnl
        
        uhf_upl_indicies = [i for i, status in enumerate(uhf_upl) if status == "NOK"]
        uhf_upl_percentage = len(uhf_upl_indicies)/len(lat)*100
        
        c_upl_indicies = [i for i, status in enumerate(c_upl) if status == "NOK"]
        c_upl_percentage = len(c_upl_indicies)/len(lat)*100
        
        sat_upl_indicies = [i for i, status in enumerate(sat_upl) if status == "NOK"]
        sat_upl_percentage = len(sat_upl_indicies)/len(lat)*100
        
        all_upl_indicies = [i for i, status in enumerate(all_upl) if status == "NOK"]
        all_upl_percentage = len(all_upl_indicies)/len(lat)*100
        
        c_dnl_indicies = [i for i, status in enumerate(c_dnl) if status == "NOK"]
        c_dnl_percentage = len(c_dnl_indicies)/len(lat)*100
        
        sat_dnl_indicies = [i for i, status in enumerate(sat_dnl) if status == "NOK"]
        sat_dnl_percentage = len(sat_dnl_indicies)/len(lat)*100
        
        all_dnl_indicies = [i for i, status in enumerate(all_dnl) if status == "NOK"]
        all_dnl_percentage = len(all_dnl_indicies)/len(lat)*100

        table_window = ttk.Toplevel(root)
        table = ttk.Treeview(table_window, columns=("Column 1", "Column 2"), show='headings')

        table.heading("Column 1", text="LINK TYPE")
        table.heading("Column 2", text="LOSS %")
        
        table.insert("", "end", values=("UHF UPLINK", f"{uhf_upl_percentage:.2f} %"))
        table.insert("", "end", values=("C UPLINK", f"{c_upl_percentage:.2f} %"))
        if sat_upl_percentage < 100:
            table.insert("", "end", values=("SAT UPLINK", f"{sat_upl_percentage:.2f} %"))
        else:
            pass
        table.insert("", "end", values=("OverAll  UPLINK", f"{all_upl_percentage:.2f} %"))

        table.insert("", "end", values=("C DOWNLINK", f"{c_dnl_percentage:.2f} %"))
        if sat_upl_percentage < 100:
            table.insert("", "end", values=("SAT DOWNLINK", f"{sat_dnl_percentage:.2f} %"))
        else:
            pass
        table.insert("", "end", values=("OverAll DOWNLINK", f"{all_dnl_percentage:.2f} %"))

        table.pack()
    except NameError:
        messagebox.showerror("Error", "Please Select a valid flight Data!!")
        

def loss_table_s():
    try :
        lat = []
        uhf_upl = []
        c_upl = []
        sat_upl = []
        all_upl = []
        
        c_dnl = []
        sat_dnl = []
        all_dnl = []
        
        lat = lat
        uhf_upl = uhf_upl
        c_upl = c_upl
        sat_upl = sat_upl
        all_upl = all_upl
        
        c_dnl = c_dnl
        sat_dnl = sat_dnl
        all_dnl = all_dnl
        
        uhf_upl_indicies = [i for i, status in enumerate(uhf_upl) if status == "NOK"]
        uhf_upl_percentage = len(uhf_upl_indicies)/len(lat)*100
        
        c_upl_indicies = [i for i, status in enumerate(c_upl) if status == "NOK"]
        c_upl_percentage = len(c_upl_indicies)/len(lat)*100
        
        sat_upl_indicies = [i for i, status in enumerate(sat_upl) if status == "NOK"]
        sat_upl_percentage = len(sat_upl_indicies)/len(lat)*100
        
        all_upl_indicies = [i for i, status in enumerate(all_upl) if status == "NOK"]
        all_upl_percentage = len(all_upl_indicies)/len(lat)*100
        
        c_dnl_indicies = [i for i, status in enumerate(c_dnl) if status == "NOK"]
        c_dnl_percentage = len(c_dnl_indicies)/len(lat)*100
        
        sat_dnl_indicies = [i for i, status in enumerate(sat_dnl) if status == "NOK"]
        sat_dnl_percentage = len(sat_dnl_indicies)/len(lat)*100
        
        all_dnl_indicies = [i for i, status in enumerate(all_dnl) if status == "NOK"]
        all_dnl_percentage = len(all_dnl_indicies)/len(lat)*100

        table_window = ttk.Toplevel(root)
        table = ttk.Treeview(table_window, columns=("Column 1", "Column 2"), show='headings')

        table.heading("Column 1", text="LINK TYPE")
        table.heading("Column 2", text="LOSS %")
        
        table.insert("", "end", values=("UHF UPLINK", f"{uhf_upl_percentage:.2f} %"))
        table.insert("", "end", values=("C UPLINK", f"{c_upl_percentage:.2f} %"))
        if sat_upl_percentage < 100:
            table.insert("", "end", values=("SAT UPLINK", f"{sat_upl_percentage:.2f} %"))
        else:
            pass
        table.insert("", "end", values=("OverAll  UPLINK", f"{all_upl_percentage:.2f} %"))

        table.insert("", "end", values=("C DOWNLINK", f"{c_dnl_percentage:.2f} %"))
        if sat_upl_percentage < 100:
            table.insert("", "end", values=("SAT DOWNLINK", f"{sat_dnl_percentage:.2f} %"))
        else:
            pass
        table.insert("", "end", values=("OverAll DOWNLINK", f"{all_dnl_percentage:.2f} %"))

        table.pack()
    except NameError:
        messagebox.showerror("Error", "Please Select a valid flight Data!!")



# main window ###################################
root = ttk.Window()
root.state('zoomed')
root.iconbitmap(r'logo.ico')
root.title("")
logo = tkinter.PhotoImage(file='logo.png')

# Frame ################################################
top_frame = ttk.Frame(root)
left_frame = ttk.Frame(root)
right_frame = ttk.Frame(root)
bottom_frame = ttk.Frame(root)

# widgets #############################################
title = ttk.Label(top_frame, text="Post Flight Analysis",image=logo, compound='top' , font="calibri 35 bold", bootstyle = "warning")

# Left Frame widgets ##########################################
gcs_label = ttk.Label(left_frame, text="Telemetry Analysis-I", font="aerial 20 bold", bootstyle = "warning")
load_file = ttk.Button(left_frame, text="Select Flight Data", command=browse_file, bootstyle = 'primary outline')
file_label = ttk.Label(left_frame, text="Select File : Select Bin File Data", font="calibri 12 bold", bootstyle = 'primary')
x_label = ttk.Label(left_frame,font="bold", text="Select X Axis: ", bootstyle = "primary")
x_dropdown = ttk.Combobox(left_frame, width=30, bootstyle = "primary")
y_label = ttk.Label(left_frame, font="bold", text="Select Y Axis: ", bootstyle = "primary")
y_dropdown = ttk.Combobox(left_frame, width=30, bootstyle = "primary")
y_dropdown_2_toggle = ttk.Button(left_frame, text="➕",command=y_2_toggle, bootstyle = "success outline")
y_dropdown_3_toggle = ttk.Button(left_frame, text="➕",command=y_3_toggle, bootstyle = "success outline")
y_dropdown_4_toggle = ttk.Button(left_frame, text="➕",command=y_4_toggle, bootstyle = "success outline")
y_dropdown_2 = ttk.Combobox(left_frame, width=30, bootstyle = "primary")
y_dropdown_3 = ttk.Combobox(left_frame, width=30, bootstyle = "primary")
y_dropdown_4 = ttk.Combobox(left_frame, width=30, bootstyle = "primary")
status_dropdown_toggle = ttk.Button(left_frame, text="Show Status Dropdown",command=status_toggle, bootstyle = "warning outline")
status_dropdown = ttk.Combobox(left_frame, width=30, bootstyle = "warning")
combine_plots = ttk.Checkbutton(left_frame, text="Combine Subplots",command=combine_subplots, state="disabled", bootstyle = "danger-round-toggle")
function_button = ttk.Button(left_frame, text="Plot",state='disabled', command=function_btn, bootstyle = "danger outline")
function_3d = ttk.Button(left_frame, text="3D Plotter", bootstyle = 'success outline', command=func_3d)

frame_label = ttk.LabelFrame(left_frame, text="Preset Plotting", bootstyle = 'danger')
uhf_link_preset = ttk.Button(frame_label, text= "UHF Link Status", bootstyle = 'primary outline', command=uhf_plot)
c_link_preset = ttk.Button(frame_label, text="C Link Status", bootstyle = 'primary outline', command=c_plot)
sat_link_preset = ttk.Button(frame_label, text="SAT Link Status", bootstyle = 'primary outline', command=sat_plot)
cmd_link_preset = ttk.Button(frame_label, text="CMD Link Status", bootstyle = 'primary outline', command=cmd_plot)
summary_preset = ttk.Button(frame_label, text="Link Summary", bootstyle = 'primary outline', command=loss_table)

# Right Frame Widgets #####################################################################
flydaq_label = ttk.Label(right_frame, text="Telemetry Analysis-II", font="aerial 20 bold", bootstyle = "warning")
load_file_s = ttk.Button(right_frame, text="Select Flight Data", command=browse_file_s, bootstyle = 'primary outline')
file_label_s = ttk.Label(right_frame, text="Select File : Select Bin Flight Data", font='calibri 12 bold', bootstyle = 'primary')
x_label_s = ttk.Label(right_frame,font="bold", text="Select X Axis: ", bootstyle = "primary")
x_dropdown_s = ttk.Combobox(right_frame, width=30, bootstyle = "primary")
y_label_s = ttk.Label(right_frame, font="bold", text="Select Y Axis: ", bootstyle = "primary")
y_dropdown_s = ttk.Combobox(right_frame, width=30, bootstyle = "primary")
y_dropdown_2_toggle_s = ttk.Button(right_frame, text="➕",bootstyle = "success outline", command=y_2_s_toggle)
y_dropdown_3_toggle_s = ttk.Button(right_frame, text="➕",bootstyle = "success outline", command=y_3_s_toggle)
y_dropdown_4_toggle_s = ttk.Button(right_frame, text="➕", bootstyle = "success outline", command=y_4_s_toggle)
y_dropdown_2_s = ttk.Combobox(right_frame, width=30, bootstyle = "primary")
y_dropdown_3_s = ttk.Combobox(right_frame, width=30, bootstyle = "primary")
y_dropdown_4_s = ttk.Combobox(right_frame, width=30, bootstyle = "primary")
status_dropdown_toggle_s = ttk.Button(right_frame, text="Show Status Dropdown",bootstyle = "warning outline", command=status_s_toggle)
status_dropdown_s = ttk.Combobox(right_frame, width=30, bootstyle = "warning")
combine_plots_s = ttk.Checkbutton(right_frame, text="Combine Subplots",command=combine_subplots_s, state="disabled", bootstyle = "danger-round-toggle")
function_button_s = ttk.Button(right_frame, text="Plot",state='disabled',command=function_btn_s, bootstyle = "danger outline")
function_3d_s  = ttk.Button(right_frame, text="3D Plotter", bootstyle = 'success outline', command=func_3d_s)

frame_label_s = ttk.Labelframe(right_frame, text="Preset Plotting", bootstyle = 'danger')
uhf_link_preset_s = ttk.Button(frame_label_s, text="UHF Link Status", bootstyle = 'primary outline', command=uhf_plot_s)
c_link_preset_s = ttk.Button(frame_label_s, text="C Link Status", bootstyle = 'primary outline', command=c_plot_s)
sat_link_preset_s = ttk.Button(frame_label_s, text="SAT Link Status", bootstyle = 'primary outline', command=sat_plot_s)
cmd_link_preset_s = ttk.Button(frame_label_s, text="CMD Link Status", bootstyle = 'primary outline', command=cmd_plot_s)
summary_preset_s = ttk.Button(frame_label_s, text="Link Summary", bootstyle = 'primary outline', command=loss_table_s)

# Bottom Frame ###################################################################################
combine_primary_secondary = ttk.Checkbutton(bottom_frame, text="Combine Primary and Secondary Plots",command=combine_pri_sec, bootstyle = "warning-round-toggle")
compare_primary_secondary = ttk.Checkbutton(bottom_frame, text="Compare Primary and Secondary Plots",command=compare_pri_sec, bootstyle = "warning-round-toggle")
special_plotter = ttk.Button(bottom_frame, text="Special Plotter",state='disabled', bootstyle = "warning outline", command=special_plotter_fnc)

# Pack Widgets ##############################################
title.grid(columnspan=2, padx=10, pady=15)

# Frame Packings #######################################
top_frame.pack()
bottom_frame.pack(side='bottom', padx=15, anchor="center")
left_frame.pack(side="left", padx=15, anchor="center", fill="y")
right_frame.pack(side="right", padx=15, anchor="center", fill="y")

 #left frame ##########################################################
gcs_label.grid(row=0, columnspan=2, padx=15, pady=15)
load_file.grid(row=1, column=0, padx=15, pady=10)
file_label.grid(row=1, column=1, padx=15, pady=10)
x_label.grid(row=2, column=0, padx=15, pady=5)
x_dropdown.grid(row=3, column=0, padx=15, pady=5)
y_label.grid(row=2, column=1, padx=15, pady=5)
y_dropdown.grid(row=3, column=1, padx=15, pady=5)
y_dropdown_2_toggle.grid(row=4, column=1, padx=15, pady=5)
y_dropdown_3_toggle.grid(row=5, column=1, padx=15, pady=5)
y_dropdown_4_toggle.grid(row=6, column=1, padx=15, pady=5)
status_dropdown_toggle.grid(row=7, columnspan=2, padx=5, pady=5)
combine_plots.grid(row=8, columnspan=2, padx=5, pady=5)
function_button.grid(columnspan=2, padx=5, pady=10, sticky="nesw")
function_3d.grid(columnspan=2, padx=5, pady=5, sticky='nesw')

frame_label.grid(columnspan=2, padx=10, pady=10)

uhf_link_preset.grid(row=0, column=0, padx=5, pady=5)
c_link_preset.grid(row=0, column=1, padx=5, pady=5)
sat_link_preset.grid(row=0, column=2, padx=5, pady=5)
cmd_link_preset.grid(row=0, column=3, padx=5, pady=5)
summary_preset.grid(row=1, columnspan=4, padx=5, pady=5)

# Right Frame Packings #################################################################################################
flydaq_label.grid(row=0, columnspan=2, padx=15, pady=15)
load_file_s.grid(row=1, column=0, padx=15, pady=10)
file_label_s.grid(row=1, column=1, padx=15, pady=10)
x_label_s.grid(row=2, column=0, padx=15, pady=5)
x_dropdown_s.grid(row=3, column=0, padx=15, pady=5)
y_label_s.grid(row=2, column=1, padx=15, pady=5)
y_dropdown_s.grid(row=3, column=1, padx=15, pady=5)
y_dropdown_2_toggle_s.grid(row=4, column=1, padx=15, pady=5)
y_dropdown_3_toggle_s.grid(row=5, column=1, padx=15, pady=5)
y_dropdown_4_toggle_s.grid(row=6, column=1, padx=15, pady=5)
status_dropdown_toggle_s.grid(row=7, columnspan=2, padx=5, pady=5)
combine_plots_s.grid(columnspan=2, padx=5, pady=5)
function_button_s.grid(columnspan=2, padx=5, pady=10, sticky="nesw")
function_3d_s.grid(columnspan=2, padx=5, pady=5, sticky='nesw')
frame_label_s.grid(columnspan=2, padx=10, pady=10)

uhf_link_preset_s.grid(row=0, column=0, padx=5, pady=5)
c_link_preset_s.grid(row=0, column=1, padx=5, pady=5)
sat_link_preset_s.grid(row=0, column=2, padx=5, pady=5)
cmd_link_preset_s.grid(row=0, column=3, padx=5, pady=5)
summary_preset_s.grid(row=1, columnspan=4, padx=5, pady=5)
# Bottom Frame Packing ##########################################################################
combine_primary_secondary.grid(row=0, column=0, padx=10, pady=10)
compare_primary_secondary.grid(row=0, column=1, padx=10, pady=10)
special_plotter.grid(columnspan=2, padx=15, pady=15, sticky='nesw')

# root main loop ###########################
root.mainloop()