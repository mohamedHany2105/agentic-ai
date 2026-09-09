import pyttsx3
from faster_whisper import WhisperModel
import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel

# TAKEA MP3 FILE AND THEN WRITE IT
def faster_whisper():
  model = WhisperModel("small", device="cpu", compute_type="int8")

  segments, info = model.transcribe("audio.mp3", language="ar")

  for segment in segments:
    print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")

def talk():

  print("start")
  model = WhisperModel("small", device="cpu", compute_type="int8")

  SAMPLE_RATE = 16000
  CHUNK_DURATION = 4  # كل جملة تتسجل كام ثانية

  print("🎤 اتكلم دلوقتي (اضغط Ctrl+C عشان توقف)...\n")

  try:
    while True:
      # تسجيل مقطع صوتي
      audio = sd.rec(
        int(CHUNK_DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype='float32'
      )
      sd.wait()  # ينتظر لحد ما التسجيل يخلص

      # تحويله لنص
      segments, _ = model.transcribe(
        audio.flatten(),
        language="en",
        vad_filter=True  # يشيل السكوت عشان ميطبعش نص فاضي
      )

      for segment in segments:
        print(segment.text)

  except KeyboardInterrupt:
    print("\n✅ اتوقف.")
talk()
def voice_simple(text):
  #Basic one
  # Get available voices
  engine = pyttsx3.init()
  voices = engine.getProperty('voices')

  # Print available voices to see IDs/genders
  for index, voice in enumerate(voices):
    print(f'ID: {voice.id}, Name: {voice.name}')

  # Change to a different voice index (e.g., 0 for male, 1 for female)
  engine.setProperty('voice', voices[0].id)

  engine.say(text)
  engine.runAndWait()


# def gtts():
#   from gtts import gTTS
#
#   tts = gTTS(text="أهلاً وسهلاً", lang='ar')
#   tts.save("output.mp3")


# def edge_tts():
#   import edge_tts
#   import asyncio
#
#   async def main():
#     communicate = edge_tts.Communicate("أهلاً وسهلاً", "ar-EG-SalmaNeural")
#     await communicate.save("output.mp3")
#
#   asyncio.run(main())

# def piper():
#   import subprocess
#
#   subprocess.run([
#     "piper", "--model", "ar_JO-kareem-medium.onnx",
#     "--output_file", "output.wav"
#   ], input="أهلاً وسهلاً".encode())
# openAiTTS
# def openAiTTS():
#   from openai import OpenAI
#
#   client = OpenAI()
#   response = client.audio.speech.create(
#     model="tts-1",
#     voice="alloy",
#     input="أهلاً وسهلاً"
#   )
#   response.stream_to_file("output.mp3")

# eleven labs

# def eleven_labs():
#
#
# from elevenlabs import generate, save
#     # audio = generate(text="أهلاً وسهلاً", voice="Bella")
#     # save(audio, "output.mp3")
talk()