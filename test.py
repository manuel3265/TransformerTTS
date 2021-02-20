#
# def numero_to_letras(numero):
#     indicador = [("", ""), ("MIL", "MIL"), ("MILLON", "MILLONES"), ("MIL", "MIL"), ("BILLON", "BILLONES")]
#     entero = int(numero)
#     decimal = int(round((numero - entero) * 100))
#     # print 'decimal : ',decimal
#     contador = 0
#     numero_letras = ""
#     while entero > 0:
#         a = entero % 1000
#         if contador == 0:
#             en_letras = convierte_cifra(a, 1).strip()
#         else:
#             en_letras = convierte_cifra(a, 0).strip()
#         if a == 0:
#             numero_letras = en_letras + " " + numero_letras
#         elif a == 1:
#             if contador in (1, 3):
#                 numero_letras = indicador[contador][0] + " " + numero_letras
#             else:
#                 numero_letras = en_letras + " " + indicador[contador][0] + " " + numero_letras
#         else:
#             numero_letras = en_letras + " " + indicador[contador][1] + " " + numero_letras
#         numero_letras = numero_letras.strip()
#         contador = contador + 1
#         entero = int(entero / 1000)
#     numero_letras = numero_letras.lower()
#     # print('numero: ', numero)
#     # print(numero_letras)
#     return numero_letras
#
#
# def convierte_cifra(numero, sw):
#     lista_centana = ["", ("CIEN", "CIENTO"), "DOSCIENTOS", "TRESCIENTOS", "CUATROCIENTOS", "QUINIENTOS", "SEISCIENTOS",
#                      "SETECIENTOS", "OCHOCIENTOS", "NOVECIENTOS"]
#     lista_decena = ["", (
#     "DIEZ", "ONCE", "DOCE", "TRECE", "CATORCE", "QUINCE", "DIECISEIS", "DIECISIETE", "DIECIOCHO", "DIECINUEVE"),
#                     ("VEINTE", "VEINTI"), ("TREINTA", "TREINTA Y"), ("CUARENTA", "CUARENTA Y"),
#                     ("CINCUENTA", "CINCUENTA Y"), ("SESENTA", "SESENTA Y"),
#                     ("SETENTA", "SETENTA Y"), ("OCHENTA", "OCHENTA Y"),
#                     ("NOVENTA", "NOVENTA Y")
#                     ]
#     lista_unidad = ["", ("UN", "UNO"), "DOS", "TRES", "CUATRO", "CINCO", "SEIS", "SIETE", "OCHO", "NUEVE"]
#     centena = int(numero / 100)
#     decena = int((numero - (centena * 100)) / 10)
#     unidad = int(numero - (centena * 100 + decena * 10))
#     # print "centena: ",centena, "decena: ",decena,'unidad: ',unidad
#
#     texto_centena = ""
#     texto_decena = ""
#     texto_unidad = ""
#
#     # Validad las centenas
#     texto_centena = lista_centana[centena]
#     if centena == 1:
#         if (decena + unidad) != 0:
#             texto_centena = texto_centena[1]
#         else:
#             texto_centena = texto_centena[0]
#
#     # Valida las decenas
#     texto_decena = lista_decena[decena]
#     if decena == 1:
#         texto_decena = texto_decena[unidad]
#     elif decena > 1:
#         if unidad != 0:
#             texto_decena = texto_decena[1]
#         else:
#             texto_decena = texto_decena[0]
#     # Validar las unidades
#     # print "texto_unidad: ",texto_unidad
#     if decena != 1:
#         texto_unidad = lista_unidad[unidad]
#         if unidad == 1:
#             texto_unidad = texto_unidad[sw]
#
#     return "%s %s %s" % (texto_centena, texto_decena, texto_unidad)
#         # print(filename, text)
#
# numbers = []
# with open('numbers.csv', encoding='utf-8') as csv_file:
#     for line in csv_file:
#         numbers.append(line.split('\n')[0])
#
# f = open("metadata1.csv", "a", encoding='utf-8')
# with open('metadata.csv', encoding='utf-8') as csv_file:
#     for line in csv_file:
#         splitted = line.split('\n')[0].split('|')
#         filename = splitted[0]
#         text = splitted[1]
#         if len(text.split(' ')) > 1:
#             digitsList = [int(digitNumber) for digitNumber in text.split() if digitNumber.isdigit()]
#             for digit in digitsList:
#                 text = text.replace(str(digit), str(numero_to_letras(digit)))
#             for number in numbers:
#                 if text.find(number.lower().replace(' ', '')) != -1:
#                     text = text.replace(number.lower().replace(' ', ''), number.lower())
#             f.write(filename + '|' + text + '|' + text + '\n')
# f.close()
#
#
#

import librosa as librosa
import numpy as np
import matplotlib.pyplot as plt

import librosa.display

n_fft=2048

# Step or stride between windows. If the step is smaller than the window lenght, the windows will overlap
hop_length=512

# Load sample audio file
y, sr = librosa.load(librosa.util.example_audio_file())

# Calculate the spectrogram as the square of the complex magnitude of the STFT
spectrogram_librosa = np.abs(librosa.stft(
    y, n_fft=n_fft, hop_length=hop_length, win_length=n_fft, window='hann'))

# spectrogram_librosa_db = librosa.power_to_db(spectrogram_librosa, ref=np.max)



f = plt.figure(figsize=(10, 4))
s_db = librosa.power_to_db(spectrogram_librosa, ref=np.max)
ax = librosa.display.specshow(s_db,
                              x_axis='time',
                              y_axis='mel',
                              sr=22050,
                              fmin=40,
                              fmax=None)
print(ax, type(ax))
f.add_subplot(ax)
