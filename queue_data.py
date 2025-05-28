import redis
import time
import os

TXT_DIR = "/app/txt"

os.makedirs(TXT_DIR, exist_ok=True)
r = redis.Redis(host='redis', port=6379, db=0)
def write_from_queue():
    while True:
        item = r.blpop('data_queue', timeout=5)
        if item:
            _, data = item
            data = data.decode('utf-8')
            lines = data.splitlines()
            if not lines:
                continue
            line_no = lines[0].strip()
            filename = f"{TXT_DIR}/PC-{line_no}.txt"

            # with open(filename, "a", encoding="utf-8") as f: # append
            with open(filename,"w",encoding="utf-8") as f: # not append
                f.write(data + "\n")
                print(f"record to {filename}: {data}")
        else:
            time.sleep(1)
if __name__ == "__main__":
    write_from_queue()
