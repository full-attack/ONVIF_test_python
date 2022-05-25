import os
from onvif import ONVIFCamera

mycam = ONVIFCamera('172.18.146.148', 80, 'admin', 'Supervisor')

media_service = mycam.create_media_service()

profiles = media_service.GetProfiles()

token = profiles[0].token

conf = media_service.create_type('GetAudioEncoderConfigurations')
resp = media_service.GetAudioEncoderConfigurations()
r = resp[0]
s = media_service.create_type('SetAudioEncoderConfiguration')
r.Encoding = 'AAC'
s.Configuration = r
s.ForcePersistence = True

media_service.SetAudioEncoderConfiguration({'Configuration':r,'ForcePersistence':True})
