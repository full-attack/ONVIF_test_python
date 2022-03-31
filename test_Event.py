import os
from onvif import ONVIFCamera

mycam = ONVIFCamera('172.18.191.63', 80, 'admin', 'Supervisor')
name = '172.18.191.63'
ptz = mycam.create_ptz_service()
media = mycam.create_media_service()
imaging = mycam.create_imaging_service()

event = mycam.create_events_service()
media_profile = media.GetProfiles()[0]
# Use the first profile and Profiles have at least one
token = media_profile.token
#r = event.create_type('SetSynchronizationPoint')
r = event.GetServiceCapabilities()
s = event.GetEventProperties()
e = event.CreatePullPointSubscription()
