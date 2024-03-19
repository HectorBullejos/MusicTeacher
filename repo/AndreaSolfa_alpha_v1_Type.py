import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import random
import speech_recognition as sr

# Define notes in the treble clef
notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
notes_Es = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si']
note_mapping = dict(zip(notes, notes_Es))
note_positions = {'G': -1, 'A': -0.5, 'B': 0, 'C': 0.5, 'D': 1, 'E': 1.5, 'F': 2}
note_positions = {'C': -3,'D': -2.5,'E': -2,'F' :-1.5,'G': -1, 'A': -0.5, 'B': 0, 'C': 0.5, 'D': 1, 'E': 1.5, 'F': 2, 'G': 2.5, 'A': 3}

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
        plt.show(block=False)  # Show plot in a non-blocking manner

        plt.pause(3)  # Display the plot for 2 seconds
        plt.close(fig)  # Close the plot
        answer = input("¿Qué nota es?")
        # Recognize speech
        # attempt = recognize_speech_from_mic(recognizer, microphone)
        # if note_name.lower() == attempt:
        if note_name.lower() == answer:
            print("Correcto! La nota que has dicho era: <", note_name, "> y era la nota correcta.")
        else:
            # print(f"Incorrect. You said: {attempt}. Try again!")
            print(f"Incorrect. You said: {answer}. Try again!")
            continue  # Skip closing the figure to retry

show_random_notes(10)