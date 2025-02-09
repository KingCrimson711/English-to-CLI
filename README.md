# English-to-CLI

## Author

Developed by [Srijan Sinha]([https://github.com/your-github-username](https://github.com/KingCrimson711))  
Feel free to contribute, suggest improvements, or report issues!

## 📌 About  
This project allows users to execute Linux terminal commands by speaking in natural language. It uses **Whisper** for speech-to-text and **Ollama (Llama3)** to convert transcriptions into valid terminal commands. The system then executes the generated commands, enabling a voice-controlled command-line interface.  

## ⚙️ Features  
- Converts spoken commands into terminal commands  
- Uses **Whisper** for speech recognition  
- Uses **Ollama (Llama3)** for converting text to terminal commands  
- Executes valid shell commands automatically  

## 🛠️ Requirements  
Make sure you have the following installed:  
- **Python 3.10+**  
- **Whisper** (for transcription)  
- **Ollama** (with **Llama3** model installed)  
- **PyAudio** (for recording)  

## 🚀 Setup & Installation  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-username/English-to-CLI.git
cd English-to-CLI
```

### 2️⃣ Create & Activate Virtual Environment  
```bash
python3 -m venv .venv  
source .venv/bin/activate  # For Mac & Linux
```

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4️⃣ Install Whisper & Ollama  
```bash
pip install openai-whisper  
brew install portaudio  # (Required for PyAudio on macOS)  
pip install pyaudio  
```

### 5️⃣ Download Llama3 Model for Ollama  
```bash
ollama pull llama3
```

## 🏃 Running the Project  
Run the script to start recording and executing commands:  
```bash
python3 execute.py
```

## 📝 Notes  
- The program records a short audio input and transcribes it  
- It converts transcriptions into valid terminal commands  
- Commands are executed only if they are safe (e.g., file creation, navigation)  

## 🐝 License  
This project is open-source and free to use.  

