import Vue from "nativescript-vue";
import App from "./components/App";
import DrawerContent from "./components/DrawerContent";
import RadSideDrawer from "nativescript-ui-sidedrawer/vue";
Vue.use(RadSideDrawer);
Vue.registerElement(
  "StarRating",
  () => require("nativescript-star-ratings").StarRating
);

Vue.registerElement(
  "BarcodeScanner",
  () => require("nativescript-barcodescanner").BarcodeScannerView
);

import InitialPage from "./components/Checking";

Vue.config.silent = (TNS_ENV === 'production');

new Vue({
    render (h) {
        return h(App, [
          h(DrawerContent, { slot: "drawerContent" }),
          h(InitialPage, { slot: "mainContent" }),
        ]);
      }
  }).$start();
