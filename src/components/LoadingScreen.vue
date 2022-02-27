<template>
  <v-container fill-height fluid>
    <v-row align="center" justify="center">
      <g-signin-button
      :params="googleSignInParams"
      @success="onSignInSuccess"
      @error="onSignInError">
      Sign in with Google
    </g-signin-button>
    <!--<v-progress-circular :size="50" color="primary" indeterminate></v-progress-circular>-->
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'LoadingScreen',

    data: () => ({
      googleSignInParams: {
        client_id: '378762485257-kpdup215b67sgg54v37f2267o9d0ejig.apps.googleusercontent.com'
      }
    }),

  methods: {
    onSignInSuccess (googleUser) {
      // `googleUser` is the GoogleUser object that represents the just-signed-in user.
      // See https://developers.google.com/identity/sign-in/web/reference#users
      const profile = googleUser.getBasicProfile()
      console.log('ID: ' + profile.getId());
      console.log('Full Name: ' + profile.getName());
      console.log('Given Name: ' + profile.getGivenName());
      console.log('Family Name: ' + profile.getFamilyName());
      console.log('Image URL: ' + profile.getImageUrl());
      console.log('Email: ' + profile.getEmail());
      this.view = 'hello'
    },
    onSignInError (error) {
      // `error` contains any error occurred.
      console.log('OH NOES', error)
    }
  }
  }
</script>
