# streamlit_app.py
import streamlit as st
import os
import datetime

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "habit_log.txt")
os.makedirs(DATA_DIR, exist_ok=True)

st.title("🧘 Habit Tracker Web App")

option = st.selectbox("Choose an action", [
    "Add Habit",
    "Mark Habit as Done",
    "View Today's Habits",
    "View Full Log"
])

if option == "Add Habit":
    habit = st.text_input("Enter new habit:")
    if st.button("Add"):
        with open(DATA_FILE, "a") as f:
            f.write(f"HABIT:{habit}\n")
        st.success(f"Habit '{habit}' added!")

elif option == "Mark Habit as Done":
    habit = st.text_input("Enter habit you completed:")
    if st.button("Mark as Done"):
        now = datetime.datetime.now()
        with open(DATA_FILE, "a") as f:
            f.write(f"DONE:{habit}:{now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        st.success(f"Marked '{habit}' as done at {now.strftime('%H:%M')}.")

elif option == "View Today's Habits":
    today = datetime.datetime.now().date()
    st.subheader(f"✔️ Habits completed today ({today}):")
    found = False
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            for line in f:
                if line.startswith("DONE"):
                    parts = line.strip().split(":")
                    name = parts[1]
                    timestamp = datetime.datetime.strptime(parts[2], '%Y-%m-%d %H:%M:%S')
                    if timestamp.date() == today:
                        st.write(f"✅ {name} at {timestamp.strftime('%H:%M')}")
                        found = True
    if not found:
        st.info("No habits marked as done today.")

elif option == "View Full Log":
    st.subheader("📜 Full Habit Log")
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            for line in f:
                if line.startswith("HABIT"):
                    st.write(f"🛠️ Created: {line.strip().split(':')[1]}")
                elif line.startswith("DONE"):
                    parts = line.strip().split(":")
                    st.write(f"✅ {parts[1]} on {parts[2]}")
    else:
        st.info("No log found yet.")
