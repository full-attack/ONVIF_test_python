import os
from onvif import ONVIFCamera

mycam = ONVIFCamera('172.18.146.148', 80, 'admin', 'Supervisor')

ptz = mycam.create_ptz_service()
media = mycam.create_media_service()
imaging = mycam.create_imaging_service()

requestGetImaging = imaging.create_type('GetImagingSettings')
video_sources = media.GetVideoSources()
requestGetImaging.VideoSourceToken = video_sources[0].token
profiles = media.GetProfiles()
token = profiles[0].token

responseGetImageSettings = imaging.GetImagingSettings(requestGetImaging)

responseGetImageSettings.Brightness = 50.0

req = imaging.create_type('SetImagingSettings')

req.ImagingSettings = responseGetImageSettings
req.VideoSourceToken = video_sources[0].token
req.ForcePersistence = True

imaging.SetImagingSettings(req)
