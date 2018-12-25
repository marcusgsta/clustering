<template>
    <v-container grid-list-md>



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
    <p>K-means clustering starts with randomly placing a specified number of clusters (here: 10). The clustering algorithm puts each blog in the closest cluster. During the next iteration an average is calculated for each cluster, and the blogs are again put in the closest cluster, until the new collection of clusters is the same as the last collection of clusters.</p>
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
