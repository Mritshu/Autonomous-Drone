from mavlink.connection import DroneConnection
from mavlink.telemetry import Telemetry


print("Program Started\n")

drone = DroneConnection()

telemetry = Telemetry(drone.master)

telemetry.print_status()

print("Program Finished")