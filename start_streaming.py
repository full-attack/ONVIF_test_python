import os
from onvif import ONVIFCamera


mycam = ONVIFCamera('172.18.191.63', 80, 'admin', 'Supervisor')

media_service = mycam.create_media_service()

profiles = media_service.GetProfiles()

token = profiles[0].token

request = media_service.create_type('StartMulticastStreaming')

request.ProfileToken = token

media_service.StartMulticastStreaming(request)

print(request)
