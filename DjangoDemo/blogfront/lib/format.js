var axios = require('axios')
axios.defaults.baseURL = 'http://localhost:8000'
// 刷新token 注意这里用到的service
export const getRefreshToken = (param) => {
  let params = {
    token: param
  }
  return axios.post('/api-token-refresh/', params)
    .then((res) => {
      return Promise.resolve(res.data)
    })
}

export function isRefreshTokenExpired (timestamp) {
  clearInterval(window.interval)
  window.interval = setInterval(() => {
    timestamp = timestamp - 1
    sessionStorage.setItem('resetTime', timestamp)
  }, 1000)
}
