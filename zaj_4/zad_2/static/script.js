document.addEventListener("DOMContentLoaded", function () {
  const taskInput = document.getElementById("new-task");
  const addTaskButton = document.getElementById("add-task");
  const taskList = document.getElementById("task-list");
  let tasks = JSON.parse(localStorage.getItem("tasks")) || [];

  function renderTasks() {
    taskList.innerHTML = "";

    tasks.forEach((task, index) => {
      const listItem = document.createElement("li");
      listItem.textContent = task.text;

      if (task.completed) {
        listItem.classList.add("completed");
      }

      const completeButton = document.createElement("button");
      completeButton.textContent = task.completed ? "Oznacz jako niewykonane" : "Oznacz jako wykonane";
      completeButton.addEventListener("click", function () {
        tasks[index].completed = !tasks[index].completed;
        updateLocalStorage();
        renderTasks();
      });

      const deleteButton = document.createElement("button");
      deleteButton.textContent = "Usuń";
      deleteButton.addEventListener("click", function () {
        tasks.splice(index, 1);
        updateLocalStorage();
        renderTasks();
      });

      listItem.appendChild(completeButton);
      listItem.appendChild(deleteButton);
      taskList.appendChild(listItem);
    });
  }

  function updateLocalStorage() {
    localStorage.setItem("tasks", JSON.stringify(tasks));
  }

  addTaskButton.addEventListener("click", function () {
    const taskText = taskInput.value.trim();
    if (taskText !== "") {
      tasks.push({ text: taskText, completed: false });
      taskInput.value = "";
      updateLocalStorage();
      renderTasks();
    }
  });

  renderTasks(); // Initial render
});
