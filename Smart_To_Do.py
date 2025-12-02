import time

class SmartCompanion:
    def __init__(self):
        # --- 1. Data Structures ---
        # List of dictionaries for tasks
        self.tasks = [] 
        self.task_counter = 1
        
        # Dictionary for habits (Key: Name, Value: Streak Count)
        self.habits = {
            "Drink Water": 0, 
            "Exercise": 0, 
            "Read": 0,
            "Code": 0
        }

    # --- Feature: Task Management ---
    def add_task(self, title):
        new_task = {
            'id': self.task_counter,
            'title': title,
            'completed': False
        }
        self.tasks.append(new_task)
        self.task_counter += 1
        print(f"✅ Added task: '{title}'")

    def view_tasks(self):
        print("\n--- 📝 Your To-Do List ---")
        if not self.tasks:
            print("No tasks yet! Add some to get started.")
        else:
            for t in self.tasks:
                status = "[x]" if t['completed'] else "[ ]"
                print(f"{t['id']}. {status} {t['title']}")
        print("--------------------------")

    def mark_task_done(self):
        self.view_tasks()
        if not self.tasks: return

        try:
            task_id_input = input("Enter ID of task to mark done: ")
            if not task_id_input.isdigit():
                print("❌ Please enter a valid number.")
                return

            task_id = int(task_id_input)
            
            # Find task by ID
            found = False
            for t in self.tasks:
                if t['id'] == task_id:
                    t['completed'] = True
                    found = True
                    print(f"🎉 Great job! '{t['title']}' is marked done.")
                    break
            
            if not found:
                print("❌ Task ID not found.")
                
        except ValueError:
            print("❌ Invalid input.")

    # --- Feature: Habit Tracking (Improved) ---
    def track_habits(self):
        print("\n--- 🌱 HABIT TRACKER ---")
        print("Which habit did you complete today?")
        
        # Get list of keys to index them
        habit_list = list(self.habits.keys())
        
        # Display habits with index and visual streak bar
        for i, habit in enumerate(habit_list, 1):
            streak = self.habits[habit]
            visual_bar = "🔥" * streak if streak > 0 else "" 
            print(f"{i}. {habit:<12} | Streak: {streak} {visual_bar}")
            
        print("------------------------")
        choice_input = input("Enter number (or 0 to cancel): ")
        
        if choice_input.isdigit():
            choice = int(choice_input)
            if 0 < choice <= len(habit_list):
                selected_habit = habit_list[choice - 1]
                self.habits[selected_habit] += 1
                print(f"🚀 Boom! Streak increased! {selected_habit} is now at {self.habits[selected_habit]}.")
            elif choice == 0:
                print("Cancelled.")
            else:
                print("❌ Invalid choice number.")
        else:
            print("❌ Please enter a number.")

    # --- Feature: Wellness Insight (The Brain) ---
    def get_wellness_insight(self):
        print("\n" + "="*30)
        print("   🧠 DAILY WELLNESS REPORT   ")
        print("="*30)

        # --- STEP 1: Gather Data ---
        total_tasks = len(self.tasks)
        
        # Guard Clause: Prevent division by zero
        if total_tasks == 0:
            print("❌ No tasks found. Add tasks to generate an insight!")
            return

        # Count completed tasks
        completed_count = sum(1 for t in self.tasks if t['completed'])
        
        # Calculate Percentage
        score_percent = (completed_count / total_tasks) * 100
        
        # Calculate Habit Points (Sum of all streaks)
        habit_points = sum(self.habits.values())

        # --- STEP 2: The Visual Progress Bar ---
        # Logic: Create a 10-block bar
        blocks = int(score_percent // 10) 
        progress_bar = "█" * blocks + "░" * (10 - blocks)

        print(f"Task Progress: {progress_bar} {int(score_percent)}%")
        print(f"Habit Bonus Points: +{habit_points}")

        # --- STEP 3: The Insight Engine (Feedback Logic) ---
        print("\n📢 INSIGHT:")
        
        if score_percent == 100:
            if habit_points > 5:
                print("🌟 GOD MODE: Perfect tasks and high habits! You are unstoppable.")
            else:
                print("🏆 PERFECTION: All tasks done. Now, work on those habits!")
                
        elif score_percent >= 75:
            print("🔥 STRONG FINISH: You're crushing it. Just a little more!")
            
        elif score_percent >= 50:
            print("👍 ON TRACK: You're halfway there. Don't stop now.")
            
        elif score_percent > 0:
            print("🌱 GOOD START: Progress is progress, no matter how small.")
            
        else:
            print("☕ BREATHE: It looks like a slow start. Pick the easiest task and do it now!")

        print("="*30 + "\n")

# --- Main Application Loop ---
def main():
    app = SmartCompanion()
    
    while True:
        print("\n=== 🧠 Smart Companion ===")
        print("1. ➕ Add Task")
        print("2. 📝 View Tasks")
        print("3. ✅ Mark Task Done")
        print("4. 🌱 Log Habit")
        print("5. 📊 Get Wellness Insight")
        print("6. 🚪 Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            t = input("Enter task name: ")
            app.add_task(t)
        elif choice == '2':
            app.view_tasks()
        elif choice == '3':
            app.mark_task_done()
        elif choice == '4':
            app.track_habits()
        elif choice == '5':
            app.get_wellness_insight()
        elif choice == '6':
            print("Goodbye! Stay productive. 👋")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()