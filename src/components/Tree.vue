<template>
  <div class="tree">
    <ul class="tree-list">
      <Node-Tree :node="treeData"></Node-Tree>


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
    // NodeTree
    NodeTree: () => import('./NodeTree.vue')
  }
};
</script>
