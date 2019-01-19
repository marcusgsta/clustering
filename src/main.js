import Vue from 'vue';
import Vuex from 'vuex'
Vue.use(Vuex)
import './plugins/vuetify'
// import Vuetify from 'vuetify'
// Vue.use(Vuetify)
import App from './App';
import router from './router';
import 'vuetify/dist/vuetify.min.css' // Ensure you are using css-loader

import { library } from '@fortawesome/fontawesome-svg-core'
import { faFacebook,faTwitter,faGooglePlus,faLinkedin,faInstagram
     } from '@fortawesome/free-brands-svg-icons'
     // fa-twitter,
     // fa-google-plus,
     // fa-linkedin,
     // fa-instagram
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
library.add(faFacebook,faTwitter,faGooglePlus,faLinkedin,faInstagram
    )
    // fab fa-twitter,
    // fab fa-google-plus,
    // fab fa-linkedin,
    // fab fa-instagram
Vue.component('font-awesome-icon', FontAwesomeIcon)

import 'roboto-fontface/css/roboto/roboto-fontface.css'
// import 'material-design-icons-iconfont/dist/material-design-icons.css'

Vue.config.productionTip = false;

const store = new Vuex.Store({
  state: {
    blognames: []
  },
  mutations: {
    setBlognames (state, blognames) {
      state.blognames = blognames
    }
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  render: h => h(App),
});
