<template>
  <div class="tree">
    <ul class="tree-list">
        <span v-if="treeData">
      <Node-Tree :node="treeData"></Node-Tree>
        </span>

    </ul>
  </div>
</template>

<script>
import NodeTree from "./NodeTree";

export default {
  props: {
    treeData: Object
  },
  components: {
    NodeTree
},
// beforeCreate: function () {
//  this.$options.components.NodeTree = require('./NodeTree.vue').default
// }

};
</script>
