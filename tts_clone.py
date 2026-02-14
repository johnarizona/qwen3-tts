#Use the voice clone model from https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice

import torch
import soundfile as sf
from qwen_tts import Qwen3TTSModel

model = Qwen3TTSModel.from_pretrained(
    #use this line to point to a locally saved model
    "D:\\demos\\qwen3-tts\\models\\Qwen3-TTS-12Hz-1.7B-Base",
    #use this line if model hasn't been downloaded and you want to download it automatically from Hugginface
    #"Qwen/Qwen3-TTS-12Hz-1.7B-Base",
    device_map="cuda:0",
    dtype=torch.bfloat16,
    #use either sdpa or flash_attention_2. flash_attention_2 is notoriously difficult to compile on Windows so we're using sdpa by default
    attn_implementation="sdpa",
    #attn_implementation="flash_attention_2",
)

#point to the local audio file with the voice you want to clone
ref_audio = "D:\\demos\\qwen3-tts\\connor.mpa"
ref_text  = "Something's wrong. She's never this nice."

wavs, sr = model.generate_voice_clone(
    text="I'm right here. I'm fine.",
    language="English",
    ref_audio=ref_audio,
    ref_text=ref_text,
)
sf.write("output_voice_clone.wav", wavs[0], sr)