class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("✅ Creating new DatabaseConnection instance...")
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        else:
            print("⚠️ Using existing DatabaseConnection instance!")
        return cls._instance

# --- Testing Singleton Behavior ---
print("--- 1st Call ---")
db1 = DatabaseConnection()

print("\n--- 2nd Call ---")
db2 = DatabaseConnection()

print("\n--- Verification ---")
print("Are db1 and db2 the exact same object in memory?", db1 is db2)