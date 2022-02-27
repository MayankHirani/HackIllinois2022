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

    <h1>My Meetups</h1>
    <v-container>
      <ul style="list-style: none;">
        <li v-for="item in mymeetups" :key="item">
            <v-row dense>
                <v-col cols="12">
                <v-card
                    color="#385F73"
                    dark
                >
                    <v-card-title class="text-h5">
                        {{item.restaurant.name}}
                    </v-card-title>

                    <v-card-subtitle>
                        {{item.start}}
                    </v-card-subtitle>
                    <v-card-subtitle>
                         {{item.restaurant.address.address}}
                    </v-card-subtitle>
                       
                    <v-card-actions>
                    <v-dialog v-model="dialog" width="500">
                        <template v-slot:activator="{ on, attrs }">
                            <v-btn
                            color="red lighten-2"
                            dark
                            v-bind="attrs"
                            v-on="on"
                            >
                            See More
                            </v-btn>
                        </template>

                        <v-card>
                            <v-card-title class="text-h5 grey lighten-2">
                            {{item.restaurant.name}}
                            </v-card-title>
                            <v-card-text>
                                {{item.restaurant.address.address}}
                                {{item.size}}
                            </v-card-text>
                            <h2>Current Attendees</h2>
                            <ul style="list-style: none;">
                                <li v-for="emo in item.attendees" :key="emo">
                                    <p>{{emo.emoji}}</p>
                                </li>
                            </ul>
                            <v-divider></v-divider>

                            <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn
                                color="primary"
                                text
                                @click="dialog = false"
                            >
                                Leave
                            </v-btn>
                            </v-card-actions>
                        </v-card>
                        </v-dialog>
                    </v-card-actions>
                </v-card>
                </v-col>
            </v-row>
        </li>
    </ul>
    </v-container>
    <h1>Other Meetups</h1>
    <v-container>
      <ul style="list-style: none;">
        <li v-for="item in meetups" :item="item" :key="item">
            <v-row dense>
                <v-col cols="12">
                <v-card
                    color="#385F73"
                    dark
                >
                    <v-card-title class="text-h5">
                        {{item.restaurant.name}}
                    </v-card-title>

                    
                    <v-card-subtitle>
                        {{item.start}}
                    </v-card-subtitle>
                    <v-card-subtitle>
                         {{item.restaurant.address.address}}
                    </v-card-subtitle>
                       
                    <v-card-actions>
                    <v-dialog v-model="dialog" width="500">
                        <template v-slot:activator="{ on, attrs }">
                            <v-btn
                            color="red lighten-2"
                            dark
                            v-bind="attrs"
                            v-on="on"
                            >
                            See More
                            </v-btn>
                        </template>

                        <v-card>
                            <v-card-title class="text-h5 grey lighten-2">
                            {{item.restaurant.name}}
                            </v-card-title>
                            <v-card-text>
                                {{item.restaurant.address.address}}
                                {{item.size}}
                            </v-card-text>
                            <h2>Current Attendees</h2>
                            <ul style="list-style: none;">
                                <li v-for="emo in item.attendees" :key="emo">
                                    <p>{{emo.emoji}}</p>
                                </li>
                            </ul>
                            <v-divider></v-divider>

                            <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn
                                color="primary"
                                text
                                @click="dialog = false"
                            >
                                Join
                            </v-btn>
                            </v-card-actions>
                        </v-card>
                        </v-dialog>
                    </v-card-actions>
                </v-card>
                </v-col>

            </v-row>
        </li>
    </ul>
    </v-container>
  </v-card>
</template>

<script>
  export default {
    name: 'MeetUps',
    data: () => ({
    }),
  
  }
</script>
