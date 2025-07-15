import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Dashboard from './pages/Dashboard'
import AuthForm from './pages/Login'
import Logout from './pages/Logout'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<AuthForm />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/logout" element={<Logout />} />
      </Routes>
    </Router>
  )
}

export default App
