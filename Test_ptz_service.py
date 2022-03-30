import os
from onvif import ONVIFCamera

mycam = ONVIFCamera('172.18.191.104', 8899, 'admin', 'Supervisor')

print('Connected to ONVIF camera')
media = mycam.create_media_service() # Создаем медиасервис

ptz = mycam.create_ptz_service() # Создаем сервис для камеры

profile = mycam.media.GetProfiles()[0]
token = profile.token # Получаем токен

request = ptz.create_type('AbsoluteMove')
request.ProfileToken = profile.token
request.Position = {'PanTilt': {'x': 0.7, 'y': 0.7}, 'Zoom': 0}
request.Speed = {'PanTilt': {'x': 1, 'y': 1}, 'Zoom': 1} # default speed
ptz.AbsoluteMove(request)

status = ptz.GetStatus({'ProfileToken': token}) # Получаем текущее положение (PTZ)

print('Pan position:', status.Position.PanTilt.x)
print('Tilt position:', status.Position.PanTilt.y)
print('Zoom position:', status.Position.Zoom.x, '/n')
