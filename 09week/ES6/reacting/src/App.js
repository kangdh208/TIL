import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  let posts = 'Gangnam';
  return (
    <div className="App">
      <div className="balck-nav">
        <div>개발 blog</div>
      </div>
      <div className="list">
        <h3> { posts }</h3>
        <p>Feb.17th.posts</p>
        <hr/>
      </div>
    </div>
  );
}

export default App;
