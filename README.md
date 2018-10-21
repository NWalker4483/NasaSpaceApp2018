# Radiation and Dust Environment Sensors (RADES)
## NASA Space Apps Challenge 2018

### Challenge
* Can You Build A../Make Sense Out of Mars
* Your challenge is to create a sensor (or cluster of multiple sensors) to be used by humans on Mars.

## The Problem
* Increase radiation exposure - Solar Proton Events cause sudden intense increases to radiation experienced on Mars
* Spontaeneous dust storms - can affect electrical connectivity and contribute to overheating
* Extreme temperature (relative to Earth) that all threaten survivability

## Assumptions Made
* Humans will have a permanent home base or central location for Mars explorarion missions
* Humans will have a vehicular means of travel on the surface of Mars
* The MIDAR sensor set on the 2020 Rover will work appropriatley on Mars surface and for the Mars environment (High TRL)
* Tripods successfully used on Apollo missions so tripods are launch and space flight worthy

## The Solution
* Tripod sensor cluster that can read and report selected zones’ relevant data to a home base. 
* Serves as a proximity sensor for weather, data collection, and survivability status reporter.
* The RADES will operate as a line of sight data transfer relay 
* The RADES will include a real time map that displays the “survivability” of each marker position, user accessible on a tablet/laptop.

## Usage
* A series of RADES waypoints away can serve as a sensor network around a permanent settlement
* The RADES can provide long term weather data for selected locations that can be used for basic weather pattern analysis 
* The RADES can monitor conditions in the area real time, providing a positive feedback when sensor expectations are being met or negative feedback when readings are outside of set parameters
* RADES set up will be similar to that of a surveyor set up; sensors ideally would be designed to be modular, all operating on the same mechanical attachment system for ease of replacing sensors
* Example Sensor Detection Usage Cases: 
 * * Radiation has suddenly spiked due to a solar event 
 * * Connection has been lost to a dust storm
 * * Temperature is outside of expected limits

## Business Prospects
* Cheaper to make and replace multiple RADEs than to produce a satellite to take the same readings
* Relatively easy to use and adjust as mission objectives change
* Less susceptible to damage from Solar Proton Events
* Scalable long range application as long as line of sight is met. 

## Links
* [Cad Files](https://myhub.autodesk360.com/ue2922a95/data/permalink/DTa9460QT04a05659b2108a74e9ba99467e7)
* https://github.com/mourner/simpleheat
* https://www.simplicity.be/article/transferring-sensor-readings-over-websockets/
* [WebSockets Tutorial](https://www.toptal.com/tornado/simple-python-websocket-server)
* https://matplotlib.org/gallery/images_contours_and_fields/image_annotated_heatmap.html
