"""
This file registers the model with the Python SDK.
"""

from viam.components.sensor import Sensor
from viam.resource.registry import Registry, ResourceCreatorRegistration

from .solaredgeMonitor import solaredgeMonitor

Registry.register_resource_creator(Sensor.SUBTYPE, solaredgeMonitor.MODEL, ResourceCreatorRegistration(solaredgeMonitor.new, solaredgeMonitor.validate))
