from playsound import playsound
import time 

WORKING_TIME = 45 * 60.0
REST_TIME = 10 * 60.0
SLEEP_TIME = 10
SOUND_FILE = 'snd/chime.wav'

beginning_work = beginning_rest = time.time()
working = True


def clear_line():
    print("                                        ", end="\r")


def signal_end():
    playsound(SOUND_FILE)
    clear_line()


def stop_working(work, start_time):
    now = time.time()
    return work and ((now - start_time) >= WORKING_TIME)


def stop_resting(work, start_time):
    now = time.time()
    return not work and ((now - start_time) >= REST_TIME)

states = {}
states[True]  = "Work"
states[False] = "Rest"

def start_state(current):
    global working, states
    working = not current
    clear_line()
    print(f"{states[current]} time is over.", end="\r")
    signal_end()
    return time.time()

def is_working():
    global working
    return working


print("Work Timer 0.1")
while True:
    if stop_working(working, beginning_work):
        beginning_rest = start_state(working)
    if stop_resting(working, beginning_rest):
        beginning_work = start_state(working)
    if is_working():
        percent = (time.time() - beginning_work) / WORKING_TIME * 100.0
        print(f"Work: {percent:.2f}% done", end='\r')
    else:
        percent = (time.time() - beginning_rest) / REST_TIME * 100.0
        print(f"Rest: {percent:.2f}% done", end='\r')
    time.sleep(SLEEP_TIME)