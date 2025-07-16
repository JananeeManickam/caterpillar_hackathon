import { useState } from 'react';
import '../styles/UploadForm.css';
import { FaTimes } from 'react-icons/fa';

export default function UploadForm() {
  const [files, setFiles] = useState([]);
  const [progress, setProgress] = useState(0);

  const handleChange = (e) => {
    const selectedFiles = Array.from(e.target.files);
    setFiles(prev => [...prev, ...selectedFiles]);
    setProgress(0);
  };

  const handleRemove = (indexToRemove) => {
    const updatedFiles = files.filter((_, idx) => idx !== indexToRemove);
    setFiles(updatedFiles);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (files.length === 0) return alert('Please select at least one file');

    setProgress(0);
    const interval = setInterval(() => {
      setProgress(prev => {
        if (prev >= 100) {
          clearInterval(interval);
          alert('Files ready to be uploaded to backend!');
          return 100;
        }
        return prev + 10;
      });
    }, 100);
  };

  return (
    <>
      <form className="upload-form" onSubmit={handleSubmit}>
        <label className="upload-button">
          <input type="file" multiple hidden onChange={handleChange} />
          Choose Files
        </label>
        <button type="submit" className="upload-button" disabled={files.length === 0}>
          Upload All
        </button>
      </form>

      <div className="file-preview-list">
        {files.map((file, index) => (
          <div className="file-preview-card" key={index}>
            <FaTimes className="remove-icon" onClick={() => handleRemove(index)} />
            <p>{file.name}</p>
          </div>
        ))}
      </div>

      {progress > 0 && (
        <div className="progress-container">
          <div className="progress-bar" style={{ width: `${progress}%` }}>
            {progress}%
          </div>
        </div>
      )}
    </>
  );
}
