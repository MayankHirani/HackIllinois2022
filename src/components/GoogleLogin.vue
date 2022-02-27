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
        client_id: '982693143054-out9354r1q3qk1oje82nt6r0tm1ca41a.apps.googleusercontent.com'
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
