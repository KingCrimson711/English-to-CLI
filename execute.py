import os
import ollama

def read_transcription_file(filename="transcription.txt"):
    with open(filename, "r") as file:
        return file.read().strip()

def get_command_from_ollama(transcription):
    prompt = f"Convert the following user request into a Linux terminal command:\n'{transcription}'\nOnly return the command without any explanations."
    
    response = ollama.chat(
        model="llama3",  # Using the correct model
        messages=[{"role": "user", "content": prompt}]
    )

    command = response['message']['content'].strip()
    return command

def execute_command(command):
    print(f"Executing: {command}")
    os.system(command)

if __name__ == "__main__":
    transcription = read_transcription_file("transcription.txt")
    print(f"Transcription: {transcription}")
    
    try:
        command = get_command_from_ollama(transcription)
        print(f"Generated Command: {command}")

        with open("command.txt", "w") as file:
            file.write(command)

        execute_command(command)
    except Exception as e:
        print(f"Error: {e}")
