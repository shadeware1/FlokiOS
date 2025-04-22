import json
import os

LOCK_FILE_PATH = '/path/to/your/floki.lock'

def read_lock_file():
    """Reads the lock file and returns its contents as a dictionary."""
    if not os.path.exists(LOCK_FILE_PATH):
        print(f"Error: {LOCK_FILE_PATH} not found.")
        return None

    with open(LOCK_FILE_PATH, 'r') as f:
        return json.load(f)

def write_lock_file(data):
    """Writes data to the lock file."""
    with open(LOCK_FILE_PATH, 'w') as f:
        json.dump(data, f, indent=4)

def update_package_version(package_name, version, checksum):
    """Updates or adds a package's version and checksum in the lock file."""
    lock_data = read_lock_file()
    if lock_data is None:
        return

    # Check for package in lock file
    package_found = False
    for package in lock_data.get('packages', []):
        if package['name'] == package_name:
            package['version'] = version
            package['checksum'] = checksum
            package_found = True
            break

    # If not found, add new package entry
    if not package_found:
        new_package = {
            'name': package_name,
            'version': version,
            'checksum': checksum,
            'dependencies': []
        }
        lock_data['packages'].append(new_package)

    write_lock_file(lock_data)
    print(f"Package {package_name} updated to version {version}.")

if __name__ == '__main__':
    # Test updating a package version and checksum
    update_package_version("core.openssh", "1.4.3", "sha256:xyz987...")
