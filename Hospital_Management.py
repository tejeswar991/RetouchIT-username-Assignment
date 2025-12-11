import csv 
import json 
import os 
from datetime import datetime 

# --- Configuration & State --- 
PATIENTS_FILE = 'patients.csv' 
APPOINTMENTS_FILE = 'appointments.csv' 
BACKUP_FILE = 'patients_backup.json' 
LOG_FILE = 'audit.log' 

# Data Stores 
patients_db = {} 
appointments_list = [] 

# --- Helper Functions for File Saving ---

def save_appointments_to_file(): 
    """Overwrites the CSV with the current list of appointments."""
    try: 
        with open(APPOINTMENTS_FILE, 'w', newline='') as f: 
            writer = csv.writer(f) 
            writer.writerow(["Date", "Time", "Doctor", "Patient_ID"]) # Header 
            writer.writerows(appointments_list) 
    except Exception as e: 
        print(f"Error saving appointments: {e}") 

def save_patients_to_file(): 
    """Overwrites the CSV with the current patient database."""
    try: 
        with open(PATIENTS_FILE, 'w', newline='') as f: 
            writer = csv.writer(f) 
            writer.writerow(["ID", "Name", "Diagnosis", "Medications"]) # Header
            for pid, data in patients_db.items(): 
                writer.writerow([pid, data['name'], data['diagnosis'], data['medications']]) 
    except Exception as e: 
        print(f"Error saving patients: {e}") 

def log_action(action_type, details_dict):  
    """Appends action to audit.log""" 
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    log_entry = f"{timestamp} | {action_type} | {json.dumps(details_dict)}\n" 
    with open(LOG_FILE, "a") as f: 
        f.write(log_entry) 

# --- Loading Functions --- 

def load_data(): 
    """Loads all data (Patients & Appointments) at startup."""
    # 1. Load Patients 
    if not os.path.exists(PATIENTS_FILE): 
        with open(PATIENTS_FILE, 'w', newline='') as f: 
            writer = csv.writer(f) 
            writer.writerow(["ID", "Name", "Diagnosis", "Medications"]) 
            writer.writerow(["101", "John Doe", "Flu", "Tamiflu"]) 
        print(f"Created dummy {PATIENTS_FILE}.") 

    try:
        with open(PATIENTS_FILE, mode='r') as file:
            reader = csv.DictReader(file) 
            for row in reader: 
                patients_db[row["ID"]] = {
                    "name": row["Name"],
                    "diagnosis": row["Diagnosis"],
                    "medications": row["Medications"]
                }
        print("Patients loaded successfully.")
    except Exception as e:
        print(f"Error loading Patients CSV: {e}")

    # 2. Load Appointments
    if os.path.exists(APPOINTMENTS_FILE):
        try:
            with open(APPOINTMENTS_FILE, mode='r') as file:
                reader = csv.reader(file)
                next(reader, None) # Skip header
                for row in reader:
                    if row: 
                        appointments_list.append(tuple(row))
            print("Appointments loaded successfully.")
        except Exception as e:
            print(f"Error loading Appointments CSV: {e}")

# --- Core Features --- 
def add_patient():
    """Adds a new patient and saves to file."""
    pid = input("Enter New Patient ID: ")
    if pid in patients_db:
        print("Error: Patient ID already exists.")
        return

    name = input("Enter Name: ")
    diagnosis = input("Enter Diagnosis: ")
    meds = input("Enter Medications: ")

    patients_db[pid] = {
        "name": name,
        "diagnosis": diagnosis,
        "medications": meds
    }
    
    # Save to file immediately
    save_patients_to_file() 
    
    # Auto-update JSON Backup
    backup_data(silent=True) 

    print(f"Patient '{name}' added and saved.") 
    log_action("ADD_PATIENT", {"pid": pid, "name": name, "diagnosis": diagnosis}) 

def schedule_appointment(): 
    """Schedules an appointment and saves to file.""" 
    pid = input("Enter Patient ID: ")
    if pid not in patients_db: 
        print("Error: Patient ID not found.") 
        return 
    
    date = input("Enter Date (YYYY-MM-DD): ")
    time = input("Enter Time (HH:MM): ")
    doctor = input("Enter Doctor Name: ")

    for appt in appointments_list:
        if appt[0] == date and appt[1] == time and appt[2] == doctor:
            print(f"Error: Dr. {doctor} is already booked at {time} on {date}.")
            return 
    new_appt = (date, time, doctor, pid) 
    appointments_list.append(new_appt) 
    
    # Save immediately
    save_appointments_to_file()
    
    print("Appointment scheduled and saved.") 
    log_action("SCHEDULE", {"date": date, "time": time, "doctor": doctor, "pid": pid}) 

