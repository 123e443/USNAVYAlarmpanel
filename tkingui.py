import tkinter as tk
import winsound
import os

# Absolute path to sound files
sound_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sounds")

Alarms = {
    "Surface Ship": {
        1: (os.path.join(sound_dir, "newgq1.wav"), "General Alarm", "#981A18"),  # Red
        2: (os.path.join(sound_dir, "chemalm.wav"), "Chemical Attack", "#5A926F"),  # Green
        3: (os.path.join(sound_dir, "colalm3a.wav"), "Collision Alarm", "#FFB000"),  # Yellow
        4: (os.path.join(sound_dir, "sonaralm.wav"), "Sonar Alarm", "#FFB000"),  # Yellow
        5: (os.path.join(sound_dir, "726ppalm"), "Power Plant Alarm", "#E9E9DF"),  # White
    },
    "Submarine": {
        1: (os.path.join(sound_dir, "newgq1.wav"), "General Alarm", "#FFB000"),  # Yellow
        2: (os.path.join(sound_dir, "colalm3a.wav"), "Collision Alarm", "#981A18"),  # Red
        3: (os.path.join(sound_dir, "k1.wav"), "Diving Alarm", "#5A926F"),  # Green
        4: (os.path.join(sound_dir, "726ppalm.wav"), "Power Plant Alarm", "#E9C9BE"),  # Pink
        5: (os.path.join(sound_dir, "726msljet.wav"), "Missile Jettison Alarm", "#005C86"),  # Blue
        6: (os.path.join(sound_dir, "726mslemerg.wav"), "Missile Emergency Alarm", "#D74D03"),  # Orange
    }
}
 
# Alarm files and names categorized by Surface Ship and Submarine with corresponding colors
Alarms = {
    "Surface Ship": {
        1: ("newgq1.wav", "General Alarm", "#981A18"),  # Red
        2: ("chemalm.wav", "Chemical Attack", "#5A926F"),  # Green
        3: ("colalm3a.wav", "Collision Alarm", "#FFB000"),  # Yellow
        4: ("sonaralm.wav", "Sonar Alarm", "#FFB000"),  # Yellow
        5: ("726ppalm", "Power Plant Alarm", "#E9E9DF"),  # White
    },
    "Submarine": {
        1: ("newgq1.wav", "General Alarm", "#FFB000"),  # Yellow
        2: ("colalm3a.wav", "Collision Alarm", "#981A18"),  # Red
        3: ("k1.wav", "Diving Alarm", "#5A926F"),  # Green
        4: ("726ppalm.wav", "Power Plant Alarm", "#E9C9BE"),  # Pink
        5: ("726msljet.wav", "Missile Jettison Alarm", "#005C86"),  # Blue
        6: ("726mslemerg.wav", "Missile Emergency Alarm", "#D74D03"),  # Orange
    }
}

# Current menu selection
current_menu = "Surface Ship"

def switch_menu(menu_name):
    """Switches between Surface Ship and Submarine menus."""
    global current_menu
    current_menu = menu_name
    update_buttons()

def play_sound(alarm_id):
    """Plays the selected alarm sound."""
    file_name, alarm_name, _ = Alarms[current_menu][alarm_id]
    print(f"Playing {alarm_name}. Press 'Stop' to stop early.")
    winsound.PlaySound(file_name, winsound.SND_FILENAME | winsound.SND_ASYNC)

def stop_sound():
    """Stops the currently playing sound."""
    winsound.PlaySound(None, winsound.SND_PURGE)
    print("Sound stopped.")

def update_buttons():
    """Updates the buttons to match the selected menu."""
    for widget in frame_buttons.winfo_children():
        widget.destroy()

    # Create buttons for the selected menu
    for key, value in Alarms[current_menu].items():
        button = tk.Button(frame_buttons, text=value[1], command=lambda k=key: play_sound(k), 
                           bg=value[2], fg="black", width=25, height=2)
        button.pack(pady=5)

    # Stop sound button
    stop_button = tk.Button(frame_buttons, text="Stop Sound", command=stop_sound, 
                            bg="gray", fg="white", width=25, height=2)
    stop_button.pack(pady=10)

# Creating the main window
root = tk.Tk()
root.title("Alarm System")
root.geometry("400x400")  # Set window size

# Menu selection buttons
frame_menu = tk.Frame(root)
frame_menu.pack(pady=10)

btn_surface = tk.Button(frame_menu, text="Surface Ship", command=lambda: switch_menu("Surface Ship"), 
                        bg="navy", fg="white", width=15, height=2)
btn_surface.pack(side=tk.LEFT, padx=10)

btn_submarine = tk.Button(frame_menu, text="Submarine", command=lambda: switch_menu("Submarine"), 
                          bg="darkred", fg="white", width=15, height=2)
btn_submarine.pack(side=tk.LEFT, padx=10)

# Frame to hold alarm buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

# Initialize buttons for the default menu
update_buttons()

# Run the Tkinter event loop
root.mainloop()