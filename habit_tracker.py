import os
import datetime

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "habit_log.txt")

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

def add_habit():
    habit = input("📝 Enter the name of the habit you want to track: ").strip()
    with open(DATA_FILE, "a") as f:
        f.write(f"HABIT:{habit}\n")
    print(f"✅ Habit '{habit}' added successfully!")

def mark_habit_done():
    habit = input("✅ Enter the habit you completed: ").strip()
    now = datetime.datetime.now()
    with open(DATA_FILE, "a") as f:
        f.write(f"DONE:{habit}:{now.strftime('%Y-%m-%d %H:%M:%S')}\n")
    print(f"🎉 Great job! Habit '{habit}' marked as completed at {now.strftime('%H:%M')}.")

def view_today_habits():
    today = datetime.datetime.now().date()
    print(f"\n📅 Habits completed today ({today}):\n")
    found = False
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            for line in f:
                if line.startswith("DONE"):
                    parts = line.strip().split(":")
                    habit_name = parts[1]
                    timestamp = datetime.datetime.strptime(parts[2], '%Y-%m-%d %H:%M:%S')
                    if timestamp.date() == today:
                        print(f"✔️ {habit_name} at {timestamp.strftime('%H:%M')}")
                        found = True
    if not found:
        print("😅 You haven't completed any habits today yet. Get going!")

def view_all_logs():
    print("\n📜 Full Habit Log:\n")
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            for line in f:
                if line.startswith("HABIT"):
                    print(f"🛠️ Created habit: {line.strip().split(':')[1]}")
                elif line.startswith("DONE"):
                    parts = line.strip().split(":")
                    print(f"✅ {parts[1]} completed on {parts[2]}")
    else:
        print("📂 No log found yet. Start adding habits!")

def main():
    while True:
        print("\n============================")
        print("  🧘 Habit Tracker Console App")
        print("============================")
        print("1. Add New Habit")
        print("2. Mark Habit as Done")
        print("3. View Today's Completed Habits")
        print("4. View Full Habit Log")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_habit()
        elif choice == "2":
            mark_habit_done()
        elif choice == "3":
            view_today_habits()
        elif choice == "4":
            view_all_logs()
        elif choice == "5":
            print("👋 Exiting Habit Tracker. Stay consistent!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
