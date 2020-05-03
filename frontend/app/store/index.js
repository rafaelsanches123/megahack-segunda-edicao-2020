import Vue from "nativescript-vue";
import Vuex from "vuex";
import * as ApplicationSettings from "application-settings";

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    cliente:{
        nome:    "",
        apelido: "",
        email:   "",
        senha:   "",
        renda:   "",
        gasto:   "",
        celular: ""
    }
  },
  mutations: {
    load(state) {
      if (ApplicationSettings.getString("store")) {
        this.replaceState(
          Object.assign(
            state,
            JSON.parse(ApplicationSettings.getString("store"))
          )
        );
      }
    },
    save(state, data) {
      state.cliente.nome    = data.nome;
      state.cliente.apelido = data.apelido;
      state.cliente.email   = data.email;
      state.cliente.senha   = data.senha;
      state.cliente.renda   = data.renda;
      state.cliente.gasto   = data.gasto;
      state.cliente.celular = data.celular;
    },
  },
});

Vue.prototype.$store = store;

module.exports = store;
