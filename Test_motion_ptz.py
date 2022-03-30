from time import sleep

from onvif import ONVIFCamera

XMAX = 1
XMIN = -1
YMAX = 1
YMIN = -1

def perform_move(ptz, request, timeout):
# Start continuous move
ptz.ContinuousMove(request)
# Wait a certain time
sleep(timeout)
# Stop continuous move
ptz.Stop({'ProfileToken': request.ProfileToken})

def move_up(ptz, request, status, timeout=1):
print ('move up...')
status.Position.PanTilt.x = 0
status.Position.PanTilt.y = YMAX
request.Velocity = status.Position
perform_move(ptz, request, timeout)

def move_down(ptz, request,status, timeout=1):
print ('move down...')
status.Position.PanTilt.x = 0
status.Position.PanTilt.y = YMIN
request.Velocity = status.Position
perform_move(ptz, request, timeout)

def move_right(ptz, request, status, timeout=1):
print('move right...')
status.Position.PanTilt.x = XMAX
status.Position.PanTilt.y = 0
request.Velocity = status.Position
perform_move(ptz, request, timeout)

def move_left(ptz, request,status, timeout=1):
print('move left...')
status.Position.PanTilt.x = XMIN
status.Position.PanTilt.y = 0
request.Velocity = status.Position
perform_move(ptz, request, timeout)

def continuous_move():
mycam = ONVIFCamera('172.18.191.63', 80, 'admin', 'Supervisor') # , no_cache=True)

# Create media service object
media = mycam.create_media_service()
# Create ptz service object
ptz = mycam.create_ptz_service()

# Get target profile
media_profile = media.GetProfiles()[0]

# Get PTZ configuration options for getting continuous move range
request = ptz.create_type('GetConfigurationOptions')
request.ConfigurationToken = media_profile.PTZConfiguration.token
ptz_configuration_options = ptz.GetConfigurationOptions(request)

request = ptz.create_type('ContinuousMove')
request.ProfileToken = media_profile.token

ptz.Stop({'ProfileToken': media_profile.token})

status = ptz.GetStatus({'ProfileToken': media_profile.token})
global XMAX, XMIN, YMAX, YMIN
XMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Max
XMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Min
YMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Max
YMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Min

move_down(ptz, request, status)

move_left(ptz, request, status)

move_up(ptz, request, status)

move_right(ptz, request, status)



if __name__ == '__main__':
continuous_move()
