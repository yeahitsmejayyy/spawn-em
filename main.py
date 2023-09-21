import os
import subprocess
import json
import time

def load_apps():
    """Loads the applications and their groups from the JSON file.
    
    Returns:
        dict: A dictionary containing app groups with their associated application configurations.
    """
    try:
        with open('apps.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_apps(app_groups):
    """Saves the app configurations to the JSON file.
    
    Args:
        app_groups (dict): The dictionary containing app groups and configurations to save.
    """
    with open('apps.json', 'w') as f:
        json.dump(app_groups, f, indent=4)

def add_app():
    """Prompts the user for details to add a new app to an app group."""
    print_groups()
    group_name = input("Enter the group name (or create a new one): ")
    app_path = input("Enter the path or name of the application to add: ")
    args = input("Enter any arguments for the application (comma separated if multiple): ").split(',')
    new_app = {'path': app_path}
    if args:
        new_app['args'] = [arg.strip() for arg in args]
    if group_name not in apps:
        apps[group_name] = []
    apps[group_name].append(new_app)
    save_apps(apps)

def remove_app():
    """Prompts the user to remove an app from an app group."""
    print_groups()
    group_name = input("Enter the group name: ")
    if group_name not in apps:
        print("Group not found.")
        return
    for i, app in enumerate(apps[group_name]):
        print(f"{i}. {app}")
    try:
        idx = int(input("Enter the number of the application to remove: "))
        apps[group_name].pop(idx)
        save_apps(apps)
    except ValueError:
        print("Invalid number entered.")
    except IndexError:
        print("Number out of range.")

def print_groups():
    """Displays all the app groups and their applications to the user."""
    for group_name, app_list in apps.items():
        print(f"\n{group_name}:")
        for i, app in enumerate(app_list):
            args_display = ', '.join(app.get('args', []))
            print(f"  {i}. {app['path']} {args_display}")

def launch_apps():
    """Prompts the user to select an app group to launch. Also allows for a delay between app launches."""
    print_groups()
    delay = int(input("Enter delay between app launches in seconds (0 for no delay): "))
    group_name = input("Enter the group name to launch or 'all' to launch everything: ")
    if group_name == 'all':
        for app_list in apps.values():
            for app in app_list:
                launch_single_app(app)
                if delay:
                    time.sleep(delay)
    elif group_name in apps:
        for app in apps[group_name]:
            launch_single_app(app)
            if delay:
                time.sleep(delay)
    else:
        print("Group not found.")

def launch_single_app(app):
    """Launches an individual app, with its associated arguments if any.
    
    Args:
        app (dict): A dictionary containing the app's path and, optionally, arguments.
    """
    try:
        if 'args' in app:
            subprocess.Popen([app['path']] + app['args'])
        else:
            subprocess.Popen(app['path'])
    except FileNotFoundError:
        print(f"Could not find or open {app}.")

if __name__ == "__main__":
    apps = load_apps()
    while True:
        """Main loop that displays the menu and prompts the user for actions."""
        print("""
 __                                    __          
/ _\_ __   __ ___      ___ __         /__\ __ ___  
\ \| '_ \ / _` \ \ /\ / / '_ \ _____ /_\| '_ ` _ \ 
_\ \ |_) | (_| |\ V  V /| | | |_____//__| | | | | |
\__/ .__/ \__,_| \_/\_/ |_| |_|     \__/|_| |_| |_|
   |_|
        Menu
        """)
        print("1. Show list of applications and groups")
        print("2. Add an application to a group")
        print("3. Remove an application from a group")
        print("4. Launch applications from a group")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            """Displays all app groups and their configurations."""
            print_groups()
        elif choice == '2':
            """Prompts the user to add a new app to a group."""
            add_app()
        elif choice == '3':
            """Prompts the user to remove an app from a group."""
            remove_app()
        elif choice == '4':
            """Prompts the user to launch apps from a specific group or all groups."""
            launch_apps()
        elif choice == '5':
            """Exits the program."""
            break
        else:
            print("Invalid choice.")

