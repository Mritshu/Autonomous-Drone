from pymavlink import mavutil
import time


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

    def print_messages(self):

        print("\nListening for MAVLink messages...\n")

        count = 0

        while count < 20:

            msg = self.master.recv_match(
                blocking=True,
                timeout=5
            )

            if msg is None:
                continue

            print(msg.get_type())

            count += 1

        print("\nFinished reading 20 messages.")