import json
import os

LOCK_FILE_PATH = '/path/to/your/floki.lock'

def lockfile_exists():
    """Checks if the lock file exists."""
    return os.path.exists(LOCK_FILE_PATH)

def generate_lockfile(iris_version, packages):
    """Generates the initial lock file with Iris version and package details."""
    lock_data = {
        "lock_version": "1.0",
        "iris_version": iris_version,
        "packages": packages,
        "metadata": {
            "lockfile_created_at": "2025-04-22T12:00:00Z",
            "generated_by": "Iris Package Manager v3.18.191"
        }
    }
    with open(LOCK_FILE_PATH, 'w') as f:
        json.dump(lock_data, f, indent=4)
    print("Lock file generated.")

def validate_lockfile():
    """Validates the integrity of the lock file."""
    if not lockfile_exists():
        print(f"Error: {LOCK_FILE_PATH} not found.")
        return False

    with open(LOCK_FILE_PATH, 'r') as f:
        lock_data = json.load(f)

    # Perform any necessary validation (e.g., check required fields)
    if 'iris_version' not in lock_data:
        print("Error: Iris version missing in lock file.")
        return False

    return True

if __name__ == '__main__':
    # Example for generating a lock file
    packages = [
        {
            "name": "core.openssh",
            "version": "1.4.2",
            "checksum": "sha256:e3b0c4...",
            "dependencies": []
        },
        {
            "name": "core.zlib",
            "version": "1.2.11",
            "checksum": "sha256:xyz789...",
            "dependencies": []
        }
    ]

    generate_lockfile("3.18.191", packages)
