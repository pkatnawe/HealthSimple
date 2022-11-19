import './App.css';
import {
  BrowserRouter as Router,
  Route,
  Routes,
} from "react-router-dom";
import Landing from './Components/Landing/Landing';
import Add from './Components/Add/Add';

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/">
          <Landing></Landing>      
        </Route>
        <Route path="/add">
          <Add></Add>
        </Route>
      </Routes>
  </Router>
  );
}

export default App;
