# import pickle

# class Task:
#     def __init__(self, name, description, status=False):
#         self.name = name
#         self.description = description
#         self.status = status

#     def mark_complete(self):
#         self.status = True

#     def __str__(self):
#         return f"Task: {self.name}\nDescription: {self.description}\nStatus: {'Complete' if self.status else 'Incomplete'}\n"

# class TaskManager:
#     def __init__(self):
#         self.tasks = []

#     def add_task(self, task):
#         self.tasks.append(task)

#     def view_tasks(self):
#         if not self.tasks:
#             print("No tasks found.")
#         else:
#             print("==== View Tasks ====")
#             for i, task in enumerate(self.tasks, 1):
#                 print(f"{i}. {task}")

#     def mark_task_complete(self):
#         self.view_tasks()
#         task_number = int(input("Enter the task number: ")) - 1
#         if 0 <= task_number < len(self.tasks):
#             self.tasks[task_number].mark_complete()
#             print("Task marked as complete!")
#         else:
#             print("Invalid task number.")

#     def delete_task(self):
#         self.view_tasks()
#         task_number = int(input("Enter the task number: ")) - 1
#         if 0 <= task_number < len(self.tasks):
#             del self.tasks[task_number]
#             print("Task deleted successfully!")
#         else:
#             print("Invalid task number.")

#     def save_tasks(self, filename):
#         with open(filename, 'wb') as file:
#             pickle.dump(self.tasks, file)

#     def load_tasks(self, filename):
#         try:
#             with open(filename, 'rb') as file:
#                 self.tasks = pickle.load(file)
#         except FileNotFoundError:
#             self.tasks = []

#     def display_menu(self):
#         print("==== Task Manager ====")
#         print("1. Add Task")
#         print("2. View Tasks")
#         print("3. Mark Task as Complete")
#         print("4. Delete Task")
#         print("5. Exit")

#     def run(self):
#         while True:
#             self.display_menu()
#             choice = input("Enter your choice: ")
#             if choice == '1':
#                 name = input("Enter the task name: ")
#                 description = input("Enter the task description: ")
#                 task = Task(name, description)
#                 self.add_task(task)
#                 print("Task added successfully!")
#             elif choice == '2':
#                 self.view_tasks()
#             elif choice == '3':
#                 self.mark_task_complete()
#             elif choice == '4':
#                 self.delete_task()
#             elif choice == '5':
#                 self.save_tasks('tasks.pkl')
#                 print("Tasks saved.")
#                 break
#             else:
#                 print("Invalid input! Please enter a valid option.")

# if __name__ == "__main__":
#     task_manager = TaskManager()
#     task_manager.load_tasks('tasks.pkl')
#     task_manager.run()

import pickle
class Task:
    def __init__(self,name,description,status=False):
        self.name=name
        self.description=description
        self.status=status
        
    def mark_task(self):
        self.status=True
    def __str__(self) -> str:
        return f"task :{self.name}\ndescription : {self.description}\n status : {self.status}"
class TaskManager:
    def __init__(self):
        self.task=[]
    def add_task(self,task):
        self.task.append(task)
        print('task added succesfuly !')
    def view_task(self):
        if not self.task:
            print(' task not found')        
        else:
            ('task list :')
            for i,j in enumerate(self.task,1):
                print(f'{i} .{j}')
    def remove_task(self):
        self.view_task()
        task_no =int(input('enter the number:'))-1
        if 0<=task_no<len(self.task)-1:
            del self.task[task_no]
        else:
            print('somthing wrong in your input')
    def Mark_Task(self):
        self.view_task()
        which=input('enter number task to mark sucsefully')-1
        if 0<=which<len(self.task):
            self.task[which].mark_task()
    def save_task(self,filename):
        with open(filename,'wb') as file:
            pickle.dump(self.task,file)
    def load_task(self,filename):
        try:
            with open(filename,'rb') as file:
               self.task= pickle.load(file)
        except FileNotFoundError:
            self.task=[]
    def Display_menu(self):
          print("==== Task Manager ====")
          print("1. Add Task")
          print("2. View Tasks")
          print("3. Mark Task as Complete")
          print("4. Delete Task")
          print("5. Exit")
    def run(self):
        while True:
            self.Display_menu()
            chois =int(input('enter the choise:'))
            if chois==1:
                name=input('enter the taske:')
                description=input('enter the description :')
                task =Task(name,description)
                self.add_task(task)
            elif chois==2:
                self.view_task()
            elif chois==3:
                self.Mark_Task()
            elif chois==4:
                self.remove_task()
            elif chois==5:
                self.save_task('new.pkl')
                print('task added succesfuly !')
                break
            
                  
if __name__=='__main__':
    object=TaskManager()
    object.save_task('new.pkl')
    object.run()