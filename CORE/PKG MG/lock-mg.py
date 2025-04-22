import json
import os
from iris_lock import generate_lockfile, validate_lockfile
from lockfile_handler import read_lock_file, write_lock_file, update_package_version

LOCK_FILE_PATH = '/path/to/your/floki.lock'

def list_installed_packages():
    """Lists all installed packages from the lock file."""
    lock_data = read_lock_file()
    if lock_data is None:
        return []

    packages = lock_data.get('packages', [])
    for package in packages:
        print(f"{package['name']} - Version: {package['version']}")
    return packages

def add_package_to_lockfile(package_name, version, checksum):
    """Adds a new package to the lock file."""
    update_package_version(package_name, version, checksum)

def remove_package_from_lockfile(package_name):
    """Removes a package from the lock file."""
    lock_data = read_lock_file()
    if lock_data is None:
        return

    lock_data['packages'] = [pkg for pkg in lock_data['packages'] if pkg['name'] != package_name]
    write_lock_file(lock_data)
    print(f"Package {package_name} removed from lock file.")

def update_package(package_name, version, checksum):
    """Updates an existing package version in the lock file."""
    update_package_version(package_name, version, checksum)

def main():
    # Ensure the lockfile exists or generate one if not
    if not os.path.exists(LOCK_FILE_PATH):
        print("Lock file does not exist, generating new one...")
        packages = [
            {
                "name": "core.openssh",
                "version": "1.4.2",
                "checksum": "sha256:e3b0c4...",
                "dependencies": []
            }
        ]
        generate_lockfile("3.18.191", packages)
    
    # List installed packages
    list_installed_packages()

    # Update a package example
    update_package("core.openssh", "1.4.3", "sha256:xyz987...")

    # Remove a package example
    remove_package_from_lockfile("core.zlib")

if __name__ == '__main__':
    main()
