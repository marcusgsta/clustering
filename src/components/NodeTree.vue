<template>

  <li class="node-tree">

      <span class="distance" v-if="node.id < 0">
          Group<br/>
          {{ node.distance }}
      </span>

      <span v-else class="label">
          {{ node.id }}
          {{ bnames[node.id] }}
      </span>


      <ul>

          <span v-if="node.left != null">
            <!-- send cluster['left'] to new Node template -->
            <node :node="node.left"></node>
      <!-- </ul> -->
        </span>

      <span v-if="node.right != null">

          <node :node="node.right"></node>
      </span>

      </ul>
            <!-- send cluster['right'] to new Node template -->

  </li>
</template>



<script>

export default {
    name: "node",
    props: {
     node: Object
    },
     computed: {
        bnames () {
            return this.$store.state.blognames
     }
 }
}

</script>
<style media="screen">
    .label {
        /* font-size:1.2em; */
    }
    ul,li {
        list-style-type: none;
    }
</style>
