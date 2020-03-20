import subprocess
import time
import datetime
import json


def __ping_single(ip: str) -> int:
    """
    Returns averge ping for one run
    """
    proc = subprocess.Popen(['ping', ip],stdout=subprocess.PIPE)
    result = [line.rstrip().decode() for line in proc.stdout.readlines()]
    latency_line = result[-1].split(" ")
    minimum = int(latency_line[6][:3])
    maximum = int(latency_line[9][:3])
    average = int(latency_line[12][:3])
    return minimum, maximum, average


def __load_historic(file_name: str) -> dict:
    """
    Load the historic dictionary from json file
    """
    pass


def __save_historic(results: dict, file_name):
    """
    Save the results dictionary to json
    """
    pass


def ping():
    """
    main cordinating function for latency_tracker
    """
    pass


if __name__ == "__main__":
    ip = "94.205.104.43"
    results = {}
    while True:
        result = __ping_single(ip)
        print(result)
        results[datetime.datetime.now()] = result
        time.sleep(60)

