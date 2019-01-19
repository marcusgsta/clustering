<template>

    <tree :tree-data="cluster"></tree>

</template>

<script>
import axios from 'axios'
import Tree from './Tree.vue'

export default {
  data: () => ({
      data: 0,
      blognames: [],
      cluster: {}
  }),
  components: {
    Tree
},
  methods: {
    getDataFromBackend () {
            let path = ""
            path = process.env.VUE_APP_ROOT_API + "/hierarchical"
            // const path = `http://localhost:5000/hierarchical`
            axios.get(path)
            .then(response => {
                this.cluster = response.data.data
                //this.blognames = response.data.blognames
                this.$store.commit('setBlognames', response.data.blognames)
            })
            .catch(error => {
                console.log(error)
            })
        }
    },
  created () {
    this.getDataFromBackend()
    },
   // mounted () {
   //  this.createTree(this.cluster)
   // }
}

</script>
<style>
body {

}
</style>
