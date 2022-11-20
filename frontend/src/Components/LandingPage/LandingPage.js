import "./LandingPage.css";
import landing from "../../landing.png";
import Topbar from "../Topbar/Topbar";
import { Link } from "react-router-dom";
import React from "react";

const Landing = () => {
  return (
    <>
      <div
        className="App"
        background={landing}
        style={{
          backgroundImage: `url(${landing})`,
          backgroundSize: "cover",
          overflow: "hidden",
        }}
      >
        <header className="App-header">
          <Topbar></Topbar>
          <h1 className="landing-title">Do health right</h1>
          {/* <h3 className="landing-sub-title">Search your ingredients and get to know your health better.</h3> */}
          <h3 className="landing-sub-title">Start learning about your health, one ingredient at a time.</h3>
          <Link className="btn" to="/add">
            Get started
          </Link>
        </header>
      </div>
    </>
  );
};

export default Landing;
