import axios from 'axios'

export const uploadFile = (file, onUploadProgress) => {
  const formData = new FormData()
  formData.append('file', file)

  return axios.post('/your-upload-endpoint', formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
    },
    onUploadProgress
  })
}
