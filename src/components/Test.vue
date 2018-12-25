<template>
  <div>
    <p>Home page</p>
    <p>Data from backend: {{ data }}</p>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      data: "0"
    }
  },
  methods: {
    getDataFromBackend () {
        const path = `http://localhost:5000/test`
        axios.get(path)
        .then(response => {
            this.data = response.data.data
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
