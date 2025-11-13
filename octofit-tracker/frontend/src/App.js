import React from 'react';
import './App.css';
import { Routes, Route, NavLink } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';
import { getApiEndpoint } from './apiConfig';

function App() {
  return (
    <div className="container mt-4">
      <header className="mb-4 app-header">
        <div className="app-brand">
          <img src="/octofitapp-small.svg" alt="OctoFit" className="app-logo" />
          <div>
            <h1 className="h3">OctoFit Tracker</h1>
            <div className="text-muted">Track activities, teams, workouts and leaderboards</div>
          </div>
        </div>

        <nav className="" role="navigation" aria-label="Main navigation">
          <ul className="nav nav-pills">
            <li className="nav-item">
              <NavLink className={({isActive}) => 'nav-link' + (isActive ? ' active' : '')} to="/activities">Activities</NavLink>
            </li>
            <li className="nav-item">
              <NavLink className={({isActive}) => 'nav-link' + (isActive ? ' active' : '')} to="/workouts">Workouts</NavLink>
            </li>
            <li className="nav-item">
              <NavLink className={({isActive}) => 'nav-link' + (isActive ? ' active' : '')} to="/teams">Teams</NavLink>
            </li>
            <li className="nav-item">
              <NavLink className={({isActive}) => 'nav-link' + (isActive ? ' active' : '')} to="/users">Users</NavLink>
            </li>
            <li className="nav-item">
              <NavLink className={({isActive}) => 'nav-link' + (isActive ? ' active' : '')} to="/leaderboard">Leaderboard</NavLink>
            </li>
          </ul>
        </nav>
      </header>

      <main>
        <Routes>
          <Route path="/" element={<Activities />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;

// show a sample endpoint in the browser console to help debugging routing/API
console.log('Sample API endpoint (activities):', getApiEndpoint('activities'));
