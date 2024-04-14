# Point Cloud Data Manager

This repository contains two main components for managing point cloud data files (.pcd) efficiently:

## Server

A FastAPI server that runs on a Raspberry Pi, designed to manage file operations such as listing available files, downloading files, and deleting files remotely.

## Client

A Python script running on a Mini PC that periodically checks for new files on the server, downloads them, and sends a deletion confirmation once the files are safely transferred.

## Getting Started

These instructions will help you set up and run the project on your local devices for development and testing purposes.

### Prerequisites

- **Python 3.6+**: Required on both the Raspberry Pi (server) and the Mini PC (client).
- **Network Connectivity**: Both devices must be connected to the same network or be able to access each other's IP addresses.

### Server Setup on Raspberry Pi

#### Dependencies

Install FastAPI and Uvicorn to serve the API:

```bash
pip install fastapi uvicorn
```

#### Installation

1. Clone the Repository:

   ```bash
   git clone https://your-repo-url.git
   cd your-repo-directory/server
   ```

2. Setup Virtual Environment (Optional):

   This step is optional but recommended to keep dependencies organized and project-specific.

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install Dependencies:

   With the virtual environment activated, install the required packages.

   ```bash
   pip install fastapi uvicorn
   ```

4. Start the Server:

   Ensure your FastAPI application (server.py) is configured correctly, then start the server:

   ```bash
   uvicorn server:app --host 0.0.0.0 --port 8000
   ```

   Replace `0.0.0.0` with the appropriate IP if needed, although this setting allows connections from all network interfaces.

5. Verify Server Running:

   Access the FastAPI automatic documentation at `http://<Raspberry_Pi_IP>:8000/docs` to see if the server is running correctly and the endpoints are accessible.

#### Configuration

- **IP Address**: Make sure the Raspberry Pi's IP address in the client's script (client.py) matches the IP used when starting the server.
- **Port**: Default is 8000, but can be changed based on network policies or preferences.

### Client Setup on Mini PC

#### Dependencies

Install the Requests library to handle HTTP requests in the client script:

```bash
pip install requests
```

#### Installation

1. Prepare the Client Script:

   Navigate to the client directory where `client.py` is located.

   ```bash
   cd path/to/your/client
   ```

2. Configure the Script:

   Open `client.py` and ensure the `SERVER_URL` is correctly set to your server's IP and port.

3. Run the Client Script:

   Execute the script to start the automated file-checking and downloading process.

   ```bash
   python3 client.py
   ```

#### Operation

The client will periodically check for new files at the interval specified by `CHECK_INTERVAL` (default is 60 seconds).

Files found are downloaded locally and then a request is sent to delete them from the server.

#### Configuration

- **Server URL**: Set this to the Raspberry Pi's IP and the port on which the FastAPI server is running (e.g., `http://192.168.1.5:8000`).
- **Check Interval**: Modify `CHECK_INTERVAL` in `client.py` to change how frequently the client checks for new files.

## Troubleshooting

1. **Network Issues**: If there's a "No route to host" or similar network-related error, ensure both devices are on the same subnet and reachable.
2. **Permissions**: Make sure the Raspberry Pi has appropriate read/write permissions on the directories and files involved.
