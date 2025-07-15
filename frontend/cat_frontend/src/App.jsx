import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Dashboard from './pages/Dashboard';
import AuthForm from './pages/Login';


function App() {
  return (
    <div>
      <AuthForm />
      {/* <Dashboard /> */}
    </div>
  );
}

export default App;
