import subprocess
import yaml
import os

CONFIG_PATH = "config.yaml"
SCRIPT_NAME = "dump_requests.py"

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)

def main():
    config = load_config()
    script_path = os.path.join(os.getcwd(), SCRIPT_NAME)

    cmd = [
        "mitmdump",
        "--listen-host", config["listen_host"],
        "--listen-port", str(config["listen_port"]),
        "--set", "block_global=false",
        "--set", "ssl_insecure=true",
        "--quiet",
        "-s", script_path
    ]

    process = subprocess.Popen(cmd)
    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()
        print("\nmitmdump stopped")

if __name__ == "__main__":
    main()

