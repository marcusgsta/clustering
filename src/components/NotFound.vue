<template>
    <v-container grid-list-md>
    <v-layout row wrap>
        <v-flex md6>
            <v-card color="secondary">
                <v-card-title primary-title>

                <div class="">
    <h2>Not Found</h2>

    <p>We couldn't find the file.</p>
    <p>Please try the navigation menu in the top right corner.</p>
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
