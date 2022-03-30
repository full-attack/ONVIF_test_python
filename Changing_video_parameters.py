import os
from onvif import ONVIFCamera

mycam = ONVIFCamera('172.18.191.63', 80, 'admin', 'Supervisor')

media_service = mycam.create_media_service()

profiles = media_service.GetProfiles()

token = profiles[0].token

configurations_list = media_service.GetVideoEncoderConfigurations()

video_encoder_configuration = configurations_list[0]

options = media_service.GetVideoEncoderConfigurationOptions({'ProfileToken':token})

video_encoder_configuration.Encoding = 'H264'

video_encoder_configuration.Resolution.Width = options.H264.ResolutionsAvailable[0].Width
video_encoder_configuration.Resolution.Height = options.H264.ResolutionsAvailable[0].Height

video_encoder_configuration.Quality = options.QualityRange.Max

video_encoder_configuration.RateControl.FrameRateLimit = options.H264.FrameRateRange.Max

video_encoder_configuration.RateControl.EncodingInterval = options.H264.EncodingIntervalRange.Max

video_encoder_configuration.RateControl.BitrateLimit = 8000

request = media_service.create_type('SetVideoEncoderConfiguration')
request.Configuration = video_encoder_configuration

request.ForcePersistence = True

media_service.SetVideoEncoderConfiguration(request)
