import time
from datetime import datetime

class PillRobot:
    def __init__(self, patient_name):
        self.name = patient_name
        self.pills_taken = 0
        self.schedule = {
            "08:00": "Coartem - Malaria",
            "14:00": "Vitamin C",
            "20:00": "Coartem - Malaria"
        }
        print(f"Hello {self.name}! I am your Pill Robot.")
        print(f"Your schedule: {self.schedule}")
        print("-" * 40)

    def check_time(self):
        return datetime.now().strftime("%H:%M")

    def remind(self, drug_name, demo_mode=False):
        print("\n" + "!" * 40)
        print(f"BEEP BEEP! Time to take {drug_name}")
        print(f"Time: {self.check_time()}")
        print("!" * 40)
        print(f"[Robot voice]: {self.name}, please take your {drug_name} now.")

        if demo_mode:
            taken = "yes"
            print("Did you take it? (yes/no): yes [auto for demo]")
        else:
            taken = input("Did you take it? (yes/no): ").lower()

        if taken == "yes":
            self.pills_taken += 1
            print(f"Good job! Pills taken today: {self.pills_taken}")
            self.save_log(drug_name, "TAKEN")
        else:
            print("Okay, I will remind you again in 5 minutes!")
            self.save_log(drug_name, "MISSED")

    def save_log(self, drug, status):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("pill_log.txt", "a") as f:
            f.write(f"{timestamp} - {drug} - {status}\n")
        print("Log saved to pill_log.txt")

    def daily_report(self):
        print("\n--- DAILY REPORT ---")
        print(f"Patient: {self.name}")
        print(f"Total pills taken: {self.pills_taken}")
        if self.pills_taken >= 2:
            print("Excellent compliance! Keep it up.")
        else:
            print("Try to remember all drugs tomorrow.")

# --- DEMO RUN ---
robot = PillRobot("Mama PH")
print("\n[DEMO MODE - faking time]")

test_times = ["08:00", "10:30", "14:00", "20:00"]

for fake_time in test_times:
    print(f"\n[Clock: {fake_time}] Checking...")
    if fake_time in robot.schedule:
        robot.remind(robot.schedule[fake_time], demo_mode=True)
    else:
        print("No drugs now. Resting...")
    time.sleep(1)

robot.daily_report()
print("\nRobot says: Stay healthy, drink water!")