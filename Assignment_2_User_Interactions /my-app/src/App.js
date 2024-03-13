import logo from './logo.svg';
import './App.css';
import MyProjects from './MyProjects';



function App() {
  return (
    <div className="App">
      <header className="App-header">
        <section>
            <h2>About Me</h2>
            <p>Diligent iOS developer with proven experience in building and deploying apps. Proficient in Swift, SwiftUI, and utilizing GitHub for collaboration.</p>
            {/* <p>As a diligent and meticulous professional, I possess a strong aptitude for creating user-centric applications. Proficient in Swift and SwiftUI, I have hands-on experience in leveraging GitHub, Firebase, and CoreData to deliver high-quality mobile applications. I am capable of translating complex ideas into user-friendly, intuitive interfaces while ensuring optimal performance, responsiveness, and scalability. I am passionate about staying updated with industry trends and best practices to produce exceptional user experiences. With exceptional communication and collaboration skills, I excel in working effectively in cross-functional teams.</p> */}
            
            <p>Languages: Swift | C++ | HTML | Java | CSS</p>
            <h3>Core Competencies</h3>
            <p>iOS Development</p>
            <p>Unit Testing</p>
            <p>Networking</p>
        </section>
        <MyProjects />
        <nav style={{textAlign: "left"}}>
          <a style={{marginLeft: "0%", color: "#dddd"}} href="https://github.com/RomaricAR/Platform_Computing">Link to my GitHub</a>
        </nav>
      </header>
    </div>
  );
}

export default App;
