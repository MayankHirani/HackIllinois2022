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
      <LoadingScreen v-if="view == 'loading'"></LoadingScreen>
      <HelloWorld v-if="view == 'hello'"></HelloWorld>
    </v-main>
  </v-app>
</template>

<script>
import LoadingScreen from './components/LoadingScreen';
import HelloWorld from './components/HelloWorld';

export default {
  name: 'App',

  components: {
    LoadingScreen,
    HelloWorld,
  },

  data: () => ({
    view: "loading"
  })
};
</script>
