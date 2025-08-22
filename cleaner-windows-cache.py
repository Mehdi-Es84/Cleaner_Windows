import os
import shutil

def clean_temp():
    temp_dir = os.environ.get('TEMP')
    if temp_dir and os.path.exists(temp_dir):
        for filename in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir , filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                print(f"deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting: {file_path}: {e}")   
    else:
        print("Temp directory not found.")
        
def clean_prefetch():
    prefetch_dir = r"C:\Windows\Prefetch"
    if os.path.exists(prefetch_dir):
        for filename in os.listdir(prefetch_dir):
            file_path = os.path.join(prefetch_dir , filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                print(f"deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting: {file_path}: {e}")
    else:
        print("Prefetch directory not found.")
        
def clean_windows_temp():
    windows_temp_dir = r"C:\Windows\Temp"
    if os.path.exists(windows_temp_dir):
        for filename in os.listdir(windows_temp_dir):
            file_path = os.path.join(windows_temp_dir , filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                print(f"deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting: {file_path}: {e}")
    else:
        print("Windows Temp directory not found.")
        
        
if __name__ == "__main__":
    print('Start cleaning . . .')
    clean_temp()
    clean_prefetch()
    clean_windows_temp()
    print("Cleaning is finished!.")