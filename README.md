# ONVIF_test_pyrhon
Тестирование функционала Onvif камер (ветка main)

### [Ссылка на документацию](https://docs.google.com/document/d/1ETw8d2tpn5bOo9HkvTpNQYkNZ9M5JjlaIUZn-Op_XgA/edit)
## Задача
Освоить различные функции камер  на примере доступных в лабораториях, изучив и подтвердив практическим использованием их возможности.
В качестве примера рассмотреть возможности видеокамер:
1.	FishEye камера, установлена в лаборатории на потолке.(172.18.191.196)
2.	PTZ камера перед доской в лаборатории(172.18.191.177)
3.	PTZ камера Axis на потолке в лаборатории(172.18.212.15/172.18.212.16)
4.	PTZ камера 10х (будет установлена над телевизором в лаборатории. Такие же стоят в аудиториях) (172.18.191.95)
5.	PTZ камера 30х (в лекционной аудитории) (172.18.191.63 - сделали)
6.	Корпусная камера 36х 8МП 
7.	Корпусная камера Sunell (в настоящее время лежит в Медиацентре, но может быть установлена в стенд для экспериментального исследования. 
подключение через консоль с помощью VPN и ffmpeg к  ONVIF_CAMERA (на доску)

Также ознакомиться с оснащением входами/выходами сигнализации и звука, способность вести запись на встроенную флешку.

Для 5 из 6 камер уже можно составить таблицы, на основе исследований, сделанных с помощью протокола onvif и питона .

![recording_table](https://user-images.githubusercontent.com/75256407/160934173-194b81af-677c-4548-afd7-dd3e1a70086c.png)

Не поддерживается протокол recording, search, pullpoint
### Код для получения информации по записи:
```python
import os
from onvif import ONVIFCamera

mycam = ONVIFCamera('172.18.191.196', 80, 'admin', 'Supervisor')

media_service = mycam.create_media_service()

profiles = media_service.GetProfiles()

token = profiles[0].token

configurations_list = media_service.StopMulticastStreaming(token)
```



```python
import os
from onvif import ONVIFCamera

mycam = ONVIFCamera('172.18.191.63', 80, 'admin', 'Supervisor')

media_service = mycam.create_events_service()
e = media_service.GetEventProperties()
print(e)
```




![image_table](https://user-images.githubusercontent.com/75256407/160934170-091548c8-b13c-4e19-a16f-d434251f434b.png)

 у камеры Axis не поддерживается протокол imaging
### Код для получения информации по изображению:

```python
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
```



![stream1_table](https://user-images.githubusercontent.com/75256407/160934174-7021446c-aa2a-4bb5-b627-a5128e942fd6.png)
![stream2_table](https://user-images.githubusercontent.com/75256407/160934176-5172e445-6572-40fa-a4d0-3817d84e3f5d.png)
		

### Код для получения информации по стриммингу:

1)
```python
import os
from onvif import ONVIFCamera

mycam = ONVIFCamera('172.18.191.63', 80, 'admin', 'Supervisor')

media_service = mycam.create_media_service()

profiles = media_service.GetProfiles()

token = profiles[0].token

configurations_list = media_service.GetVideoEncoderConfigurations()

print(configurations_list)
```


2)

```python
import os
from onvif import ONVIFCamera

mycam = ONVIFCamera('172.18.191.63', 80, 'admin', 'Supervisor')

media_service = mycam.create_media_service()

profiles = media_service.GetProfiles()

token = profiles[0].token

configurations_list = media_service.GetVideoEncoderConfigurationOptions()
print(configurations_list)
```



![audio_table](https://user-images.githubusercontent.com/75256407/160934177-74670bf6-2563-448b-a094-8c0545ea3c5d.png)

### Код для получения информации по звуку:
1)
```python
import os
from onvif import ONVIFCamera

mycam = ONVIFCamera('172.18.191.63', 80, 'admin', 'Supervisor')

media_service = mycam.create_media_service()

profiles = media_service.GetProfiles()

token = profiles[0].token

configurations_list = media_service.GetAudioEncoderConfigurationOptions()
print(configurations_list)

```


2)
```python
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
```



