<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>FoodBuddies</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon v-if="view == 'meet'" @click="view = 'settings'">
        <v-icon>mdi-cog</v-icon>
      </v-btn>
    </v-app-bar>
    <v-btn @click="openCreate" fab large bottom right absolute>
      <v-icon>mti-plus-circle-outline</v-icon>
    </v-btn>
    <v-main>
      <GoogleLogin @setUser="setUser" v-if="view == 'login'"></GoogleLogin>
      <LoadingScreen v-if="view == 'loading'"></LoadingScreen>
      <CantAccess @setUser="setUser" v-if="view == 'cant'"></CantAccess>
      <MeetUps @joinMeetup="joinMeetup" @leaveMeetup="leaveMeetup" :user="user" :mymeetups="mymeetups" :meetups="meetups" v-if="view == 'meet'"></MeetUps>
      <SettingsPage @updateDistance="updateDistance" @setUser="setUser" :user="user" :distance="distance" v-if="view == 'settings'"></SettingsPage>
      <CreateMeetup :restaurants="restaurants" @createMeetup="createMeetup" v-if="view == 'create'"></CreateMeetup>
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
    distance: 15,
    restaurants: []
  }),
  methods: {
    setUser(googleUser) {
      console.log(this.distance)
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
        this.mymeetups = JSON.parse(response.data.meetups)
        console.log(this.meetups)
        console.log(response)
        this.getLocation()
      })
      .catch(error => {
        console.log(error)
      })
    },
    getLocation() {
      this.$getLocation({
        enableHighAccuracy: false,
        maximumAge: 300000
      })
      .then(coordinates => {
        console.log(coordinates)
        this.loadMeetups(coordinates.lat, coordinates.lng)
      })
    },
    loadMeetups(lat, lon) {
      axios.get('http://localhost:8080/getmeetups', { params: { "id" : this.user.getBasicProfile().getId(), "lat" : lat, "lon" : lon, "distance" : this.distance }})
      .then(response => {
        this.meetups = JSON.parse(response.data.meetups)
        console.log(response)
        this.view = "meet"
      })
      .catch(error => {
        console.log(error)
      })
    },
    joinMeetup(mid, emoji) {
      this.view = "loading"
      axios.get('http://localhost:8080/joinmeetup', { "params" : { "id" : this.user.getBasicProfile().getId(), "emoji" : emoji, "mid" : mid}})
      .then(response => {
        this.setUser(this.user)
        console.log(response)
      })
      .catch(error => {
        console.log(error)
      })
    },
    leaveMeetup(mid) {
      this.view = "loading"
      axios.get('http://localhost:8080/leavemeetup', { "params" : { "id" : this.user.getBasicProfile().getId(), "mid" : mid } })
      .then(response => {
        this.setUser(this.user)
        console.log(response)
      })
      .catch(error => {
        console.log(error)
      })
    },
    updateDistance(dist) {
      this.distance = dist
    },
    createMeetup(rid, time, emoji, size) {
      this.view = "loading"
      console.log(rid)
      console.log(time)
      console.log(emoji)
      console.log(size)
      console.log(this.user.getBasicProfile().getId())
      axios.get('http://localhost:8080/createmeetup', { "params" : { "rid" : rid.toString(), "time" : time, "id" : this.user.getBasicProfile().getId(), "emoji" : emoji, "size" : size } })
      .then(response => {
        this.setUser(this.user)
        console.log(response)
      })
      .catch(error => {
        console.log(error)
      })
    },
    openCreate() {
      this.view = "loading"
      this.$getLocation({
        enableHighAccuracy: false,
        maximumAge: 300000
      })
      .then(coordinates => {
        axios.get('http://localhost:8080/getrestaurants', { params: { "id" : this.user.getBasicProfile().getId(), "lat" : coordinates.lat, "lon" : coordinates.lng, "distance" : this.distance }})
        .then(response => {
          this.restaurants = JSON.parse(response.data.restaurants)
          this.view = "create"
          console.log(this.restaurants)
        })
        .catch(error => {
          console.log(error)
        })
      })
    }
  }
};
</script>
