from datetime import datetime
TOTAL_SLOTS = 10
PARKING_RATES = {
    "bike": 10,
    "car": 30,
    "heavy vehicle": 50
}
parking_slots = {i: None for i in range(1, TOTAL_SLOTS + 1)}
def display_menu():
    print("\n" + "=" * 40)
    print("   SMART PARKING FEE MANAGEMENT")
    print("=" * 40)
    print("1. Park Vehicle")
    print("2. Exit Vehicle and Pay Fee")
    print("3. View Available Slots")
    print("4. View Parking Records")
    print("5. Exit")
    print("=" * 40)
def park_vehicle():
    vehicle_number = input("Enter vehicle number: ").strip().upper()
    if not vehicle_number:
        print("Error: Vehicle number cannot be empty.")
        return
    for record in parking_slots.values():
        if record and record["vehicle_number"] == vehicle_number:
            print("This vehicle is already parked.")
            return
    vehicle_type = input(
        "Enter vehicle type (bike/car/heavy vehicle): "
    ).strip().lower()
    if vehicle_type not in PARKING_RATES:
        print("Invalid vehicle type!")
        return
    available_slot = None
    for slot, record in parking_slots.items():
        if record is None:
            available_slot = slot
            break
    if available_slot is None:
        print("Parking is full!")
        return
    entry_time = datetime.now()
    parking_slots[available_slot] = {
        "vehicle_number": vehicle_number,
        "vehicle_type": vehicle_type,
        "entry_time": entry_time
    }
    print("\nVehicle parked successfully!")
    print("Vehicle Number:", vehicle_number)
    print("Vehicle Type:", vehicle_type.title())
    print("Parking Slot:", available_slot)
    print("Entry Time:", entry_time.strftime("%d-%m-%Y %H:%M:%S"))
def exit_vehicle():
    print("\n--- VEHICLE EXIT ---")
    try:
        slot = int(input("Enter parking slot number: "))
    except ValueError:
        print("Please enter a valid slot number.")
        return
    if slot not in parking_slots:
        print("Invalid parking slot!")
        return
    record = parking_slots[slot]
    if record is None:
        print("This parking slot is already empty.")
        return
    exit_time = datetime.now()
    entry_time = record["entry_time"]
    duration_seconds = (exit_time - entry_time).total_seconds()
    hours = max(1, int((duration_seconds + 3599) // 3600))
    vehicle_type = record["vehicle_type"]
    rate = PARKING_RATES[vehicle_type]
    total_fee = hours * rate
    print("Vehicle Number:", record["vehicle_number"])
    print("Vehicle Type:", vehicle_type.title())
    print("Parking Slot:", slot)
    print("Entry Time:", entry_time.strftime("%d-%m-%Y %H:%M:%S"))
    print("Exit Time:", exit_time.strftime("%d-%m-%Y %H:%M:%S"))
    print("Parking Duration:", hours, "hour(s)")
    print("Hourly Rate: Rs.", rate)
    print("Total Fee: Rs.", total_fee)
    payment = input("Confirm payment received? (yes/no): ").strip().lower()
    if payment == "yes":
        print("Payment successful!")
        print("Thank you for using Smart Parking!")

        parking_slots[slot] = None
    else:
        print("Payment not completed.")
        print("Vehicle remains in its parking slot.")


def view_available_slots():
    print("\n--- PARKING SLOT STATUS ---")

    available = 0
    for slot, record in parking_slots.items():
        if record is None:
            print(f"Slot {slot}: Available")
            available += 1
        else:
            print(
                f"Slot {slot}: Occupied "
                f"({record['vehicle_number']})"
            )
    print("\nTotal Slots:", TOTAL_SLOTS)
    print("Available Slots:", available)
    print("Occupied Slots:", TOTAL_SLOTS - available)
def view_parking_records():
    print("\n--- CURRENT PARKING RECORDS ---")
    found = False
    for slot, record in parking_slots.items():
        if record is not None:
            found = True
            print("\nSlot Number:", slot)
            print("Vehicle Number:", record["vehicle_number"])
            print("Vehicle Type:", record["vehicle_type"].title())
            print(
                "Entry Time:",
                record["entry_time"].strftime("%d-%m-%Y %H:%M:%S")
            )
    if not found:
        print("No vehicles are currently parked.")
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            park_vehicle()
        elif choice == "2":
            exit_vehicle()
        elif choice == "3":
            view_available_slots()
        elif choice == "4":
            view_parking_records()
        elif choice == "5":
            print("Thank you for using Smart Parking!")
            break
        else:
            print("Invalid choice! Please select 1 to 5.")
if __name__ == "__main__":
    main()