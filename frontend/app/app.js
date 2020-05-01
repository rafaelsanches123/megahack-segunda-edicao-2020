import Vue from "nativescript-vue";
import App from "./components/App";
import Login from "./components/Login";
import DrawerContent from "./components/DrawerContent";
import RadSideDrawer from "nativescript-ui-sidedrawer/vue";
Vue.use(RadSideDrawer);

import Home from "./components/Home";

Vue.config.silent = (TNS_ENV === 'production');

new Vue({
    render (h) {
        return h(
          App,
          [
            h(DrawerContent, { slot: 'drawerContent' }),
            h(Home, { slot: 'mainContent' })
            //h(Login, { slot: 'mainContent' })
          ]
        )
      }
  }).$start();
