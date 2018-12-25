<template>
  <v-footer
    dark
    height="auto"
  >
    <v-card
      class="flex"
      flat
      tile
    >
      <v-card-title class="teal">
        <strong class="subheading">Get connected with us on social networks!</strong>

        <v-spacer></v-spacer>

        <!-- <font-awesome-icon :icon="{ prefix: 'fab', iconName: 'facebook' }" /> -->
        <v-btn
          v-for="icon in icons"
          :key="icon"
          class="mx-1 social_icon"
          icon>
          <a :href="icon[0]">
          <font-awesome-icon :icon="{ prefix: prefix, iconName: icon[1] }" />
        </a>

        </v-btn>
      </v-card-title>

      <v-card-actions class="grey darken-3 justify-center">
        &copy;2018 — <strong>Marcus Gustafsson</strong>
      </v-card-actions>
    </v-card>
  </v-footer>
</template>

<script>
  export default {
    data: () => ({
      prefix: 'fab',
      icons: [
        ['https://facebook.com/marcussn', 'facebook'],
        ['https://twitter.com/marcusgu1','twitter'],
        ['https://www.linkedin.com/in/marcus-gustafsson-80b595a3/', 'linkedin'],
        ['https://instagram.com/marcusgsta', 'instagram']
      ]
    })
  }
</script>
<style>
    .social_icon a{
        color: #fff;
    }
</style>
