from pymavlink import mavutil


class DroneConnection:

    def __init__(self):

        print("======================================")
        print("Connecting to ArduPilot...")
        print("======================================")

        ports = [
            "tcp:127.0.0.1:5760",
            "tcp:127.0.0.1:5762",
            "tcp:127.0.0.1:5763",
        ]

        self.master = None

        for port in ports:

            print(f"\nTrying {port}...")

            try:
                connection = mavutil.mavlink_connection(port)

                print("Waiting for heartbeat (10 sec timeout)...")

                heartbeat = connection.wait_heartbeat(timeout=10)

                if heartbeat is not None:
                    print(f"\nSUCCESS! Connected on {port}")
                    self.master = connection
                    break

                print("No heartbeat received.")

            except Exception as e:
                print(f"Failed: {e}")

        if self.master is None:
            print("\n======================================")
            print("Could not connect to any MAVLink port.")
            print("======================================")
        else:
            print("\nDrone is ready.")