from typing import ClassVar, Mapping, Sequence, Any, Dict, Optional, Tuple, Final, List, cast
from typing_extensions import Self

from typing import Any, Final, Mapping, Optional


from viam.utils import SensorReading




from viam.module.types import Reconfigurable
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName, Vector3
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily

from viam.components.sensor import Sensor
from viam.logging import getLogger

import time
import asyncio
import urllib.request
import json


LOGGER = getLogger(__name__)

class solaredgeMonitor(Sensor, Reconfigurable):
    
    MODEL: ClassVar[Model] = Model(ModelFamily("mcvella", "sensor"), "solaredge-monitor")
    
    site_id: str
    api_key: str

    # Constructor
    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        my_class = cls(config.name)
        my_class.reconfigure(config, dependencies)
        return my_class

    # Validates JSON Configuration
    @classmethod
    def validate(cls, config: ComponentConfig):
        # here we validate config, the following is just an example and should be updated as needed
        site_id = config.attributes.fields["site_id"].string_value
        if site_id == "":
            raise Exception("A site_id must be defined")
        api_key = config.attributes.fields["api_key"].string_value
        if api_key == "":
            raise Exception("A SolarEdge api_key must be defined")
              
        return

    # Handles attribute reconfiguration
    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        self.site_id = config.attributes.fields["site_id"].string_value
        self.api_key = config.attributes.fields["api_key"].string_value

        return

    
    async def get_readings(
        self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Mapping[str, SensorReading]:
        res = urllib.request.urlopen(f"https://monitoringapi.solaredge.com/site/{self.site_id}/currentPowerFlow/?api_key={self.api_key}")
        res_body = res.read()

        return json.loads(res_body.decode("utf-8"))

