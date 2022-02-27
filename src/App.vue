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
      <CantAccess @setUser="setUser" v-if="view == 'cant'"></CantAccess>
      <MeetUps :mymeetups="mymeetups" :meetups="meetups" v-if="view == 'meet'"></MeetUps>
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
import SettingsPage from './components/SettingsPage';
import CreateMeetup from './components/CreateMeetup';
import axios from 'axios';

export default {
  name: 'App',

  components: {
    GoogleLogin,
    LoadingScreen,
    CantAccess,
    MeetUps,
    SettingsPage,
    CreateMeetup
  },
  data: () => ({
    view: "login",
    user: null,
    mymeetups: [],
    meetups: [],
    distance: 15
  }),
  methods: {
    setUser(googleUser) {
      this.user = googleUser
      if (this.user == null) {
        this.view = "login"
        return
      }
      if (this.user.getBasicProfile().getEmail().split("@")[1] != "illinois.edu") {
        this.view = "cant"
        return
      }
      this.view = "loading"
      this.loadMyMeetups()
    },
    loadMyMeetups() {
      axios.get('http://localhost:8080/getmymeetups', { params: { "id" : this.user.getBasicProfile().getId() }})
      .then(response => {
        this.mymeetups = response
        this.getLocation()
      })
      .catch(error => {
        console.log(error)
      })
    },
    getLocation() {
      this.$getLocation({
        enableHighAccuracy: true,
        maximumAge: 300000
      })
      .then(coordinates => {
        this.loadMeetups(coordinates.latitude, coordinates.longitude)
      })
    },
    loadMeetups(lat, lon) {
      axios.get('http://localhost:8080/getmeetups', { params: { "id" : this.user.getBasicProfile().getId(), "lat" : lat, "lon" : lon, "distance" : this.distance }})
      .then(response => {
        this.meetups = response
        this.view = "meet"
      })
      .catch(error => {
        console.log(error)
      })
    }
  }
};
</script>
