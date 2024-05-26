import sys

try:
    import pyttsx3
except ImportError:
    print('The pyttsx3 module needs to be installed to run this')
    print('program. On Windows, open a Command Prompt and run:')
    print('pip install pyttsx3')
    print('On macOS and Linux, open a Terminal and run:')
    print('pip3 install pyttsx3')
    sys.exit()

tts = pyttsx3.init()  # Initialize the TTS engine.

print('ular melingkar diatas pagar')
print('ular nguar nguar ')
print('ular melingkar nguar nguar diatas pagar')
print('try those text in this code')
print()
print('Enter the text to speak, or QUIT to quit.')
while True:
    text = input('> ')

    if text.upper() == 'QUIT':
        print('Thanks for playing!')
        sys.exit()

    tts.say(text)  # Add some text for the TTS engine to say.
    tts.runAndWait()  # Make the TTS engine say it.
