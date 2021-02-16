import psutil

bad_process_names = {
                    'vmms.exe',
                    'com.docker.service',
                    'vmcompute.exe',
                    'SkypeBackgroundHost.exe',
                    'SkypeApp.exe',
}


def process_killing(process_names_collection):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] in process_names_collection:
            p = psutil.Process(proc.info['pid'])
            try:
                p.kill()
            except psutil.AccessDenied:
                print("Process " + proc.info['name'] + " (pid=" + str(proc.info['pid']) +
                      ") was not killed (psutil.AccessDenied).")


if __name__ == '__main__':
    process_killing(bad_process_names)
