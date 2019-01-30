<template>
    <v-container grid-list-md fluid>

    <v-layout row wrap>
        <v-flex md6>
            <v-card color="secondary">
                <v-card-title primary-title>

                <div class="">
    <h2>About</h2>

    <p>This application was made as an assigment in clustering in the course Web Intelligence, Linneaus University, Sweden</p>
    <p>It was coded by Marcus Gustafsson</p>

    <p>A collection of 99 blogs is being sorted in clusters, according to frequency of 706 different words</p>
    <p>Blogs that contain the same words should appear in the same cluster, so that blogs are sorted according to their content</p>
    <h3>K-Means</h3>
    <p>K-means clustering starts with randomly placing a specified number of clusters (here: 10). The clustering algorithm puts each blog in the closest cluster. During the next iteration an average is calculated for each cluster, and the blogs are again put in the closest cluster, until the new collection of clusters is the same as the last collection of clusters.</p>
    <h3>Hierarchical</h3>
    <p>In hierarchical clustering the algorithm compares each blog to the others to always find the closest one. The two closest ones are combined, and in the next iteration the closest blogs or clusters are combined and so on. In the end there is only one cluster left which contains all the blogs in the format of a tree.</p>
                    </div>
                </v-card-title>
</v-card>
    </v-flex>
</v-layout>

    <Footer></Footer>

</v-container>
</template>

<script type="text/javascript">

import Footer from './Footer.vue'

    export default {
        components: {
          Footer
        },
    }

</script>
