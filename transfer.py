import shutil
import dotenv
import os

def copy_files_overwrite(src, dst):
    # check path destination
    if not os.path.exists(dst):
        os.makedirs(dst)

    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copy_files_overwrite(s, d)
        else:
            shutil.copy(s, d) 

def main():
    source = os.environ.get("CSV_SOURCE")
    destination = os.environ.get("CSV_DESTINATION")

    if not source or not destination:
        print("Path not found.")
        return

    try:
        copy_files_overwrite(source, destination)
    except Exception as e:
        print(f"Error copying files: {e}")

if __name__ == "__main__":
    dotenv.load_dotenv(dotenv.find_dotenv(), override=True)
    main()
