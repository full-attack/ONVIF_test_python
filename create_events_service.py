import datetime
from onvif import ONVIFCamera
mycam = ONVIFCamera('172.18.191.196', 80, 'admin', 'Supervisor')

resp = mycam.devicemgmt.GetHostname()

print('My camera`s hostname: ' + str(resp.Name))

event_service = mycam.create_events_service()
print(event_service.GetEventProperties())
pullpoint = mycam.create_pullpoint_service()
try:
pullmess = pullpoint.PullMessages({"Timeout": datetime.timedelta(seconds=5), "MessageLimit": 10})
print("current time"+ pullmess.CurrentTime)
print("termination time" + pullmess.TerminationTime)
for msg in pullmess.NotificationMessage:
print("message" + msg)
except Exception as e:
print(e)
finally:
pass

#print(pullpoint.PullMessages(10,100))
