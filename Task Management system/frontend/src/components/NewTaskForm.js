import React, { useState } from 'react';

const NewTaskForm = ({ onCreateTask }) => {
    const [task, setTask] = useState({ title: '', description: '' });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setTask({ ...task, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        onCreateTask(task);
        setTask({ title: '', description: '' });
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                name="title"
                value={task.title}
                onChange={handleChange}
                placeholder="Task Title"
                required
            />
            <input
                type="text"
                name="description"
                value={task.description}
                onChange={handleChange}
                placeholder="Task Description"
            />
            <button type="submit">Create Task</button>
        </form>
    );
};

export default NewTaskForm;
