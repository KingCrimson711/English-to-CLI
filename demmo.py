import whisper
import pyaudio
import wave

# Function to record audio from the microphone
def record_audio(filename="audio.wav", duration=5):
    p = pyaudio.PyAudio()

    # Set audio format and parameters
    rate = 16000  # Sample rate
    channels = 1  # Mono audio
    frames_per_buffer = 1024
    format = pyaudio.paInt16

    # Open the audio stream
    stream = p.open(format=format, channels=channels,
                    rate=rate, input=True,
                    frames_per_buffer=frames_per_buffer)

    print("Recording...")

    frames = []
    for i in range(0, int(rate / frames_per_buffer * duration)):
        data = stream.read(frames_per_buffer)
        frames.append(data)

    print("Recording finished.")
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recorded audio as a .wav file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))

# Function to transcribe audio using Whisper
def transcribe_audio(audio_file):
    model = whisper.load_model("base")  # Load Whisper model (base is a good option for speed)
    result = model.transcribe(audio_file)
    return result["text"]

# Main program to record and transcribe
if __name__ == "__main__":
    # Record audio (you can adjust duration if needed)
    record_audio("audio.wav", duration=5)

    # Transcribe the recorded
    # 
    # 
    # audio
    transcription = transcribe_audio("audio.wav")

    print("Transcription: ", transcription)

    with open("transcription.txt", "w") as file:
        file.write(transcription)
    print("Transcription saved to 'transcription.txt'")
