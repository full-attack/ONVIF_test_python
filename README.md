# ONVIF_test_pyrhon
Test files for Onvif cameras functionality. 
Задача
Освоить различные функции камер  на примере доступных в лабораториях, изучив и подтвердив практическим использованием их возможности.
В качестве примера рассмотреть возможности видеокамер:
1.	FishEye камера, установлена в лаборатории на потолке.(172.18.191.196)
2.	PTZ камера перед доской в лаборатории(172.18.191.177)
3.	PTZ камера Axis на потолке в лаборатории(172.18.212.15/172.18.212.16)
4.	PTZ камера 10х (будет установлена над телевизором в лаборатории. Такие же стоят в аудиториях) (172.18.191.95)
5.	PTZ камера 30х (есть в лаборатории, такие стоят в лекционных аудиториях) (172.18.191.63 - сделали)
6.	Корпусная камера 36х 8МП (в лаборатории, вероятно будет установлена в кожух).

для 5 из 6 камер уже можно составить таблицы, на основе исследований, сделанных с помощью протокола onvif и питона .
Запись
	FishEye           172.18.191.196	PTZ камера(перед доской) 172.18.191.177	PTZ камера Axis 
172.18.212.16/ 172.18.212.15	PTZ камера 10x
172.18.191.95	PTZ камера 30x 172.18.191.63	Корпусная камера 36x 8МП	Корпусная камера Sunell 
Старт/стоп	+	+	+	+	+		
Сигнализация	+	-	+	-	-		
Передача записи на удаленный сервер	не подд	не подд	не подд	не подд	не подд		
Передача отдельных кадров по наступлению определенных событий	не подд	+	не подд	+	+		
Изменение настроек плановой записи по расписанию	не подд	не подд	не подд	не подд	не подд		

не поддерживается протокол recording, search, pullpoint

import os
from onvif import ONVIFCamera

mycam = ONVIFCamera('172.18.191.196', 80, 'admin', 'Supervisor')

media_service = mycam.create_media_service()

profiles = media_service.GetProfiles()

token = profiles[0].token

configurations_list = media_service.StopMulticastStreaming(token)


import os
from onvif import ONVIFCamera

mycam = ONVIFCamera('172.18.191.63', 80, 'admin', 'Supervisor')

media_service = mycam.create_events_service()
e = media_service.GetEventProperties()
print(e)

Изображение

	FishEye           172.18.191.196	PTZ камера(перед доской) 172.18.191.177	PTZ камера Axis 
172.18.212.16/ 172.18.212.15	PTZ камера 10x
172.18.191.95	PTZ камера 30x 172.18.191.63	Корпусная камера 36x 8МП	Корпусная камера Sunell 
Регулированиеbrightness	+	+	не подд	+	+		
Contrast	+	+	не подд	+	+		
Насыщенность (saturation)	+	+	не подд	+	+		
Резкость
(Sharpness)	+	+	не подд	+	+		
color tone (cb/cr)	-	+	не подд	+	+		
Регулирование фокуса	+	-	не подд	+	+		

 у камеры Axis не поддерживается протокол imaging
Код для получения информации по изображению:

import os
from onvif import ONVIFCamera

mycam = ONVIFCamera('172.18.191.196', 80, 'admin', 'Supervisor')

ptz = mycam.create_ptz_service()
media = mycam.create_media_service()
imaging = mycam.create_imaging_service()

requestGetImaging = imaging.create_type('GetImagingSettings')
video_sources = media.GetVideoSources()
requestGetImaging.VideoSourceToken = video_sources[0].token

responseGetImageSettings = imaging.GetImagingSettings(requestGetImaging)


print(responseGetImageSettings)



Стримминг 

	FishEye           172.18.191.196	PTZ камера(перед доской) 172.18.191.177	PTZ камера Axis 
172.18.212.16/ 172.18.212.15	PTZ камера 10x
172.18.191.95	PTZ камера 30x 172.18.191.63	Корпусная камера 36x 8МП	Корпусная камера Sunell 
Настройка битрейта	‘BitrateLimit': 1024	‘BitrateLimit': 6192	'BitrateLimit': 0	'BitrateLimit': 4096	'BitrateLimit': 8000		
Настройка фреймрейта	JPEG: FrameRateRange: 'Min': 1,
       'Max': 25
