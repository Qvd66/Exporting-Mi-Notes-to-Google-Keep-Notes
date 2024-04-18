import time
import pyautogui

# Function to create notes in Google Keep
def create_notes(notes):
    # Press Windows key to open Start menu
    pyautogui.press('win')
    time.sleep(1)

    # Type 'Google Keep' to search for it in Start menu
    pyautogui.write('Google Keep')
    time.sleep(1)

    # Press Enter to open Google Keep
    pyautogui.press('enter')
    time.sleep(3)

    # Loop through each note content and create a new note in Google Keep
    for note_content in notes:
        # Create a new note
        pyautogui.hotkey('alt', 'enter')  # Use 'Ctrl + n' to create a new note
        time.sleep(1)

        # Type note content
        pyautogui.write(note_content)
        time.sleep(1)

        # Save the note
        pyautogui.hotkey('ctrl', 'enter')  # Use 'Ctrl + s' to save the note
        time.sleep(1)

   # Function to extract notes from the file
def extract_notes(file_path):
    encodings = ['utf-8', 'cp1252', 'latin-1']  # Add more as necessary
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                content = file.read()
            # Split content into notes using '=======\n' as delimiter and reverse the order
            notes = content.split('=======\n')[1:-1]
            return notes[::-1]  # Reverse the order of notes
        except UnicodeDecodeError:
            continue
    # If none of the encodings work
    print("Failed to decode the file using any of the specified encodings.")

# Example usage
if __name__ == "__main__":
    file_path = 'C:/Users/qvd66/Desktop/a/test.txt'  # Update with your file path
    notes = extract_notes(file_path)
    create_notes(notes)
