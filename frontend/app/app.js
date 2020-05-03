import Vue from "nativescript-vue";
import App from "./components/App";
import DrawerContent from "./components/DrawerContent";
import RadSideDrawer from "nativescript-ui-sidedrawer/vue";
import Vuex from "vuex";
import store from "./store";

Vue.use(Vuex);
Vue.use(RadSideDrawer);
Vue.registerElement(
  "StarRating",
  () => require("nativescript-star-ratings").StarRating
);

Vue.registerElement(
  "BarcodeScanner",
  () => require("nativescript-barcodescanner").BarcodeScannerView
);

import InitialPage from "./components/Login";

Vue.config.silent = (TNS_ENV === 'production');

Vue.config.suppressRenderLogs = true;

new Vue({
  store,
  render(h) {
    return h(App, [h(DrawerContent, { slot: "drawerContent" }),h(InitialPage, { slot: "mainContent" }),
    ]);
  },
}).$start();
