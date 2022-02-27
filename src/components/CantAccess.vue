<template>
  <v-container fill-height fluid>
    <v-row align="center" justify="center">
        <v-container fluid>
            <v-row align="center" justify="center">
                You are not allowed to access this app without an @illinois.edu email account.
            </v-row>
            <v-row class="pt-6" align="center" justify="center">
                <v-btn color="red" @click="logout">
                     Logout
                </v-btn>
            </v-row>
        </v-container>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'LoadingScreen',
    data: () => ({}),
    methods: {
        logout() {
            this.$emit('setUser', null)
        }
    }
  }
</script>
