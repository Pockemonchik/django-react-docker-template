import axios from "axios"
import { currentUserStore } from "../store/auth/currentUserStore"

// const baseUrl = "http://localhost:8000/api/"
//const baseUrl = "http://192.168.0.241:8000/api/"
// const baseUrl = 'http://192.168.0.153:2000/api/'
const baseUrl = process.env.REACT_APP_API_URL
console.log("baseUrl",baseUrl)
const client = axios.create({
    baseURL: baseUrl,
});

const onSuccess = (response) => {
    console.debug('Request Successful!', response);
    return response
}

const onError = (error) => {
    console.error('Request Failed:', error.config);

    if (error.response) {
        console.error('Status:', error.response.status);
        console.error('Data:', error.response.data);
        console.error('Headers:', error.response.headers);

    } else {
        console.error('Error Message:', error.message);
    }
    throw new Error(error.response || error.message || 'Что то пошло не так')
    // return Promise.reject(error.response || error.message);
}

const request = {
    async get(url, params) {
        return client({ method: "get", url: url, params: params, headers: {
            'Authorization': 'Token ' + currentUserStore.currentUser.token || " "
        }, })
            .then(onSuccess)
            .catch(onError);
    },
    async getFile(url, params) {
        return client({
            method: "get", url: url, params: params, responseType: 'blob', headers: {
                'Authorization': 'Token ' + currentUserStore.currentUser.token || " "
            },
        })
            .then(onSuccess)
            .catch(onError);
    },
    async post(url, params) {
        return client({
            method: "post", url: url, data: params, headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Token ' + currentUserStore.currentUser.token || " "
            },
        })
            .then(onSuccess)
            .catch(onError);
    },
    async put(url, params) {
        return client({
            method: "put", url: url, data: params, headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Token ' + currentUserStore.currentUser.token || " "
            },
        })
            .then(onSuccess)
            .catch(onError);
    },
    async patch(url, params) {
        return client({
            method: "patch", url: url, data: params, headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Token ' + currentUserStore.currentUser.token || " "
            },
        })
            .then(onSuccess)
            .catch(onError);
    },
    async delete(url, params) {
        return client({
            method: "delete", url: url, data: params, headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Token ' + currentUserStore.currentUser.token || " "
            },
        })
            .then(onSuccess)
            .catch(onError);
    }

}
export default request
