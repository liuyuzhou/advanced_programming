import os
import time

def modified_within(top, seconds):
    now = time.time()
    for path, dirs, files in os.walk(top):
        for name in files:
            full_path = os.path.join(path, name)
            if not os.path.exists(full_path):
                continue

            m_time = os.path.getmtime(full_path)
            if m_time > (now - seconds):
                print(f'full path is: {full_path}')

if __name__ == '__main__':
    modified_within('/advanced_programming/chapter13', float(1000))