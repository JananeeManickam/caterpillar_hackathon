import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import {
  FaUpload,
  FaFolderOpen,
  FaCog,
  FaSignOutAlt,
  FaChevronLeft,
  FaChevronRight
} from 'react-icons/fa'
import '../styles/Sidebar.css'

export default function Sidebar() {
  const [collapsed, setCollapsed] = useState(false)
  const navigate = useNavigate()

  const handleLogout = () => {
    // Clear session info if stored (e.g., localStorage)
    localStorage.clear()
    // Navigate to logout page (or login page)
    navigate('/logout') // or navigate('/')
  }

  return (
    <div className={`sidebar ${collapsed ? 'collapsed' : ''}`}>
      <div className="sidebar-toggle" onClick={() => setCollapsed(!collapsed)}>
        {collapsed ? <FaChevronRight /> : <FaChevronLeft />}
      </div>

      <ul>
        <li><FaUpload /> {!collapsed && 'Upload Docs'}</li>
        <li><FaFolderOpen /> {!collapsed && 'My Files'}</li>
        <li><FaCog /> {!collapsed && 'Settings'}</li>
        <li onClick={handleLogout}><FaSignOutAlt /> {!collapsed && 'Logout'}</li>
      </ul>
    </div>
  )
}
