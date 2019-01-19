<template>
    <v-container grid-list-md fluid>

        <div class="" v-if="iters">
            Iterations: {{ iters }}
        </div>


            <v-layout align-space-around justify-start row wrap class="" v-if="kclust.length">
                <v-flex v-for="(cluster, index) in kclust" class="cluster" md4 grow>

                    <v-progress-circular v-if="show"
                        indeterminate
                        :size="50"
                        :width="7"
                        color="blue"></v-progress-circular>

                        <v-card>


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
      query: false
    }
  },
  components: {
    Footer
  },
  methods: {
    getDataFromBackend () {
        const params = this.$route.params
        let isMyObjectEmpty = !Object.keys(params).length;
        let path = ""
        console.log(isMyObjectEmpty)
        console.log(params)
        if (!isMyObjectEmpty) {
            let iters = params.iters
            // path = `http://marcusgsta-ai.info:5000/iterations/` +
            // iters
            path = process.env.VUE_APP_ROOT_API
            // path = `http://localhost:5000/iterations/` + iters
            // console.log("process.env.BACKEND_HOST")
            // console.log(process.env.BACKEND_HOST)
            // path = process.env.BACKEND_HOST + `/iterations/` + iters
         }
        else {
            // path = `http://marcusgsta-ai.info:5000`
            path = process.env.VUE_APP_ROOT_API;
            // path = process.env.VUE_APP_BACKEND_HOST + `:5000`
            // path = `http://localhost:5000`;
        }
        axios.get(path)
        .then(response => {
            this.blognames = response.data.blognames
            this.kclust = response.data.kclust
            // try {
            this.iters = response.data.iters
            // } catch {
            //
            // }
            this.show = false
        })
        .catch(error => {
            console.log(error)
        })
    }
  },
  created () {
    this.loading2 = true
    this.getDataFromBackend()
  }
}
</script>
