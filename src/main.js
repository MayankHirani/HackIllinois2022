import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import GSignInButton from 'vue-google-signin-button'
import VueGeolocation from 'vue-browser-geolocation'

Vue.config.productionTip = false

Vue.use(GSignInButton)
Vue.use(VueGeolocation)

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
