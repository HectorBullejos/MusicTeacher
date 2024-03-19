import speech_recognition as sr

# List of words to recognize
TARGET_WORDS = ["do", "re", "mi", "fa", "sol", "la", "si"]


def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`."""
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")
    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # Adjust the recognizer sensitivity to ambient noise and record audio
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Start speaking now...")
        audio = recognizer.listen(source)

    # Set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # Try recognizing the speech in the recording
    try:
        response["transcription"] = recognizer.recognize_google(audio, language="es-ES")
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # Speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response


if __name__ == "__main__":
    # Create recognizer and microphone instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    response = recognize_speech_from_mic(recognizer, microphone)

    if response["success"]:
        transcription = response["transcription"].lower()
        print(f"Transcription: {transcription}")
        # Check if any of the target words were said
        if any(word in transcription for word in TARGET_WORDS):
            print("Target word detected in the transcription.")
        else:
            print("No target words detected in the transcription.")
    else:
        print(f"Error: {response['error']}")
