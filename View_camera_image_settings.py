import os
from onvif import ONVIFCamera

mycam = ONVIFCamera('172.18.191.63', 80, 'admin', 'Supervisor')

ptz = mycam.create_ptz_service()
media = mycam.create_media_service()
imaging = mycam.create_imaging_service()

requestGetImaging = imaging.create_type('GetImagingSettings')
video_sources = media.GetVideoSources()
requestGetImaging.VideoSourceToken = video_sources[0].token

responseGetImageSettings = imaging.GetImagingSettings(requestGetImaging)


print(responseGetImageSettings)
