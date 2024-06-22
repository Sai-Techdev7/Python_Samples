import React, { useState, useEffect } from 'react';
import { getTasks, createTask, updateTask, deleteTask } from './api';

function App() {
    const [tasks, setTasks] = useState([]);
    const [newTask, setNewTask] = useState({ title: '', description: '' });

    useEffect(() => {
        fetchTasks();
    }, []);

    const fetchTasks = async () => {
        const fetchedTasks = await getTasks();
        setTasks(fetchedTasks);
    };

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setNewTask({ ...newTask, [name]: value });
    };

    const handleCreateTask = async () => {
        await createTask(newTask);
        fetchTasks();
        setNewTask({ title: '', description: '' });
    };

    const handleUpdateTask = async (taskId) => {
        await updateTask(taskId, { ...newTask });
        fetchTasks();
    };

    const handleDeleteTask = async (taskId) => {
        await deleteTask(taskId);
        fetchTasks();
    };

    return (
        <div className="App">
            <h1>TaskMaster</h1>
            <div>
                <input
                    type="text"
                    name="title"
                    value={newTask.title}
                    onChange={handleInputChange}
                    placeholder="Task Title"
                />
                <input
                    type="text"
                    name="description"
                    value={newTask.description}
                    onChange={handleInputChange}
                    placeholder="Task Description"
                />
                <button onClick={handleCreateTask}>Create Task</button>
            </div>
            <ul>
                {tasks.map((task) => (
                    <li key={task._id}>
                        <h2>{task.title}</h2>
                        <p>{task.description}</p>
                        <button onClick={() => handleUpdateTask(task._id)}>Update</button>
                        <button onClick={() => handleDeleteTask(task._id)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default App;
