<template>

  <li class="node-tree" v-if="node">

     <font-awesome-icon icon="folder"/>

     <!-- if node is leaf node, print its data -->
     <span v-if="node.left == null && node.right == null">

         {{ bnames[node.id] }}

     </span>

      <!-- if left child exists, check for leaf recursively -->
      <ul v-if="node.left != null">
          <node :node="node.left"></node>
      </ul>

      <!-- if right child exists, check for leaf recursively -->
      <ul v-if="node.right != null">
          <node :node="node.right"></node>
      </ul>

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
