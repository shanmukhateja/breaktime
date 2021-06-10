from .counter import SessionCounter

global counter

def action_new_session(tray):
    global counter
    counter = SessionCounter(tray)

def action_stop_session(tray):
    try:
        global counter
        counter.stop_session()
    except NameError:
        print("No active session")
