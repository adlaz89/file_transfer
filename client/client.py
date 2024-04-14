import requests
import time

SERVER_URL = "http://192.168.20.188:8000"
CHECK_INTERVAL = 60  # in seconds, set to how often you want to check for new files

def list_files():
    """Get the list of files from the server."""
    response = requests.get(f"{SERVER_URL}/list-files/")
    return response.json()

def download_file(file_path):
    """Download a file given its server path."""
    response = requests.get(f"{SERVER_URL}/download-file/{file_path}")
    if response.status_code == 200:
        with open(file_path.split('/')[-1], 'wb') as f:
            f.write(response.content)
        return True
    return False

def delete_file(file_path):
    """Delete a file from the server."""
    response = requests.delete(f"{SERVER_URL}/delete-file/{file_path}")
    return response.status_code == 200

def main():
    while True:
        files = list_files()
        if files:
            print(f"Found {len(files)} files. Downloading...")
            for file_path in files:
                if download_file(file_path):
                    print(f"Downloaded {file_path} successfully.")
                    if delete_file(file_path):
                        print(f"Deleted {file_path} successfully.")
                    else:
                        print(f"Failed to delete {file_path}.")
                else:
                    print(f"Failed to download {file_path}.")
        else:
            print("No new files found.")
        
        print(f"Waiting for {CHECK_INTERVAL} seconds.")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
