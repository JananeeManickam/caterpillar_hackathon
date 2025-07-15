import { useState } from 'react'
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

  return (
    <div className={`sidebar ${collapsed ? 'collapsed' : ''}`}>
      <div className="sidebar-toggle" onClick={() => setCollapsed(!collapsed)}>
        {collapsed ? <FaChevronRight /> : <FaChevronLeft />}
      </div>

      {/* {!collapsed && <h3 className="sidebar-title">Cathackathon</h3>} */}
      <ul>
        <li class="toggle-button" onclick="toggleSidebar()">
            {/* <i class="fas fa-chevron-left"></i>  */}
        </li>
        <li><FaUpload /> {!collapsed && 'Upload Docs'}</li>
        <li><FaFolderOpen /> {!collapsed && 'My Files'}</li>
        <li><FaCog /> {!collapsed && 'Settings'}</li>
        <li><FaSignOutAlt /> {!collapsed && 'Logout'}</li>
      </ul>
    </div>
  )
}
