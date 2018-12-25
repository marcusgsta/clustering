import Vue from 'vue';
import './plugins/vuetify'
// import Vuetify from 'vuetify'
// Vue.use(Vuetify)
import App from './App';
import router from './router';
import 'vuetify/dist/vuetify.min.css' // Ensure you are using css-loader

import 'roboto-fontface/css/roboto/roboto-fontface.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App),
});
