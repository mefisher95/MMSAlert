import MMSAlert
import traceback

def main():
    try:
        print(1 / 0)
    except:
        MMSAlert.ErrorNotify(traceback.format_exc())

if __name__ == "__main__":
    main()
    MMSAlert.TerminateNotify()