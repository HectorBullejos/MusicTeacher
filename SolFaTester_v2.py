import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import random
import time

# Define notes in the treble clef
notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
notes_Es = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si']
note_mapping = dict(zip(notes, notes_Es))
note_positions = {'G': -1, 'A': -0.5, 'B': 0, 'C': 0.5, 'D': 1, 'E': 1.5, 'F': 2}

def draw_staff(ax):
    """Draw a simple staff."""
    for i in range(-2, 3):
        ax.axhline(i, color='black', lw=3, xmin=0.2, xmax=0.8)  # Narrow the staff)

def draw_note(ax, note):
    """Draw a note on the staff."""
    y_pos = note_positions[note]
    circle = plt.Circle((0.5, y_pos), 0.2, color='black', zorder=1)  # Ensure note is above the clef
    ax.add_patch(circle)


def draw_treble_clef(ax):
    """Draw the treble clef on the staff."""
    treble_clef = mpimg.imread('GCLEF3.png')
    ax.imshow(treble_clef, aspect='auto', extent=[-3.8, 0.4, -3, 3], zorder=1)  # Adjust as needed

def show_random_notes(num_notes, delay=2):
    """Display random notes one by one."""
    for _ in range(num_notes):
        fig, ax = plt.subplots(figsize=(2, 6))  # Adjust for thinner and taller plot

        # Set up the plot
        ax.set_xlim(-3, 3)  # Adjusted to accommodate treble clef
        ax.set_ylim(-6, 6)
        ax.axis('off')

        draw_staff(ax)
        draw_treble_clef(ax)

        # Draw a random note
        note = random.choice(list(note_positions.keys()))
        draw_note(ax, note)
        plt.title(f"Nota: {note_mapping[note]}", fontsize=16)

        plt.show()
        # Pause between notes
        time.sleep(delay)
        plt.close(fig)

# Number of notes to display
num_notes = 2
show_random_notes(num_notes)
