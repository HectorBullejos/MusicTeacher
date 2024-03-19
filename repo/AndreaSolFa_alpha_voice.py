import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import random
import time
import speech_recognition as sr

# Define notes in the treble clef
notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
notes_Es = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si']
note_mapping = dict(zip(notes, notes_Es))
note_positions = {'G': -1, 'A': -0.5, 'B': 0, 'C': 0.5, 'D': 1, 'E': 1.5, 'F': 2}


# Speech recognition functions and settings
def recognize_speech_from_mic(recognizer, microphone):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Por favor, diga el nombre de la nota ...")
        audio = recognizer.listen(source)

    try:
        transcription = recognizer.recognize_google(audio, language="es-ES").lower()
        print(transcription)
        return transcription
    except sr.RequestError:
        print("API unavailable")
    except sr.UnknownValueError:
        print("Unable to recognize speech")
    return ""


def draw_staff(ax):
    for i in range(-2, 3):
        ax.axhline(i, color='black', lw=3, xmin=0.2, xmax=0.8)


def draw_note(ax, note):
    y_pos = note_positions[note]
    circle = plt.Circle((0.5, y_pos), 0.2, color='black', zorder=1)
    ax.add_patch(circle)


def draw_treble_clef(ax):
    treble_clef = mpimg.imread('GCLEF3.png')
    ax.imshow(treble_clef, aspect='auto', extent=[-3.8, 0.4, -3, 3], zorder=1)


def show_random_notes(num_notes):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    for _ in range(num_notes):
        note = random.choice(list(note_positions.keys()))
        note_name = note_mapping[note]

        fig, ax = plt.subplots(figsize=(2, 6))
        ax.set_xlim(-3, 3)
        ax.set_ylim(-6, 6)
        ax.axis('off')
        draw_staff(ax)
        draw_treble_clef(ax)
        draw_note(ax, note)
        # plt.title(f"Nota: {note_name}", fontsize=16)
        plt.show()


        # Recognize speech
        attempt = recognize_speech_from_mic(recognizer, microphone)
        if note_name.lower() == attempt:
            print("Correcto, la nota que has dicho era: <", note_name.lower(), "> y era la nota correcta.")
        else:
            print(f"Incorrect. You said: {attempt}. Try again!")
            plt.close(fig)
            continue  # Skip closing the figure to retry

        # time.sleep(2)  # Adjust timing as needed
        # plt.close(fig)





show_random_notes(2)

