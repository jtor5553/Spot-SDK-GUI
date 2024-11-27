from bosdyn.client import create_standard_sdk
from bosdyn.client.auth import AuthClient

TOKEN_PATH = r"C:\Users\jose3\OneDrive\Desktop\Spot\GUI\spot_token.json"
USERNAME = "user2"
PASSWORD = "simplepassword"

#Generates token so user can be logged in
def generate_token():
    sdk = create_standard_sdk("Spot GUI")
    robot = sdk.create_robot(ROBOT_IP)

    auth_client = robot.ensure_client(AuthClient.default_service_name)
    token = auth_client.get_auth_token(USERNAME, PASSWORD)
    print("Authenticated with user and password")

    auth_client = robot.ensure_client(AuthClient.default_service_name)
    token = auth_client.get_auth_token()

    with open(TOKEN_PATH, "w") as token_file:
        token_file.write(token)
    print(f"Token saved to {TOKEN_PATH}")

#Authenticates the token 
def authenticate_with_token():
    sdk = create_standard_sdk("Spot GUI")
    robot = sdk.create_robot(ROBOT_IP)

    if not os.path.exists(TOKEN_PATH) or os.stat(TOKEN_PATH).st_size == 0:
        generate_token()

    with open(TOKEN_PATH, "r") as token_file:
        token = token_file.read().strip()

    robot.authenticate_with_token(token)

    if not os.path.exists(TOKEN_PATH) or os.stat(TOKEN_PATH).st_size == 0:
        generate_token()

    return robot