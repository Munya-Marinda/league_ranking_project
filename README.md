# League Ranking Project

## Overview

This project calculates the ranking table for a league based on match results. The application takes match results as input and outputs the league rankings based on points.

## Install packages

```bash
pip install -r requirements.txt
```

## Setup

Run the application with the following command (the -m flag in Python is used to run a module as a script.):

```bash
python -m league_ranking.main
```

## Run test

The -m flag in Python is used to run a module as a script.

```bash
python -m pytest tests/test_league_table.py
```

<br/>
<br/>

# Instructions for Creating a Virtual Environment

## Creating a Virtual Environment on macOS

1. **Open Terminal**: You can find Terminal in the Applications > Utilities folder or by searching for it in Spotlight.

2. **Navigate to Your Project Directory**:
   Use the `cd` command to navigate to your project folder. Replace `path/to/your/project` with your actual project path.

   ```bash
   cd path/to/your/project
   ```

3. **Create a Virtual Environment**:
   Run the following command to create a virtual environment named `venv`:

   ```bash
   python3 -m venv venv
   ```

4. **Activate the Virtual Environment**:
   Activate the virtual environment by running:

   ```bash
   source venv/bin/activate
   ```

   You should see the name of your virtual environment (`(venv)`) in your terminal prompt, indicating that the virtual environment is active.

5. **Install Required Packages**:
   After activating the virtual environment, install any required packages specified in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

6. **Deactivate the Virtual Environment**:
   To deactivate the virtual environment when you're done, simply run:

   ```bash
   deactivate
   ```

---

## Creating a Virtual Environment on Windows

1. **Open Command Prompt**: You can find Command Prompt by searching for it in the Start menu.

2. **Navigate to Your Project Directory**:
   Use the `cd` command to navigate to your project folder. Replace `path\to\your\project` with your actual project path.

   ```cmd
   cd path\to\your\project
   ```

3. **Create a Virtual Environment**:
   Run the following command to create a virtual environment named `venv`:

   ```cmd
   python -m venv venv
   ```

4. **Activate the Virtual Environment**:
   Activate the virtual environment by running:

   ```cmd
   venv\Scripts\activate
   ```

   You should see the name of your virtual environment (`(venv)`) in your command prompt, indicating that the virtual environment is active.

5. **Install Required Packages**:
   After activating the virtual environment, install any required packages specified in `requirements.txt`:

   ```cmd
   pip install -r requirements.txt
   ```

6. **Deactivate the Virtual Environment**:
   To deactivate the virtual environment when you're done, simply run:

   ```cmd
   deactivate
   ```
