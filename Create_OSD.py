import datetime
from onvif import ONVIFCamera
mycam = ONVIFCamera('172.18.191.196', 80, 'admin', 'Supervisor')

mycam.create_media_service()

profiles = mycam.media.GetProfiles()
try:
osd = mycam.media.create_type('CreateOSD')
osd.OSD = {
'token': 'token0',

'Position': {
'Type': 'UpperLeft',
},
'TextString': {
'PlainText': 'TEST',
'Type': 'Plain',
},
'Type': 'Text',
'VideoSourceConfigurationToken': profiles[0].VideoSourceConfiguration.token,
}
response = mycam.media.CreateOSD(osd)
get = mycam.media.GetOSDs()
except Exception as e:
print(e)
