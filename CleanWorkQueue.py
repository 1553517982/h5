import os


def CleanWorkQueque(folder):
    exefolder = os.getcwd()
    os.chdir(folder+"/.svn")
    os.system("{}/sqlite3.exe wc.db \"select * from work_queue\"".format(exefolder))
    os.system("{}/sqlite3.exe wc.db \"delete from work_queue\"".format(exefolder))
    os.system("{}/sqlite3.exe wc.db \"delete from wc_lock\"".format(exefolder))
    os.chdir(folder)

if __name__ == "__main__":
    folder=os.getcwd()
    if len(sys.argv) >1:
        folder = sys.argv[1]
    CleanWorkQueque(folder)
