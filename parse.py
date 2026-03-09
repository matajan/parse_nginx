import re
import shlex
import sys
from collections import defaultdict
from time import sleep


def parse_line(line):

    TIME = 3
    STATUS_CODE = 6

    try:
        line = re.sub(r"[\[\]]", "", line)
        data = shlex.split(line)
        result = {
            "time": data[TIME],
            "status_code": data[STATUS_CODE],
            "count": 1
        }
        return result
    except Exception as e:
        raise e


def check_arg():

    if len(sys.argv) != 2:
        print("Usage: yourscript.py /path/to/access.log")
        sys.exit(1)
    return sys.argv[1]


def open_file(LOG):

    try:
        f = open(LOG, "r")
    except FileNotFoundError:
        print(f"The file '{LOG}' does not exists!")
        sys.exit(1)
    return f


if __name__ == '__main__':

    LOGFILE = check_arg()
    f = open_file(LOGFILE)
    grouped = defaultdict(lambda: defaultdict(int))
    first = True
    f.seek(0, 2)
    current_pos = f.tell()

    try:
        while True:
            f.seek(0, 2)

            if f.tell() > current_pos:
                f.seek(current_pos)
                log_entries = [parse_line(line) for line in f]
                current_pos = f.tell()

                for entry in log_entries:
                    time = entry['time']
                    status = entry['status_code']
                    grouped[time][status] += entry['count']

                for time in sorted(grouped.keys()):
                    if first:
                        print(f"\n======== Starting")
                        first = False
                    else:
                        print(f"========")

                    for status in sorted(grouped[time].keys()):
                        count = grouped[time][status]
                        print(f"http code {status}: {count}")

                grouped = defaultdict(lambda: defaultdict(int))

            else:
                sleep(1)
                
    except KeyboardInterrupt:
        pass

    f.close()
    print(f"\n\nGood bye!")