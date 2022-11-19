import "./Landing.css";
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
          <h1>Do health right</h1>
          <h3>Search your ingredients and such and get your health info.</h3>
          <Link className="btn" to="/add">
            Get started
          </Link>
        </header>
      </div>
    </>
  );
};

export default Landing;
