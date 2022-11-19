import landing from './landing.png';
import './App.css';
import Topbar from './Components/Topbar';

function App() {
  return (
    <div className="App" background={landing} style={{
        backgroundImage: `url(${landing})`,
        backgroundSize: 'cover',
        overflow: 'hidden'
      }}>
      <header className="App-header">
        <Topbar></Topbar>
        <h1>Do health right</h1>
        <h3>Search your ingredients and such and get your health info.</h3>
        <a className="btn" href="">Get started</a>
      </header>
    </div>
  );
}

export default App;
