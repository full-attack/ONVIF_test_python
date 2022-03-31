import os
from onvif import ONVIFCamera

def stop():
requests.PanTilt = True
requests.Zoom = True
#print(f"request:{requests}")
ptz.Stop(requests)

def perform_move(requestc):
ret = ptz.ContinuousMove(requestc)

def move_tilt(velocity):
requestc.Velocity.PanTilt.x = 0.0
requestc.Velocity.PanTilt.y = velocity
perform_move(requestc)

def move_pan(velocity):
requestc.Velocity.PanTilt.x = velocity
requestc.Velocity.PanTilt.y = 0.0
perform_move(requestc)

def move_continuous(pan, tilt):
requestc.Velocity.PanTilt.x = pan
requestc.Velocity.PanTilt.y = tilt
perform_move(requestc)

def zoom(velocity):
requestc.Velocity.Zoom.x = velocity
perform_move(requestc)

def move_abspantilt(pan, tilt, velocity):
requesta.Position.PanTilt.x = pan
requesta.Position.PanTilt.y = tilt
requesta.Speed.PanTilt.x = velocity
requesta.Speed.PanTilt.y = velocity
ret = ptz.AbsoluteMove(requesta)

def move_relative(pan, tilt, velocity):
requestr.Translation.PanTilt.x = pan
requestr.Translation.PanTilt.y = tilt
requestr.Speed.PanTilt = [velocity, velocity]
requestr.Speed.Zoom = 0.8
ret = ptz.RelativeMove(requestr)

def zoom_relative(zoom, velocity):
requestr.Translation.PanTilt.x = 0
requestr.Translation.PanTilt.y = 0
requestr.Translation.Zoom.x = zoom
requestr.Speed.PanTilt.x = 0
requestr.Speed.PanTilt.y = 0
requestr.Speed.Zoom.x = velocity
ret = ptz.RelativeMove(requestr)

def set_preset(name):
requestp.PresetName = name
requestp.PresetToken = '1'
preset = ptz.SetPreset(requestp)

def get_preset():
ptzPresetsList = ptz.GetPresets(requestc)

def goto_preset():
requestg.PresetToken = '1'
ptz.GotoPreset(requestg)

mycam = ONVIFCamera('172.18.191.63', 80, 'admin', 'Supervisor')
name = '172.18.191.63'
ptz = mycam.create_ptz_service()
media = mycam.create_media_service()
imaging = mycam.create_imaging_service()
media_profile = media.GetProfiles()[0]
# Use the first profile and Profiles have at least one
token = media_profile.token
request = ptz.create_type('GetServiceCapabilities')
Service_Capabilities = ptz.GetServiceCapabilities(request)
status = ptz.GetStatus({'ProfileToken':token})
request = ptz.create_type('GetConfigurationOptions')
request.ConfigurationToken = media_profile.PTZConfiguration.token
ptz_configuration_options = ptz.GetConfigurationOptions(request)
requestc = ptz.create_type('ContinuousMove')
requestc.ProfileToken = media_profile.token
if requestc.Velocity is None:
requestc.Velocity = ptz.GetStatus({'ProfileToken': media_profile.token}).Position
requestc.Velocity.PanTilt.space = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].URI
requestc.Velocity.Zoom.space = ptz_configuration_options.Spaces.ContinuousZoomVelocitySpace[0].URI
requesta = ptz.create_type('AbsoluteMove')
requesta.ProfileToken = media_profile.token
if requesta.Position is None:
requesta.Position = ptz.GetStatus(
{'ProfileToken': media_profile.token}).Position
if requesta.Speed is None:
requesta.Speed = ptz.GetStatus(
{'ProfileToken': media_profile.token}).Position
requestr = ptz.create_type('RelativeMove')
requestr.ProfileToken = media_profile.token
if requestr.Translation is None:
requestr.Translation = ptz.GetStatus(
{'ProfileToken': media_profile.token}).Position
requestr.Translation.PanTilt.space = ptz_configuration_options.Spaces.RelativePanTiltTranslationSpace[0].URI
requestr.Translation.Zoom.space = ptz_configuration_options.Spaces.RelativeZoomTranslationSpace[0].URI
if requestr.Speed is None:
requestr.Speed = ptz.GetStatus(
{'ProfileToken': media_profile.token}).Position
requests = ptz.create_type('Stop')
requests.ProfileToken = media_profile.token
requestp = ptz.create_type('SetPreset')
requestp.ProfileToken = media_profile.token
requestg = ptz.create_type('GotoPreset')
requestg.ProfileToken = media_profile.token
stop()
goto_preset()
zoom_relative(0.5,0.4)
move_tilt(0.5)
move_pan(0.5)
move_continuous(0.1,0.2)
zoom(0.2)
move_abspantilt(0.1,0.3,0.4)
