<template>
  <v-container fill-height fluid>
    <v-row align="center" justify="center">
      <g-signin-button
      :params="googleSignInParams"
      @success="onSignInSuccess"
      @error="onSignInError"
      >
            <v-btn>Sign in with Google</v-btn>
        </g-signin-button>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'GoogleLogin',
    data: () => ({
      googleSignInParams: {
        client_id: '378762485257-kpdup215b67sgg54v37f2267o9d0ejig.apps.googleusercontent.com'
      }
    }),
    methods: {
        onSignInSuccess (googleUser) {
            this.$emit('setUser', googleUser)
            console.log('Login Success')
        },
        onSignInError (error) {
            console.log('OH NOES', error)
        }
    }
  }
</script>
