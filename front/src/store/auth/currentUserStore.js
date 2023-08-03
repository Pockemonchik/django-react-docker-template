import { makeAutoObservable } from 'mobx'
import {authAPI} from "../../api"


export const currentUserStore = makeAutoObservable({
    currentUser: {
        // "token": "b54cd0e290013cbdc4f0223f18c0e86018d87fcf",
        // "token": "cdf9c14ecefb3340315bf56b7ba1f4a6074f7b57",
        // "UserID": "267",   
        // "UserLogin": "79",
        // "GrpName": "2"
    },
    isAuth: false,
    initialized: false,
    loading: false,
    
    logout() {
        console.log("this.logout")
        this.isAuth = false
    },
    async login(value) {
        console.log("start auth")
        this.setLoading()
        try {
            const data = await authAPI.auth(value)
            console.log("data auth api",data)
            this.currentUser = data.data
            console.log("this.currentUser",this.currentUser)
            this.isAuth = true
            this.setLoading()
        } catch (e) {
            this.setLoading()
        }

    },

    setLoading() {
        this.loading = !this.loading
    },

})