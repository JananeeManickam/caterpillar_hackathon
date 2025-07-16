import React, { useEffect, useState } from 'react';
import '../styles/MyFiles.css';
import { FaEdit, FaDownload, FaFileAlt } from 'react-icons/fa';

export default function MyFiles() {
  const [files, setFiles] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/briefs/')
      .then(res => res.json())
      .then(data => setFiles(data))
      .catch(err => console.error('Error fetching files:', err));
  }, []);

  return (
    <div className="myfiles-page">
      <h2>Your Uploaded Files</h2>
      <div className="file-list">
        {files.map(file => (
          <div className="file-card" key={file.id}>
            <div className="file-icon"><FaFileAlt /></div>
            <div className="file-info">
              <a href={file.file} className="file-link" target="_blank" rel="noopener noreferrer">
                {file.file.split('/').pop()}
              </a>
              <p className="file-desc">{file.description}</p>
            </div>
            <div className="file-actions">
              <a href={file.file} download><FaDownload title="Download" /></a>
              <FaEdit title="Edit description (coming soon)" />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
