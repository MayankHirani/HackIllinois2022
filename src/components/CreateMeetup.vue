<template>
  <v-container fluid>
    <v-row class="pl-3 pr-3 pt-3 pb-3">
      <v-btn icon @click="back">
        <v-icon>mdi-arrow-left</v-icon>
      </v-btn>
    </v-row>

  </v-container>
</template>

<script>
  export default {
    name: 'SettingsPage',
    data: () => ({
    }),
    methods: {
        back() {
          this.$emit('setUser', this.user)
        }
    },
    watch: {
    }
  }
</script>
