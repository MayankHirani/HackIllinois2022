<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>FoodBuddies</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon v-if="view == 'meet'" @click="view = 'settings'">
        <v-icon>mdi-cog</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <GoogleLogin @setUser="setUser" v-if="view == 'login'"></GoogleLogin>
      <LoadingScreen v-if="view == 'loading'"></LoadingScreen>
      <CantAccess v-if="view == 'cant'"></CantAccess>
      <MeetUps v-if="view == 'meet'"></MeetUps>
      <Settings v-if="view == 'settings'"></Settings>
      <CreateMeetup v-if="view == 'create'"></CreateMeetup>
    </v-main>
  </v-app>
</template>

<script>
import GoogleLogin from './components/GoogleLogin';
import LoadingScreen from './components/LoadingScreen';
import CantAccess from './components/CantAccess';
import MeetUps from './components/MeetUps';
import Settings from './components/Settings';
import CreateMeetup from './components/CreateMeetup';

export default {
  name: 'App',

  components: {
    GoogleLogin,
    LoadingScreen,
    CantAccess,
    MeetUps,
    Settings,
    CreateMeetup
  },
  data: () => ({
    view: "login",
    user: null
  }),
  methods: {
    setUser(googleUser) {
      this.user = googleUser
      this.view = "loading"
    },
    loadMeetups() {
      // LOAD MEETUP DATA AXIOS
    }
  }
};
</script>
