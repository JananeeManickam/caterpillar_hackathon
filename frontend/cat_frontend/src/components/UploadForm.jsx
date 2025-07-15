import { useState } from 'react'
import { uploadFile } from '../services/fileService'
import '../styles/UploadForm.css'

export default function UploadForm() {
  const [file, setFile] = useState(null)
  const [progress, setProgress] = useState(0)

  const handleChange = (e) => {
    setFile(e.target.files[0])
    setProgress(0) // reset progress on new file
  }

  const handleSubmit = async (e) => {
  e.preventDefault();
  try {
    if (isLogin) {
        const res = await loginUser({
            email: form.email,
            password: form.password,
        });
        console.log('Login success', res);
        navigate('/dashboard');
        } else {
        const res = await registerUser({
            username: form.username,
            email: form.email,
            password: form.password,
            role: 'user' // or any default
        });
        alert('Signup successful! Please login.');
        setIsLogin(true);
        }
    } catch (err) {
        alert('Error: ' + err.message);
    }
    }


  return (
    <>
      <form className="upload-form" onSubmit={handleSubmit}>
        <label className="upload-button">
          <input type="file" onChange={handleChange} />
          Choose File
        </label>
        <button type="submit" className="upload-button">Upload</button>
      </form>

      {/* Progress Bar */}
      {progress > 0 && (
        <div className="progress-container">
          <div className="progress-bar" style={{ width: `${progress}%` }}>
            {progress}%
          </div>
        </div>
      )}
    </>
  )
}
