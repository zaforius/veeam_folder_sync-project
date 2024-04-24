import os
import shutil
import argparse
import logging
import time
from hashlib import md5

def calculate_md5(file_path):
    hash_md5 = md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def sync_folders(source, replica):
    source_files = {os.path.join(dp, f): calculate_md5(os.path.join(dp, f)) for dp, dn, filenames in os.walk(source) for f in filenames}
    replica_files = {os.path.join(dp, f): calculate_md5(os.path.join(dp, f)) for dp, dn, filenames in os.walk(replica) for f in filenames}

    # Remove files that are in replica but not in source
    for replica_file in list(replica_files.keys()):
        if replica_file.replace(replica, source) not in source_files:
            logging.info(f'Removing: {replica_file}')
            os.remove(replica_file)

    # Copy new files and update changed files
    for source_file, source_hash in source_files.items():
        replica_file = source_file.replace(source, replica)
        if replica_file not in replica_files or source_hash != replica_files[replica_file]:
            replica_dir = os.path.dirname(replica_file)
            if not os.path.exists(replica_dir):
                os.makedirs(replica_dir)
            logging.info(f'Copying: {source_file} to {replica_file}')
            shutil.copy2(source_file, replica_file)

def main():
    parser = argparse.ArgumentParser(description='Synchronize two folders.')
    parser.add_argument('source', type=str, help='Source directory path')
    parser.add_argument('replica', type=str, help='Replica directory path')
    parser.add_argument('--interval', type=int, default=60, help='Sync interval in seconds')
    parser.add_argument('--log', type=str, default='sync.log', help='Log file path')

    args = parser.parse_args()

    logging.basicConfig(filename=args.log, level=logging.INFO, format='%(asctime)s - %(message)s')

    while True:
        sync_folders(args.source, args.replica)
        time.sleep(args.interval)

if __name__ == "__main__":
    main()