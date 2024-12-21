import datetime
import subprocess

HOSTNAME = ""
LOG_FILE = "host.log"

def log_message(message: str):
    timestamp = datetime.datetime.now(tz=datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} {HOSTNAME} {message} \n"
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)
    print(log_entry)

def is_host_reachable() -> bool:
    try:
        subprocess.run(
            ["ping", "-c", "1", HOSTNAME],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return True
    except subprocess.CalledProcessError:
        log_message("Host is unreachable")
        return False




