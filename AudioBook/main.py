import PyPDF2
import pyttsx3

# Open and read the PDF file
pdfReader = PyPDF2.PdfReader('Read.pdf')  # Assuming the PDF file is named 'Read.pdf' in the same directory

# Initialize the text-to-speech engine
speaker = pyttsx3.init()

# Text to be spoken
welcome_text = (
    "Welcome to the PDF reader created by Vidyan. "
    "Add your PDF in the same directory and name it as 'Read.pdf'. "
    "I will read it for you! I will start to read it now. Enjoy."
)

# Speak the welcome text
speaker.say(welcome_text)
speaker.runAndWait()

# Iterate through each page of the PDF
for page_num in range(len(pdfReader.pages)):
    # Extract text from the current page
    text = pdfReader.pages[page_num].extract_text()

    # Speak the extracted text
    speaker.say(text)

    # Wait for the speech to finish before moving to the next page
    speaker.runAndWait()

# Stop the text-to-speech engine
speaker.stop()

# Notify the end of reading
end_text = "I have finished reading the PDF. I hope you enjoyed it!"
speaker.say(end_text)
speaker.runAndWait()