def cancel_appointment(): 
    """Cancels an appointment and updates file.""" 
    pid = input("Enter Patient ID to cancel: ") 
    date = input("Enter Date of appointment: ") 
    
    found = False 
    for appt in appointments_list: 
        if appt[3] == pid and appt[0] == date: 
            appointments_list.remove(appt) 
            save_appointments_to_file() # Update file 
            print(f"Appointment for Patient {pid} on {date} canceled.") 
            log_action("CANCEL", {"date": appt[0], "time": appt[1], "doctor": appt[2], "pid": appt[3]}) 
            found = True 
            break 
    
    if not found: 
        print("Error: No matching appointment found.") 

def generate_treatment_report(): 
    """Generates report grouped by diagnosis""" 
    report = {}
    for pid, data in patients_db.items():
        diag = data['diagnosis'] 
        if diag not in report:
            report[diag] = [] 
        report[diag].append(data['name']) 
    
    print("\n--- Treatment Report (Grouped by Diagnosis) ---")
    for diag, names in report.items(): 
        print(f"{diag}: {', '.join(names)}") 
    print("-----------------------------------------------") 

def backup_data(silent=False): 
    """Backs up records to JSON""" 
    try:
        with open(BACKUP_FILE, 'w') as f: 
            json.dump(patients_db, f, indent=4)
        if not silent:
            print(f"Backup saved to {BACKUP_FILE}.")
        log_action("BACKUP", {"status": "success"})
    except Exception as e:
        print(f"Backup failed: {e}")

def rollback_actions():
    """Undoes the last 3 actions and SYNC FILES"""
    if not os.path.exists(LOG_FILE):
        print("No log file found.") 
        return 

    print("Rolling back last 3 actions...")
    with open(LOG_FILE, 'r') as f:
        lines = f.readlines() 
    
    to_undo = lines[-3:][::-1]
    
    # Remove lines from log file
    with open(LOG_FILE, 'w') as f:
        f.writelines(lines[:-3]) 

    for line in to_undo:
        try:
            parts = line.strip().split(" | ")
            action_type = parts[1]
            data = json.loads(parts[2])
            
            if action_type == "SCHEDULE":
                target = (data['date'], data['time'], data['doctor'], data['pid'])
                if target in appointments_list:
                    appointments_list.remove(target)
                    save_appointments_to_file() # Sync File
                    print(f" -> Undid SCHEDULE for {data['pid']}")
            
            elif action_type == "CANCEL":
                restored = (data['date'], data['time'], data['doctor'], data['pid'])
                appointments_list.append(restored)
                save_appointments_to_file() # Sync File
                print(f" -> Undid CANCEL for {data['pid']}")
            
            elif action_type == "ADD_PATIENT": 
                pid_to_remove = data['pid'] 
                if pid_to_remove in patients_db: 
                    del patients_db[pid_to_remove] 
                    save_patients_to_file() # Sync File
                    print(f" -> Undid ADD_PATIENT for {pid_to_remove}")

            elif action_type == "BACKUP":
                print(" -> Cannot undo file backup (skipped).")
                
        except Exception as e:
            print(f"Error parsing log line: {e}")

# --- Main ---

def main():
    global patients_db 

    load_data() # Load everything at start
    
    while True:
        print("\n=== HOSPITAL MANAGEMENT SYSTEM ===")
        print("1. List Patients")
        print("2. Add Patient")
        print("3. Schedule Appointment")
        print("4. Cancel Appointment")
        print("5. Treatment Report")
        print("6. Backup Records")
        print("7. Rollback (Last 3 Actions)")
        print("8. Show Appointments")
        print("9. Exit")
        
        choice = input("\nSelect Option: ")

        if choice == '1':
            for pid, info in patients_db.items():
                print(f"ID: {pid} | Name: {info['name']} | Diagnosis: {info['diagnosis']}")
        
        elif choice == '2':
            add_patient()

        elif choice == '3':
            schedule_appointment()

        elif choice == '4':
            cancel_appointment()

        elif choice == '5':
            generate_treatment_report()

        elif choice == '6':
            backup_data()

        elif choice == '7':
            rollback_actions()

        elif choice == '8':
            if not appointments_list:
                print("No appointments found.")
            else:
                for a in appointments_list:
                    print(f"Date: {a[0]} | Time: {a[1]} | Dr. {a[2]} | Patient: {a[3]}")

        elif choice == '9':
            print("Exiting system...")
            break
        else:
            print("Invalid selection.")

# CALL MAIN DIRECTLY
if __name__ == "__main__":
    main()