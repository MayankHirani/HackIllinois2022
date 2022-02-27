<template>
  <v-container fluid>
    <v-row class="pl-3 pr-3 pt-3 pb-3">
      <v-btn icon @click="back">
        <v-icon>mdi-arrow-left</v-icon>
      </v-btn>
    </v-row>
    <v-row align="center" justify="center">
      <v-slider
        label="Maximum Distance"
        step="1"
        min="1"
        max="15"
        class="pt-12 pl-5 pr-5 pb-6"
        v-model="dist"
        thumb-label="always"
        ></v-slider>
    </v-row>
    <v-row align="center" justify="center">
      You are currently signed in as: {{ user.getBasicProfile().getEmail() }}
    </v-row>
    <v-row class="pt-6" align="center" justify="center">
      <v-btn color="red" @click="logout">
        Logout
      </v-btn>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'SettingsPage',
    data: () => ({
        dist: 15
    }),
    methods: {
        logout() {
          this.$emit('setUser', null)
        },
        back() {
          this.$emit('setUser', this.user)
        }
    },
    props: ['distance', 'user'],
    watch: {
        dist() {
            this.$emit('updateDistance', this.dist)
        }
    }
  }
</script>
