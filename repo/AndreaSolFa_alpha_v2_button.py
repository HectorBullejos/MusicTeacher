import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.widgets import Button
import numpy as np
import random

# Define notes in the treble clef and other initializations
notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
notes_Es = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si']
note_mapping = dict(zip(notes, notes_Es))
note_positions = {'C': -3, 'D': -2.5, 'E': -2, 'F': -1.5, 'G': -1, 'A': -0.5, 'B': 0,
                  'C2': 0.5, 'D2': 1, 'E2': 1.5, 'F2': 2, 'G2': 2.5, 'A2': 3}
note_positions = {'C': -3, 'D': -2.5, 'E': -2, 'F': -1.5, 'G': -1, 'A': -0.5, 'B': 0,
                  'C': 0.5, 'D': 1, 'E': 1.5, 'F': 2, 'G': 2.5, 'A': 3}

def draw_staff(ax):
    for i in range(-2, 3):
        ax.axhline(i, color='black', lw=3, xmin=0.2, xmax=0.8)

def draw_note(ax, note):
    y_pos = note_positions[note]
    circle = plt.Circle((0.2, y_pos), 0.3, color='black', zorder=1)
    ax.add_patch(circle)

def draw_treble_clef(ax):
    treble_clef = mpimg.imread('GCLEF3.png')
    ax.imshow(treble_clef, aspect='auto', extent=[-3.8, 0.4, -4, 4], zorder=1)

# This variable is used to store the user's selected answer
user_answer = ""

def on_button_clicked(note):
    def button_callback(event):
        global user_answer
        user_answer = note
        plt.close()
    return button_callback

def show_random_notes(num_notes):
    for _ in range(num_notes):
        note = random.choice(list(note_positions.keys()))
        note_name = note_mapping[note]

        fig, ax = plt.subplots(figsize=(6, 6)) # x,y
        plt.subplots_adjust(bottom=0.2)
        ax.set_xlim(-3, 3)
        ax.set_ylim(-6, 6)
        ax.axis('off')
        draw_staff(ax)
        draw_treble_clef(ax)
        draw_note(ax, note)

        # Create buttons for each note
        # button_axes = [plt.axes([0.1, 0.05 * (i + 1), 0.08, 0.04]) for i in range(len(notes_Es))]
        note_positions_buttons = {'G': -1, 'A': -0.5, 'B': 0, 'C': 0.5, 'D': 1, 'E': 1.5, 'F': 2}  # Positions on the staff
        button_axes = [plt.axes([0.75, 0.03 * (i + 1) + 0.03 * (i + 10), 0.05, 0.04]) for i in range(len(note_positions_buttons))] # [a,b,c,d] [, , ancho del boton, altura del boton ]


        buttons = [Button(ax, label) for ax, label in zip(button_axes, notes_Es)]

        for button, note_es in zip(buttons, notes_Es):
            button.on_clicked(on_button_clicked(note_es))

        plt.show()

        # Check the user's answer after the plot window is closed
        correct_note_es = note_mapping[note]
        if user_answer == correct_note_es:
            print(f"Correct! The note was {correct_note_es}.")
        else:
            print(f"Incorrect. You selected {user_answer}; the correct note was {correct_note_es}. Try again!")
            continue  # Optionally, you could remove this to not retry on wrong answers


# Show the notes
show_random_notes(2)