H264: 
FrameRateRange: 
'Min': 1,
'Max': 25	H264: 
FrameRateRange: 
'Min': 1,
'Max': 25	H264: 
FrameRateRange: 
'Min': 1,
'Max': 25	JPEG: 
FrameRateRange: 
'Min': 1,
'Max': 30
H264:
FrameRateRange: 
'Min': 1,
'Max': 25	JPEG: 
FrameRateRange: 
'Min': 1,
'Max': 30
H264:
FrameRateRange: 
'Min': 1,
'Max': 25		
Настройка интервала GOP	JPEG: -
H264: 
GovLengthRange:
'Min': 1,
'Max': 400	H264: 
GovLengthRange:
'Min': 1,
'Max': 100	H264: 
GovLengthRange:
'Min': 1,
'Max': 32767	JPEG:
GovLengthRange:
'Min': 1,
'Max': 50	H264:
GovLengthRange:
'Min': 1,
'Max': 50		
Связь с битрейтом	JPEG: EncodingIntervalRange:     'Min': 1,
'Max': 1;
H264:
EncodingIntervalRange:     'Min': 1,
'Max': 1	H264:
EncodingIntervalRange:     'Min': 1,
'Max': 100	H264:
EncodingIntervalRange:     'Min': 0,
'Max': 0	JPEG:
EncodingIntervalRange:     'Min': 1,
'Max': 30
H264:
EncodingIntervalRange:     'Min': 1,
'Max': 30	JPEG:
EncodingIntervalRange:     'Min': 1,
'Max': 30
H264:
EncodingIntervalRange:     'Min': 1,
'Max': 30		
Варианты регулирования качества потока	'Min': 0,
'Max': 5


	'Min': 0,
'Max': 5	'Min': 0,
'Max': 100	'Min': 0,
'Max': 5	'Min': 0,
'Max': 5		
Выбор кодека	JPEG - Width: 352,Heigh: 288;Width:640,Heigh:480;Width: 704,Heigh:576;Width:1280,Heigh:720;Width: 1280,Heigh:960;Width:1920,Heigh:1080

H264:
Width:1280,Heigh:720;Width: 1280,Heigh:960;Width:1920,Heigh:1080;Width:2560,Heigh:1440;Width:352,Heigh:288;Width:640,Heigh:480;Width:704,Heigh:576;
'H264ProfilesSupported':
'Main', 'Baseline','High'	H264:
Width:2560,Heigh:1920;Width:2560,Heigh:1440;Width:2304,Heigh:1296;Width:1920,Heigh:1080;Width:1280,Heigh:720; Width:640,Heigh:512;Width:800,Heigh:448; Width:704,Heigh:576;Width:640,Heigh:360;Width:352,Heigh:288;
'H264ProfilesSupported':
'Main'	H264:
Width:1280,Heigh:720;Width:1024,Heigh:768;
Width:1024,Heigh:576;Width:800,Heigh:600;
H264:Baseline;
	JPEG: Width:2560,Heigh:1440;
H264: Width:2560,Heigh:1440;
H264:Baseline;	JPEG: Width:2560,Heigh:720;
H264:
Width:1280,Heigh:720;Width:1280,Heigh:960;
Width:1920,Heigh:1080;
H264:Baseline;
		

Код для получения информации по стриммингу:

1)
import os
from onvif import ONVIFCamera

mycam = ONVIFCamera('172.18.191.63', 80, 'admin', 'Supervisor')

media_service = mycam.create_media_service()

profiles = media_service.GetProfiles()

token = profiles[0].token

configurations_list = media_service.GetVideoEncoderConfigurations()

print(configurations_list)

2)
import os
from onvif import ONVIFCamera

mycam = ONVIFCamera('172.18.191.63', 80, 'admin', 'Supervisor')

media_service = mycam.create_media_service()

profiles = media_service.GetProfiles()

token = profiles[0].token

configurations_list = media_service.GetVideoEncoderConfigurationOptions()
print(configurations_list)

Звук

	FishEye           172.18.191.196	PTZ камера(перед доской) 172.18.191.177	PTZ камера Axis 
172.18.212.16/ 172.18.212.15	PTZ камера 10x
172.18.191.95	PTZ камера 30x 172.18.191.63	Корпусная камера 36x 8МП	Корпусная камера Sunell 
Громкость	+	-	-	-	-		
Тип входа	хз	хз	хз	хз	хз		
 Кодек	G711, G726, AAC	G711	AAC, G726, G711	G711	G711		
Битрейт	G711 - 64; G726 - 16;
AAC - 16,32,64	G711 - 64	AAC - 8,12,16,24,32; G726 - 24,32;
G711 - 64 	G711 - 16	G711 - 16		

Код для получения информации по звуку:
1)
import os
from onvif import ONVIFCamera

mycam = ONVIFCamera('172.18.191.63', 80, 'admin', 'Supervisor')

media_service = mycam.create_media_service()

profiles = media_service.GetProfiles()

token = profiles[0].token

configurations_list = media_service.GetAudioEncoderConfigurationOptions()
print(configurations_list)

2)
from onvif import ONVIFCamera

mycam = ONVIFCamera('172.18.191.63', 80, 'admin', 'Supervisor')

media = mycam.create_media_service()
profiles = media.GetProfiles()

token = profiles[0].token
try:
   n = media.GetProfiles()
   print(n)
except Exception as e:
   print(e)

7.	Корпусная камера Sunell (в настоящее время лежит в Медиацентре, но может быть установлена в стенд для экспериментального исследования. 
подключение через консоль с помощью VPN и ffmpeg к  ONVIF_CAMERA (на доску)
Также ознакомиться с оснащением входами/выходами сигнализации и звука, способность вести запись на встроенную флешку.
