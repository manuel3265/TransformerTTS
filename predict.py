from utils.config_manager import Config
from utils.audio import Audio
from scipy.io.wavfile import write
config_loader = Config(config_path=f'config/wavernn/', model_kind=f'autoregressive')
audio = Audio(config_loader.config)
model = config_loader.load_model()
out = model.predict('Los científicos del laboratorio del CERN dicen que han descubierto una nueva partícula.')

# Convert spectrogram to wav (with griffin lim)
wav = audio.reconstruct_waveform(out['mel'].numpy().T)
print(wav, type(wav))
write('test.wav', 16000, wav)
