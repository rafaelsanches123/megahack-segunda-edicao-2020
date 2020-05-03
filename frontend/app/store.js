import Vue from "nativescript-vue";
import Vuex from "vuex";
import * as ApplicationSettings from "application-settings";
import * as http from "http";
//import localStorage from "nativescript-localstorage";

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    usuario: {},
    meta: {}
  },
  mutations: {
    /*
    load(state) {
      if (ApplicationSettings.getString("store")) {
        this.replaceState(
          Object.assign(
            state,
            JSON.parse(ApplicationSettings.getString("store"))
          )
        );
      }
    },*/
    saveUsuario(state, data) {
      state.usuario = data;
    },
    saveMeta(state,data){
      state.meta = data
    }
  },
  actions: {
    getMeta({commit},payload){
      http
        .request({
          url: payload.url + payload.email,
          method: "GET",
          headers: { "Content-Type": "application/json" },
        })
        .then(
          (response) => {
            var result = response.content.toJSON();
            if (response.statusCode == 200) {
              commit("saveMeta",result.dados)
            }
          },
          (error) => {
            console.error(error);
            this.alert(
              "Erro com a conexão ao servidor. Tente novamente mais tarde!"
            );
          }
        );
    }
  }
});

//Vue.prototype.$store = store;

//module.exports = store;
export default store;