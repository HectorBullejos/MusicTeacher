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
                  'C': 0.5, 'D': 1, 'E': 1.5, 'F': 2, 'G': 2.5, 'A': 3}  # Correct this to have unique keys if needed

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

def on_button_clicked(note):
    def button_callback(event):
        global user_answer
        user_answer = note
        plt.close()
    return button_callback

def show_feedback(correct, note_name):
    # Create a new figure for feedback
    fig_feedback, ax_feedback = plt.subplots()
    plt.axis('off')  # Hide axes
    feedback_text = "Correcto!" if correct else f"Incorrecto. Era: {note_name}"
    ax_feedback.text(0.5, 0.5, feedback_text, ha='center', va='center', fontsize=16, transform=ax_feedback.transAxes)
    plt.show(block=False)
    plt.pause(0.7)  # Display feedback for 2 seconds
    plt.close(fig_feedback)  # Close the feedback figure



def show_random_notes(num_notes):
    for _ in range(num_notes):
        global user_answer
        user_answer = None  # Reset the user answer for each note
        note = random.choice(list(note_positions.keys()))
        weights = [1, 1, 1, 1, 1, 2, 2]  # Example weights, adjust as needed

        note = random.choices(notes, weights=weights, k=1)[0]
        print(note)
        note_name = note_mapping[note]

        fig, ax = plt.subplots(figsize=(6, 6))
        plt.subplots_adjust(bottom=0.2)
        ax.set_xlim(-3, 3)
        ax.set_ylim(-6, 6)
        ax.axis('off')
        draw_staff(ax)
        draw_treble_clef(ax)
        draw_note(ax, note)

        # Create buttons for each note
        button_axes = [plt.axes([0.75, 0.03 * (i + 1) + 0.03 * (i + 10), 0.05, 0.04]) for i in range(len(notes_Es))]
        buttons = [Button(ax, label) for ax, label in zip(button_axes, notes_Es)]

        for button, note_es in zip(buttons, notes_Es):
            button.on_clicked(on_button_clicked(note_es))

        plt.show(block=True)  # Show plot and wait for it to be closed

        # After plot is closed, check the answer and show feedback
        correct = user_answer == note_name
        show_feedback(correct, note_name)

number = 10

# Show the notes
number = input("cuantas notas quieres hacer ?")
tiempo_de = input("cuanta velocidad de muestra en segundos (recomendable: 1) ?")
show_random_notes(int(number))


