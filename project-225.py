import glob
import os
import sys
import random
import threading
import time
import numpy as np
import cv2
import mayavi as mlab
try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla




actor_list = []
try:
    client = carla.Client('127.0.0.1', 2000)
    client.set_timeout(2.0)
    world = client.get_world()


    get_blueprint_of_world = world.get_blueprint_library()
    car_model = get_blueprint_of_world.filter('model3')[0]
    spawn_point = world.get_map().get_spawn_points()[spawn_point = world.get_map().get_spawn_points()[‘location value’]]
    dropped_vehicle = world.spawn_actor(car_model, spawn_point)
    dropped_vehicle.apply_control(carla.VehicleControl(throttle=0.5))
#write code here

    simulator_camera_location_rotation = carla.Transform(spawn_point.location, spawn_point.rotation)
    simulator_camera_location_rotation.location += spawn_point.get_forward_vector() * 30
    simulator_camera_location_rotation.rotation.yaw += 180
    simulator_camera_view = world.get_spectator()
    simulator_camera_view.set_transform(simulator_camera_location_rotation)

    actor_list.append(dropped_vehicle)



    time.sleep(1000)
finally:
    print('destroying actors')
    for actor in actor_list:
        actor.destroy()
    print('done.')