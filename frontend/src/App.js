import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Landing from "./Components/Landing/Landing";
import Add from "./Components/Add/Add";

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path="/" exact element={<Landing />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
