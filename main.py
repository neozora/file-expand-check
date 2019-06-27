import os
import glob
import time

time_gap = 5 # secs
target = "//tv3/RECORD/*"

files = glob.glob(target)
latest_file = max(files, key=os.path.getctime)



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
    print(get_diff(target))
    

if __name__== "__main__":
    main()
