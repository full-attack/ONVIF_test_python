import os
from onvif import ONVIFCamera

mycam = ONVIFCamera('172.18.191.63', 80, 'admin', 'Supervisor')

media_service = mycam.create_media_service()

profiles = media_service.GetProfiles()

token = profiles[0].token

configurations_list = media_service.GetAudioEncoderConfigurationOptions()
print(configurations_list)
configurations_list.Options[0].Encoding = 'AAC'
configurations_list.Options[0].BitrateList.Items[0] = 17
print(configurations_list)
