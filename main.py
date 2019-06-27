import os
import glob
import time

time_gap = 5 # secs
source = "target_list.txt"


def list_targets(source):
    with open(source) as f:
        lines = f.readlines()


def get_latest(target):
    files = glob.glob(target)
    latest_file = max(files, key=os.path.getctime)
    print(latest_file)
    return latest_file


def get_size(file):
    return os.path.getsize(latest_file)


def get_diff(target):
    size_initial = get_size(target)
    print(size_initial)
    time.sleep(time_gap)
    size_final = get_size(target)
    print(size_final)

    return size_final - size_initial


def main():
    
    for target in targets:
        print(get_diff(target))

if __name__== "__main__":
    main()
