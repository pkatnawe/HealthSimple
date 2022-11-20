import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LandingPage from "./Components/LandingPage/LandingPage";
import AddPage from "./Components/AddPage/AddPage";
import SummaryPage from "./Components/SummaryPage/SummaryPage";
import axios from "axios";
import { useEffect } from "react";
function App() {
  useEffect(() => {
    axios
      .get("http://localhost:5000/api/score/kale", { mode: "cors" })
      .then((res) => console.log(res.data))
      .catch((err) => console.log(err));
  }, []);
  return (
    <>
      <Router>
        <Routes>
          <Route path="/" exact element={<LandingPage />} />
          <Route path="/add" exact element={<AddPage />} />
          <Route path="/summary" exact element={<SummaryPage />}/>
        </Routes>
      </Router>
    </>
  );
}

export default App;
