# SPAWN-EM 🌌

![SPAWN-EM Banner](https://res.cloudinary.com/dgah9ureo/image/upload/v1695268051/spawn-em/i1xnpmp2afravttefz8h.png)

## Overview
Harness the power of **SPAWN-EM** - a CLI tool developed with principles inspired by the Jedi archives. This utility gathers your apps in harmony, much like a Jedi meditating to summon objects with the Force. Perfect for those times when you desire efficiency and focus as you embark on your coding quests.

## Motivation
Ever felt like maneuvering through a labyrinth of apps and services, similar to navigating the corridors of the Death Star? With **SPAWN-EM**, your journey becomes simpler. As Master Yoda might say, "Do, or do not. There is no try." — and with this tool, 'doing' becomes a lot more streamlined.

## Quick Start
1. Clone the repository:
    ```bash
    git clone https://github.com/yeahitsmejayyy/spawn-em.git
    ```
    ```bash
    cd spawn-em
    ```

2. Ensure Python is installed. If not, you can [download it here](https://www.python.org/downloads/).

3. Execute the program:
    ```bash
    python main.py
    ```
    or
    
    ```bash
    python3 main.py
    ```

## How to Use
The interface will guide you on your path. You can add apps, remove any unnecessary ones, or launch your pre-set configuration.

For more personalized setups, you can tailor the `apps.json`.

## Sample `apps.json` Setup
To test the balance of this tool, use this configuration:
```json
{
    "Dev": [
        {
            "path": "C:\\path\\to\\Code.exe",
            "args": ["--folder-uri=your_project_directory"]
        },
        {
            "path": "C:\\path\\to\\chrome.exe",
            "args": ["--new-window", "http://localhost:3000"]
        }
    ]
}