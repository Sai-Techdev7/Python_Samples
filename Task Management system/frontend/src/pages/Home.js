import React, { useState, useEffect } from 'react';
import { getTasks, createTask, updateTask, deleteTask } from '../api';
import TaskList from '../components/TaskList';
import NewTaskForm from '../components/NewTaskForm';

const Home = () => {
    const [tasks, setTasks] = useState([]);

    useEffect(() => {
        fetchTasks();
    }, []);

    const fetchTasks = async () => {
        const fetchedTasks = await getTasks();
        setTasks(fetchedTasks);
    };

    const handleCreateTask = async (task) => {
        await createTask(task);
        fetchTasks();
    };

    const handleUpdateTask = async (taskId) => {
        const updatedTask = { title: 'Updated Task', description: 'Updated description' };
        await updateTask(taskId, updatedTask);
        fetchTasks();
    };

    const handleDeleteTask = async (taskId) => {
        await deleteTask(taskId);
        fetchTasks();
    };

    return (
        <div>
            <h1>TaskMaster</h1>
            <NewTaskForm onCreateTask={handleCreateTask} />
            <TaskList tasks={tasks} onUpdateTask={handleUpdateTask} onDeleteTask={handleDeleteTask} />
        </div>
    );
};

export default Home;
