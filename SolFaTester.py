import matplotlib.pyplot as plt
import numpy as np
import random
import time

# Define notes in the treble clef
notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
notes_Es = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si']
note_mapping = dict(zip(notes, notes_Es))
note_positions = {'C': -1, 'D': -0.5, 'E': 0, 'F': 0.5, 'G': 1, 'A': 1.5, 'B': 2}  # Positions on the staff
note_positions = {'G': -1, 'A': -0.5, 'B': 0, 'C': 0.5, 'D': 1, 'E': 1.5, 'F': 2}  # Positions on the staff


def draw_staff(ax):
    """Draw a simple staff."""
    for i in range(-2, 3):
        ax.axhline(i, color='black', lw=2)


def draw_note(ax, note):
    """Draw a note on the staff."""
    y_pos = note_positions[note]
    circle = plt.Circle((0.5, y_pos), 0.08, color='black')
    ax.add_patch(circle)
    # Add stem
    if y_pos < 1:
        ax.plot([0.5, 0.5], [y_pos + 0.2, y_pos + 1], color='black', lw=1)
    else:
        ax.plot([0.5, 0.5], [y_pos - 0.2, y_pos - 1], color='black', lw=1)


def show_random_notes(num_notes, delay=2):
    """Display random notes one by one."""
    for _ in range(num_notes):
        fig, ax = plt.subplots()

        # Set up the plot
        ax.set_xlim(0, 1)
        ax.set_ylim(-3, 3)
        ax.axis('off')
        draw_staff(ax)

        # Draw a random note
        note = random.choice(notes)
        draw_note(ax, note)
        plt.title(f"Note: {note_mapping[note]}")

        plt.show()
        # Pause between notes
        time.sleep(delay)
        plt.close(fig)


# Number of notes to display
num_notes = 2
show_random_notes(num_notes)

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
notes_Es = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si']