from langchain_core.tools import tool

# Helper functions to simulate data retrieval
def get_telemetry_data(data_type):
    # Simulated telemetry data
    telemetry_data = {
    "GPS": {"latitude": 37.7749, "longitude": -122.4194},
    "altitude": 1200, # in meters
    "battery": 85, # in percentage
    "flight_mode": "AUTO",
    "speed": 45,
    # in m/s
    "heading": 90
    # in degrees
    }
    return telemetry_data.get(data_type, "Data type not available")

def get_autopilot_status():
    # Simulated autopilot status
    return {
    "flight_mode": "AUTO",
    "armed": True,
    "waypoint_index": 3,
    "system_health": "Nominal",
    "errors": None
    }

@tool
def mavproxy_command(operator: str, command: str, parameters: str = '') -> dict:
    """
    Use this to send MAVProxy commands to the UAV's autopilot system.
    'operator' can be any of the following: 'Mission Commander', 'Flight Operator', or 'Systems
    Analyst'.'command' is the MAVProxy command to execute (e.g., 'arm throttle', 'mode AUTO', 'wp load
    mission.txt').
    'parameters' are additional parameters required for the command, if any. If not applicable, set
    to an empty string.
    """
    # Simulate executing the MAVProxy command
    return {
    "operator": operator,
    "command": command,
    "parameters": parameters,
    "status": "Command executed successfully"
    }

@tool
def telemetry_request(requester: str, data_type: str) -> dict:
    """
    Use this to request specific telemetry data from the UAV.
    'requester' can be any of the following: 'Mission Commander', 'Flight Operator', 'Systems
    Analyst'.
    'data_type' is the type of telemetry data requested (e.g., 'GPS', 'altitude', 'battery',
    'flight_mode').
    """
    telemetry_data = get_telemetry_data(data_type)
    return {
    "requester": requester,
    "data_type": data_type,
    "data": telemetry_data
    }

@tool
def autopilot_status_update() -> dict:
    """
    The Autopilot System uses this to send status updates and telemetry data back to the ground
    station.
    """
    status_update = get_autopilot_status()
    return {
    "status_update": status_update
    }

@tool
def system_alert(sender: str, alert_level: str, message: str) -> dict:
    """
    Use this to send alerts or warnings to the team.'sender' is the role sending the alert.
    'alert_level' can be 'INFO', 'WARNING', or 'CRITICAL'.
    'message' is the alert message detailing the issue.
    """
    return {
    "sender": sender,
    "alert_level": alert_level,
    "message": message
    }

@tool
def communication(sender: str, receiver: str, message: str) -> dict:
    """
    Use this to facilitate communication between team members.
    'sender' is the role initiating the communication.
    'receiver' is the intended recipient (can be a specific role or 'All').
    'message' is the content of the communication.
    """
    return {
    "sender": sender,
    "receiver": receiver,
    "message": message
    }
