# take_lease.py
from bosdyn.client import create_standard_sdk
from bosdyn.client.robot import Robot
from bosdyn.client.lease import LeaseClient, LeaseKeepAlive

ROBOT_IP = "192.168.80.3"
USERNAME = "user2"
PASSWORD = "simplepassword"

def take_lease():
    sdk = create_standard_sdk("LeaseTakingApp")
    robot = sdk.create_robot(ROBOT_IP)
    robot.authenticate(USERNAME, PASSWORD)
    lease_client = robot.ensure_client(LeaseClient.default_service_name)

    try:
        # Forcefully take the lease
        lease = lease_client.take()
        print("Lease successfully taken.")
        
        # Keep the lease alive if needed
        lease_keepalive = LeaseKeepAlive(lease_client)
        
        # Add robot commands here if needed
        
    finally:
        # Return the lease after operations are done
        lease_client.return_lease(lease)
        print("Lease returned.")

if __name__ == "__main__":
    take_lease()