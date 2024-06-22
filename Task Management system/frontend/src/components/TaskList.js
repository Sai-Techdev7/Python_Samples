import React from 'react';

const TaskList = ({ tasks, onUpdateTask, onDeleteTask }) => {
    return (
        <ul>
            {tasks.map((task) => (
                <li key={task._id}>
                    <h2>{task.title}</h2>
                    <p>{task.description}</p>
                    <button onClick={() => onUpdateTask(task._id)}>Update</button>
                    <button onClick={() => onDeleteTask(task._id)}>Delete</button>
                </li>
            ))}
        </ul>
    );
};

export default TaskList;
