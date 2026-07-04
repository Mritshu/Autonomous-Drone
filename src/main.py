from mavlink.connection import DroneConnection
from mavlink.telemetry import Telemetry

drone = DroneConnection()

telemetry = Telemetry(drone.master)

telemetry.print_messages()