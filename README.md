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

![](./Users/MI/Downloads/images_mark_onvif/recording_table.png)

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


![](C:\Users\MI\Downloads\images_mark_onvif\image_table.png)

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



![](C:\Users\MI\Downloads\images_mark_onvif\stream1_table.png)
![](C:\Users\MI\Downloads\images_mark_onvif\stream2_table.png)
		

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


![](C:\Users\MI\Downloads\images_mark_onvif\audio_table.png)

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
