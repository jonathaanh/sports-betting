// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;

// App.js
import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

import Home from "./Home";
import Betting from "./Betting";
import Results from "./Results";
import Statistics from "./Statistics";
import Account from "./Account";

function App() {
  return (
    <Router>
      <header>
        <nav>
          <Link to="/">Home</Link>
          <Link to="/betting">Betting</Link>
          <Link to="/results">Results</Link>
          <Link to="/statistics">Statistics</Link>
          <Link to="/account">Account</Link>
        </nav>
      </header>

      <Routes>
        <Route path="/" exact component={Home} />
        <Route path="/betting" component={Betting} />
        <Route path="/results" component={Results} />
        <Route path="/statistics" component={Statistics} />
        <Route path="/account" component={Account} />
      </Routes>
    </Router>
  );
}

export default App;
