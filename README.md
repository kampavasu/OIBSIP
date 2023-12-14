# OIBSIP
## NAME:KAMPA VASU
## DOMAIN:PYTHON PROGRAMMING
# AIM:
The aim of this task is to create a basic voice assistant.

## DESCRIPTION:
This Python script is a simple voice-controlled assistant using the SpeechRecognition library (`speech_recognition`), text-to-speech conversion with the pyttsx3 library (`pyttsx3`), and basic datetime and web browsing functionalities.

Here's a breakdown of the script:

1. **Function Definitions:**
   - `greet()`: Returns a greeting message.
   - `get_time()`: Retrieves the current time and returns it as a string.
   - `get_date()`: Retrieves the current date and returns it as a string.
   - `search_web(query)`: Opens a web browser with a Google search for the specified query.

2. **Main Function (`main()`):**
   - Initializes the text-to-speech engine (`pyttsx3`) and the speech recognizer (`speech_recognition`).
   - Uses a `with` block to access the microphone as a source for audio input.
   - Greets the user and captures the user's voice command using the speech recognizer.
   - Processes the recognized command and performs actions based on the content of the command:
     - Greets the user if "hello" is in the command.
     - Retrieves and announces the current time if "time" is in the command.
     - Retrieves and announces the current date if "date" is in the command.
     - Performs a web search if the command contains "search," extracting the query and opening a Google search in the web browser.
     - Responds with a default message if the command is not recognized.
   - Handles exceptions, such as when the speech recognizer fails to understand the input or encounters a request error.

3. **Script Execution:**
   - The script initializes the assistant when executed, and the main function is called.

4. **Execution Flow:**
   - The assistant listens to the user, recognizes the speech, processes the command, and responds accordingly using text-to-speech.

5. **Usage:**
   - The user can run the script and interact with the assistant by speaking commands. The assistant performs actions based on the recognized commands, such as providing the time, date, greeting, or conducting a web search.


