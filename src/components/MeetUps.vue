<template>
  <v-card
    max-width="80%"
    class="mx-auto"
  >
    <v-system-bar
      color="white"
      dark
    >
      <v-spacer></v-spacer>

      <v-icon>mdi-window-minimize</v-icon>

      <v-icon>mdi-window-maximize</v-icon>

      <v-icon>mdi-close</v-icon>
    </v-system-bar>


    <v-container grid-list-md>
      <v-row dense>
        <v-col cols="12">
          <v-card
            color="#385F73"
            dark
          >
            <v-card-title class="text-h5">
              Restaurant Name
            </v-card-title>

            <v-card-subtitle>Restaurant Description</v-card-subtitle>

            <v-card-actions>
              <v-btn text>
                Join Group
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>

        <v-col
          v-for="(item, i) in items"
          :key="i"
          cols="12"
        >
          <v-card
            :color="item.color"
            dark
          >
            <div class="d-flex flex-no-wrap justify-space-between">
              <div>
                <v-card-title
                  class="text-h5"
                  v-text="item.title"
                ></v-card-title>

                <v-card-subtitle v-text="item.artist"></v-card-subtitle>
              </div>

              <v-avatar
                class="ma-3"
                size="125"
                tile
              >
                <v-img :src="item.src"></v-img>
              </v-avatar>
            </div>
          </v-card>
        </v-col>
      </v-row>
      
    </v-container>
  </v-card>
</template>

<script>
  export default {
    name: 'MeetUps',
    data: () => ({
        meetups: [
            {
                "id" : "",
                "start": "",
                "restaurant" : {

                }
            }
        ]
    }),
  
  }
</script>
