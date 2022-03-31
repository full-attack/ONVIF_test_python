import os
from onvif import ONVIFCamera

mycam = ONVIFCamera('172.18.191.63', 80, 'admin', 'Supervisor')
name = '172.18.191.63'
ptz = mycam.create_ptz_service()
media = mycam.create_media_service()
imaging = mycam.create_imaging_service()
analytics = mycam.create_analytics_service()
media_profile = media.GetProfiles()[0]
token = media_profile.token
s = analytics.create_type('CreateAnalyticsModules')
r = analytics.create_type('DeleteAnalyticsModules')
c = analytics.create_type('GetServiceCapabilities')
req = analytics.GetServiceCapabilities(c)
x = analytics.create_type('GetSupportedAnalyticsModules')
x.ConfigurationToken = token
b = analytics.GetSupportedAnalyticsModules(x)
