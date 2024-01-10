# TTS
'''
* text_to_speech_24/text_to_speech(text)
                                    |       
                                    |        
                                     --- questions
                                     
pip install gtts
pip install playsound==1.2.2

'''

from gtts import gTTS
from presentation.FileErrorHandler import eraseTmpFile

def text_to_speech(text):
     eraseTmpFile()
     tts = gTTS(text=text, lang='ko')
     tts.save("media/tmp/question.mp3")