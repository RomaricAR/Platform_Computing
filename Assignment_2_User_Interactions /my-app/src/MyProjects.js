import React from 'react';
// Import images if they're local to your project
// import HabitsImage from './Habits.png';
// import TodoListImage from './TodoList.png';
// import HealthVisionImage from './HealthVision.jpeg';

function MyProjects() {
  return (
    <section>
    <h2>My Projects</h2>
    <div class="project-titles">
    <h3 style={{textAlign: "left"}}>1. One Priority App</h3>
    <div class="row">
        <div className="column">
          <img src="Habits.png" alt="One Priority App" style={{width: '150px', height: 'auto'}} />
        </div>
        <div className="column1">
          <img src="TodoList.png" alt="HealthVision App"style={{width: '150px', height: 'auto'}} />
        </div>
    </div>
        <h3>2. Health In-Sight</h3>
    </div>
    <div class="row">
        <div className="column2">
            <img src="health1.png" alt="HealthVision App" style={{width: '150px', height: 'auto'}} />
         </div>
         <div className="column3">
            <img src="health2.png" alt="HealthVision App" style={{width: '150px', height: 'auto'}} />
         </div>
    </div>
</section>
  );
}

export default MyProjects;
