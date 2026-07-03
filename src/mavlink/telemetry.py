from pymavlink import mavutil


class Telemetry:

    def __init__(self, master):
        self.master = master

    def get_gps(self):

        while True:

            msg = self.master.recv_match(
                type="GLOBAL_POSITION_INT",
                blocking=True
            )

            if msg is not None:
                return msg

    def print_gps(self):

        gps = self.get_gps()

        print("\n========== GPS ==========")
        print(f"Latitude  : {gps.lat / 1e7}")
        print(f"Longitude : {gps.lon / 1e7}")
        print(f"Altitude  : {gps.alt / 1000:.2f} m")
        print("=========================\n")