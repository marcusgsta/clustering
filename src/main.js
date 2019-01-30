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

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faCoffee } from '@fortawesome/free-solid-svg-icons'
import { faFolder } from '@fortawesome/free-solid-svg-icons'

library.add(faFacebook,faTwitter,faGooglePlus,faLinkedin,faInstagram
    )
library.add(faFolder)
library.add(faCoffee)

Vue.component('font-awesome-icon', FontAwesomeIcon)

import 'roboto-fontface/css/roboto/roboto-fontface.css'

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
