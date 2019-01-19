<template>
  <v-app dark>
    <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">

        <span>CLUSTERING</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <!-- <v-btn
        flat
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
      >
        <span class="mr-2">Latest Release</span>
      </v-btn> -->
      <router-link class="navlink" to="/">Home</router-link>
      <router-link class="navlink" to="/hierarchical">Hierarchical</router-link>
      <router-link class="navlink" to="/about">About</router-link>
      <!-- <router-link to="/iterations/">Iterations</router-link> -->

    </v-toolbar>

    <v-content>
        <router-view/>
      <!-- <HelloWorld/> -->
    </v-content>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  data () {
    return {
      //
    }
  }
}
</script>

<style>
.navlink {
    padding: 10px;
}

</style>
