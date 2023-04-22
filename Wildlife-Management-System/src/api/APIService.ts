import axios from "axios";

axios.defaults.baseURL = "http://127.0.0.1:5000"

class APIService {
  get(url: string, params?: Object) {
    return axios.get(url, { params: params });
  }

  post(url: string, data: Object, params?: Object) {
    return axios.post(url, data, { params: params });
  }

  put(url: string, data?: Object, params?: Object) {
    return axios.put(url, data, { params: params });
  }

  delete(url: string, params?: Object) {
    return axios.delete(url, { params: params });
  }
}

export default APIService;