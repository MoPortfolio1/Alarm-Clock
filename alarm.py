import time
import winsound


UNITS = {
    "hours": (3600, "hour", "hours", "How many hours: "),
    "mins": (60, "min", "mins", "How many mins: "),
    "sec": (1, "second", "seconds", "How many seconds: "),
}


def get_duration():
    while True:
        unit = input("Hours, mins, or sec: ").strip().lower()
        if unit not in UNITS:
            print("Please enter hours, mins, or sec.")
            continue

        multiplier, _, _, prompt = UNITS[unit]
        try:
            amount = int(input(prompt))
        except ValueError:
            print("Please enter a whole number greater than zero.")
            continue

        if amount <= 0:
            print("Please enter a whole number greater than zero.")
            continue

        return amount * multiplier, amount, unit


def sound():
    try:
        for _ in range(3):
            winsound.Beep(1000, 1000)
            time.sleep(0.5)
    except (RuntimeError, OSError) as error:
        print(f"Could not play the alarm sound: {error}")


def main():
    waiting_time, amount, unit = get_duration()
    _, singular, plural, _ = UNITS[unit]
    label = singular if amount == 1 else plural
    print(f"Your alarm is set for {amount} {label}.")
    time.sleep(waiting_time)
    sound()


if __name__ == "__main__":
    main()
    
