# todo.py


Task Manager in Python
A simple command-line Task Manager written in Python. This application allows you to manage your tasks with a straightforward interface. Tasks are stored persistently using a text file (tasks.txt), ensuring your data is saved between sessions.


📌 Features
➕ Add new tasks

🔍 View existing tasks

🗑 Remove tasks

💾 Persistent storage via tasks.txt

✅ Simple and easy-to-understand Python code

🛠 Project Structure
📂 tasks.txt
Stores your tasks across multiple runs.

Each line represents one task.


📄 Function BreakdownExplanation of the Code
Storing Tasks: Tasks are kept in a Python list.



File Handling:

On startup, tasks are read from tasks.txt.

Any changes (add/remove) update this file so your list persists between runs.

Functional Breakdown:

load_tasks: Loads tasks from the text file.

save_tasks: Saves all tasks back to the file.

view_tasks: Prints the current task list.

add_task: Adds user input as a new task.

remove_task: Lets user remove a task by its listed number.

main: The main interaction loop.
