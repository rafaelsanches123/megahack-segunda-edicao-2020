import Vue from "nativescript-vue";
import App from "./components/App";
import Login from "./components/Login";
import DrawerContent from "./components/DrawerContent";
import RadSideDrawer from "nativescript-ui-sidedrawer/vue";
Vue.use(RadSideDrawer);
Vue.registerElement(
  "StarRating",
  () => require("nativescript-star-ratings").StarRating
);

import Ranking from "./components/Ranking";

Vue.config.silent = (TNS_ENV === 'production');

new Vue({
    render (h) {
        return h(
          App,
          [
            h(DrawerContent, { slot: 'drawerContent' }),
            h(Ranking, { slot: 'mainContent' })
            //h(Login, { slot: 'mainContent' })
          ]
        )
      }
  }).$start();
