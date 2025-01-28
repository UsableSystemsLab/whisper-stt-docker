import numpy as np
import io
import soundfile as sf
import whisper
import os
from pydub import AudioSegment


print("loading model ...")
model = whisper.load_model("medium", weights_only=True)
print("model loaded.")

def transcribe(audio_file):
    if not os.path.exists(audio_file):
        print("No audio provided")
        os.exit(1)

    # Read the audio file with pydub
    audio = AudioSegment.from_file(audio_file)
    audio = audio.set_channels(1)
    audio = audio.set_frame_rate(16000)

    # Convert audio to WAV format
    wav_io = io.BytesIO()
    audio.export(wav_io, format="wav")
    wav_io.seek(0)

    # Use soundfile to read the WAV data
    audio_data, sample_rate = sf.read(wav_io)
    audio_array = np.array(audio_data, dtype=np.float32)

    # Transcribe the audio with Whisper model
    result = model.transcribe(audio_array)
    transcript_text = result["text"]

    return transcript_text


# Read the audio file path name frm the command line
print("Usage: python whisper.py <audio_file>")
audio_file = os.sys.argv[1]
print(transcribe(audio_file))
