<template>
  <v-app dark>
    <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">

        <span>CLUSTERING</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>

      <router-link class="navlink" to="/">K-Means</router-link>
      <router-link class="navlink" to="/hierarchical">Hierarchical</router-link>
      <router-link class="navlink" to="/about">About</router-link>

    </v-toolbar>

    <v-content>
        <router-view/>

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
