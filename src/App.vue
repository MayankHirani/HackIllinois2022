<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>FoodBuddies</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon v-if="view == 'list'" @click="view = 'settings'">
        <v-icon>mdi-cog</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <GoogleLogin @setUser="setUser" v-if="view == 'login'"></GoogleLogin>
      <LoadingScreen v-if="view == 'loading'"></LoadingScreen>
      <MeetUps v-if="view == 'list'"></MeetUps>
    </v-main>
  </v-app>
</template>

<script>
import GoogleLogin from './components/GoogleLogin';
import LoadingScreen from './components/LoadingScreen';
import MeetUps from './components/MeetUps';

export default {
  name: 'App',

  components: {
    GoogleLogin,
    LoadingScreen,
    MeetUps
  },
  data: () => ({
    view: "login",
    user: null
  }),
  methods: {
    setUser(googleUser) {
      this.user = googleUser
      this.view = "loading"
    }
  }
};
</script>
