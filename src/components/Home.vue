<template>
    <v-container grid-list-md fluid>
        <h2>K-means algorithm</h2>
        <!--  Loading animation -->
        <div class="loader" v-if="show">
        <v-progress-circular v-if="show"
            indeterminate
            :size="50"
            :width="7"
            color="blue"></v-progress-circular>
        </div>
        <!--  End of loading animation -->

        <div class="" v-if="iters">
            Iterations: {{ iters }}
        </div>
            <v-layout align-space-around justify-start row wrap class="" v-if="kclust.length">

                <v-flex v-for="(cluster, index) in kclust" class="cluster" md4 grow>

                    <v-card v-if="hide">
                        <v-card-title primary-title>
                            <div class="">
                            <h3>Cluster {{ index+1 }} ({{ cluster.length }}) </h3>
                            <div class="px-0 blogname"
                                v-for="blog in cluster">
                                {{ blog }}
                            </div>
                            </div>
                        </v-card-title>
                    </v-card>
                </v-flex>
            </v-layout>
            <p v-else class="warning">Couldn't retrieve data!</p>

            <Footer></Footer>
        </v-container>

</template>

<script>
import axios from 'axios'
import Footer from './Footer.vue'

export default {
  data () {
    return {
      blognames: "0",
      kclust: "0",
      iters: "",
      value: 0,
      show: true,
      hide: false,
      query: false
    }
  },
  components: {
    Footer
  },
  methods: {
    getDataFromBackend () {

        let path = process.env.VUE_APP_ROOT_API;

        axios.get(path)
            .then(response => {
                this.blognames = response.data.blognames
                this.kclust = response.data.kclust
                this.iters = response.data.iters
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

<style media="screen">
    .loader {
        padding: 100px;
        width: 50px;
        margin: 0 auto;
    }
</style>
