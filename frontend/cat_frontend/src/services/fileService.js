import axios from 'axios'

export const uploadFile = (file, onUploadProgress) => {
  const formData = new FormData()
  formData.append('file', file)

  return axios.post('http://', formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
    },
    onUploadProgress
  })
}
