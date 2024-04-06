from fastapi import FastAPI
from pydantic import BaseModel
import os
import shutil
import moviepy.editor as mp 
import speech_recognition as sr 


def extract_transcript(videoPath: str):
    video = mp.VideoFileClip(videoPath)
    audio_file = video.audio 
    audio_file.write_audiofile("temp_audio.wav") 
    r = sr.Recognizer() 
    with sr.AudioFile("temp_audio.wav") as source: 
        audio_data = r.record(source)
        text = r.recognize_google(audio_data) 
    # Remove temporary audio file
    os.remove("temp_audio.wav")
    return text
    
