# solaredge-monitor modular resource

This module implements the [rdk sensor API](https://github.com/rdk/sensor-api) in a mcvella:sensor:solaredge-monitor model.
With this model, you can read current power flow from your Solaredge equipment via the [SolarEdge Monitoring Server API](https://knowledge-center.solaredge.com/sites/kc/files/se_monitoring_api.pdf)

## Build and run

To use this module, follow the instructions to [add a module from the Viam Registry](https://docs.viam.com/registry/configure/#add-a-modular-resource-from-the-viam-registry) and select the `mcvella:sensor:solaredge-monitor` model from the [`mcvella:sensor:solaredge-monitor` module](https://app.viam.com/module/rdk/mcvella:sensor:solaredge-monitor).

## Configure your sensor

> [!NOTE]  
> Before configuring your sensor, you must [create a machine](https://docs.viam.com/manage/fleet/machines/#add-a-new-machine).

Navigate to the **Config** tab of your machine's page in [the Viam app](https://app.viam.com/).
Click on the **Components** subtab and click **Create component**.
Select the `sensor` type, then select the `mcvella:sensor:solaredge-monitor` model.
Click **Add module**, then enter a name for your sensor and click **Create**.

On the new component panel, copy and paste the following attribute template into your sensor’s **Attributes** box:

```json
{
  "site_id": "<solaredge site id>",
  "api_key": "<solaredge api key>"
}
```

> [!NOTE]  
> For more information, see [Configure a Machine](https://docs.viam.com/manage/configuration/).

### Attributes

The following attributes are available for `rdk:sensor:mcvella:sensor:solaredge-monitor` sensors:

| Name | Type | Inclusion | Description |
| ---- | ---- | --------- | ----------- |
| `site_id` | string | **Required** |  SolarEdge site ID - from your [Solaredge monitoring portal](https://monitoring.solaredge.com/) or installer|
| `api_key` | string | **Required** |  SolarEdge API KEY - from your [Solaredge monitoring portal](https://monitoring.solaredge.com/) or installer |

### API

This module implements the GetReadings() sensor method, and returns results that look like:

``` JSON
{
  "siteCurrentPowerFlow": {
    "GRID": {
      "currentPower": 0,
      "status": "Active"
    },
    "LOAD": {
      "currentPower": 0.55,
      "status": "Active"
    },
    "PV": {
      "currentPower": 0,
      "status": "Idle"
    },
    "STORAGE": {
      "chargeLevel": 27,
      "critical": false,
      "currentPower": 0.55,
      "status": "Discharging"
    },
    "connections": [
      {
        "from": "STORAGE",
        "to": "Load"
      }
    ],
    "unit": "kW",
    "updateRefreshRate": 3
  }
}
```
