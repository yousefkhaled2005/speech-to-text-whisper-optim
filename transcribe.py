def run_inference(audio_path):
    print(f'Transcribing {audio_path} using INT8 quantized Whisper model.')
run_inference('audio.wav')
