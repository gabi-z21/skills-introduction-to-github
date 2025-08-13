import json
import os
""" this is a mini project to make a task tracker that can add, update, save, load 
and delete tasks """
class TaskTracker:
    def __init__(self, tasks):
        self.tasks = tasks
        self.load_tasks() #load tasks from files when object is created

    def load_tasks(self):
        try:
            if os.path.exists("tasks.txt"): #check if file exists
               with open("tasks.txt", "r") as file:
                  self.tasks = json.load(file)
        except: # if file is not found or any other error occurs, start with empty list
            self.tasks = []

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            json.dump(self.tasks, file) # save tasks to file 
#add task to file
    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print("task added succesfully!")
#delete task from file
    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            self.save_tasks()
            print("task is delted")
        else:
            print("task not found")
#update an already existing task
    def update_task(self, old_task, task):
        if old_task in self.tasks:
            self.old_task = old_task
            self.task = task
            index = self.tasks.index(old_task)
            self.tasks[index] = task
            self.save_tasks()
            print("you have updated the task")
        else:
            print("the task you entered was not found")

#view all tasks in the file
    def view_tasks(self):
       if self.tasks:
           for task in self.tasks:
               print(task)
       else:
           print("No task was found!")

task_tracker = TaskTracker([])

#create the menu loop
while True:
    print("Task tracker menu\n")
    print("1.Add task\n")
    print("2.Delete task\n")
    print("3.Update task\n")
    print("4.View tasks\n")
    print("5.Exit\n")

    choice = input("Enter your choice: ")

  

    match choice:
        case "1":
            task = input("Enter the task to add: ")
            task_tracker.add_task(task)
            
        case "2":
            task = input("Enter the task to delete: ")
            task_tracker.delete_task(task)
          
        case "3":
            old_task = input("Enter the task to update: ")
            task = input("Enter the new task: ")
            task_tracker.update_task(old_task, task)
          
        case "4":
            task_tracker.view_tasks()
        case "5":
            print("Exiting...")
            break

task_tracker.view_tasks()
