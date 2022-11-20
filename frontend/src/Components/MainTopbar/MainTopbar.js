import './MainTopbar.css';
import { Link } from 'react-router-dom';

const MainTopbar = () => {
    return (
      <>
        <div className="topbar">
          <Link to="/">
            <h2 className="logo">Healthsimple</h2> 
          </Link>
        </div>
      </>
    );
}

export default MainTopbar;