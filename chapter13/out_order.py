import subprocess

out_bytes = subprocess.check_output(['netstat','-a'])


out_text = out_bytes.decode('utf-8')


try:
    out_bytes = subprocess.check_output(['cmd','arg1','arg2'])
except subprocess.CalledProcessError as e:
    out_bytes = e.output       # Output generated before error
    code      = e.returncode   # Return code


out_bytes = subprocess.check_output(['cmd','arg1','arg2'],
                                    stderr=subprocess.STDOUT)


try:
    out_bytes = subprocess.check_output(['cmd','arg1','arg2'], timeout=5)
except subprocess.TimeoutExpired as e:
    ...


out_bytes = subprocess.check_output('grep python | wc > out', shell=True)