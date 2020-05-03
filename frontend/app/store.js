import Vue from "nativescript-vue";
import Vuex from "vuex";
import * as ApplicationSettings from "application-settings";
import * as http from "http";
//import localStorage from "nativescript-localstorage";

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    usuario: {},
    meta: {},
    gastos_mensal: [],
    ranking: []
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
      console.log(data);
      state.usuario = data;
    },
    saveMeta(state, data) {
      console.log(data);
      state.meta = data;
    },
    saveGastosMensal(state, data) {
      console.log(data);
      state.gastos_mensal = data;
    },
    saveRanking(state, data) {
      console.log(data);
      state.ranking = data;
    },
  },
  actions: {
    getMeta({ commit }, payload) {
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
              commit("saveMeta", result.dados);
            }
          },
          (error) => {
            console.error(error);
            this.alert(
              "Erro com a conexão ao servidor. Tente novamente mais tarde!"
            );
          }
        );
    },
    getGastosMensal({ commit }, payload) {
      http
        .request({
          url: payload.url,
          method: "GET",
          headers: { "Content-Type": "application/json" },
        })
        .then(
          (response) => {
            var result = response.content.toJSON();
            if (response.statusCode == 200) {
              commit("saveGastosMensal", result.dados);
            }
          },
          (error) => {
            console.error(error);
            this.alert(
              "Erro com a conexão ao servidor. Tente novamente mais tarde!"
            );
          }
        );
    },
    getRanking({ commit }, payload) {
      http
        .request({
          url: payload.url,
          method: "GET",
          headers: { "Content-Type": "application/json" },
        })
        .then(
          (response) => {
            var result = response.content.toJSON();
            if (response.statusCode == 200) {
              commit("saveRanking", result.dados);
            }
          },
          (error) => {
            console.error(error);
            this.alert(
              "Erro com a conexão ao servidor. Tente novamente mais tarde!"
            );
          }
        );
    },
  },
});

//Vue.prototype.$store = store;

//module.exports = store;
export default store;