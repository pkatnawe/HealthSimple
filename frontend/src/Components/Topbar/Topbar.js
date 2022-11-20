import './Topbar.css';

const Topbar = () => {
    return (
      <>
        <div className="topbar">
          <h2 className="logo">Healthsimple</h2>
          <a className="top-btn" href="/add">Get started</a>
        </div>
      </>
    );
}

export default Topbar;