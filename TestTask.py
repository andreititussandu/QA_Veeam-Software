import os
import shutil
import time

def sync_folders(source_folder, replica_folder):
    source_files = os.listdir(source_folder)
    
    if not os.path.exists(replica_folder):
        os.makedirs(replica_folder)
    
    for file in source_files:
        source_file = os.path.join(source_folder, file)
        replica_file = os.path.join(replica_folder, file)
        shutil.copy(source_file, replica_file)
    
    replica_files = os.listdir(replica_folder)
    for file in replica_files:
        replica_file = os.path.join(replica_folder, file)
        if file not in source_files:
            os.remove(replica_file)

source_folder = "C:/SourceFolder"
replica_folder = "C:/ReplicaFolder"
while True:
    sync_folders(source_folder, replica_folder)
    time.sleep(5)