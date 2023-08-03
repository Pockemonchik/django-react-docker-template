import axios from "axios"
import request from "./request"

export const authAPI = {
    async auth(params) {
        console.log("auth start api/", params)
        let res = await request.post("/auth/", params)
        console.log("auth/", res)
        return res
    }
}

