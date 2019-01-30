<template>
    <v-container grid-list-md fluid>
        <h2>Hierarchical algorithm</h2>
        <!--  Loading animation -->
        <div class="loader" v-if="show">
        <v-progress-circular v-if="show"
            indeterminate
            :size="50"
            :width="7"
            color="blue"></v-progress-circular>
        </div>
        <!--  End of loading animation -->

        <tree v-if="hide" :tree-data="cluster"></tree>
        <Footer></Footer>
    </v-container>
</template>

<script>
import axios from 'axios'
import Tree from './Tree.vue'
import Footer from './Footer.vue'

export default {
  data: () => ({
      data: 0,
      blognames: [],
      cluster: {},
      show: true,
      hide: false
  }),
  components: {
    Tree,
    Footer
},
  methods: {
    getDataFromBackend () {
        let path = ""
        path = process.env.VUE_APP_ROOT_API + "/hierarchical"
        axios.get(path)
        .then(response => {
            this.cluster = response.data.data
            this.$store.commit('setBlognames', response.data.blognames)
            this.show = false
            this.hide = true
        })
        .catch(error => {
            console.log(error)
        })
    }
    },
  created () {
    this.getDataFromBackend()
    }
}

</script>

<style>
.loader {
    padding: 100px;
    width: 50px;
    margin: 0 auto;
}
</style>
