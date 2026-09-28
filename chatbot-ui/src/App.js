import {useState} from 'react';
import './App.css';

function App() {
  const[open,setOpen]=useState(false);
  return (
    <div>
      <button className="chat-button" onClick={() => setOpen(!open)}>💬</button>
      {open && (
      <div className="chat-window">
        <div className="chat-header">
          <h3>AI Assistance</h3>
          <button className="close-button" onClick={() => setOpen(false)}>X</button>
        </div>
      </div>
    )}
    </div>
  );
}

export default App;