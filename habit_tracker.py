import sys  # Add this at the top of your file (if not already)

def main():
    # If run with 'ci' argument (by GitHub Actions), skip the menu
    if len(sys.argv) > 1 and sys.argv[1] == "ci":
        print("✅ CI mode: Script ran without user input.")
        return

    # Your existing while-loop menu goes here
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
