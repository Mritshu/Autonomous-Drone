from pymavlink import mavutil
import time
import math


class Telemetry:

    def __init__(self, master):

        print("Telemetry object created.")

        self.master = master

        print("Requesting telemetry stream...")

        self.master.mav.request_data_stream_send(
            self.master.target_system,
            self.master.target_component,
            mavutil.mavlink.MAV_DATA_STREAM_ALL,
            10,
            1
        )

        time.sleep(1)

    def get_gps(self):

        while True:

            msg = self.master.recv_match(
                type="GLOBAL_POSITION_INT",
                blocking=True,
                timeout=5
            )

            if msg is not None:

                latitude = msg.lat / 1e7
                longitude = msg.lon / 1e7
                altitude = msg.alt / 1000

                return latitude, longitude, altitude

    def get_attitude(self):

        while True:

            msg = self.master.recv_match(
                type="ATTITUDE",
                blocking=True,
                timeout=5
            )

            if msg is not None:

                roll = math.degrees(msg.roll)
                pitch = math.degrees(msg.pitch)
                yaw = math.degrees(msg.yaw)

                return roll, pitch, yaw

    def print_status(self):

        latitude, longitude, altitude = self.get_gps()

        roll, pitch, yaw = self.get_attitude()

        print("\n========== DRONE STATUS ==========\n")

        print(f"Latitude  : {latitude}")
        print(f"Longitude : {longitude}")
        print(f"Altitude  : {altitude:.2f} m\n")

        print(f"Roll      : {roll:.2f}°")
        print(f"Pitch     : {pitch:.2f}°")
        print(f"Yaw       : {yaw:.2f}°")

        print("\n=================================\n")