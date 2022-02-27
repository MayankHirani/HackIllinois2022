<template>
    <v-container>
        <div v-if="mymeetups.length">
            <v-row class="pt-3">
                <h1>My Meetups</h1>
            </v-row>
            <v-row class="pt-3" v-for="meetup in mymeetups" :key="meetup.id">
                <v-card width="80%" class="mx-auto">
                    <v-card-title> {{ meetup.restaurant.name }} </v-card-title>
                    <v-card-subtitle> {{ meetup.start.split(' ')[1] }} </v-card-subtitle>
                    <v-card-subtitle> {{ meetup.restaurant.address.address }} </v-card-subtitle>
                    <v-card-actions>
                        <v-dialog width="500">
                            <template v-slot:activator="{ on, attrs }">
                                <v-btn color="red lighten-2" dark v-bind="attrs" v-on="on">See More</v-btn>
                            </template>
                            <template v-slot:default="dialog">
                                <v-card>
                                    <v-card-title class="text-h5 grey lighten-2">
                                        {{meetup.restaurant.name}}
                                    </v-card-title>
                                    <v-card-text class="pt-1"> {{ meetup.restaurant.address.address }} </v-card-text>
                                    <v-card-text> Maximum Attendees: {{ meetup.size }} </v-card-text>
                                    <v-card-text>
                                        <h2>Current Attendees</h2>
                                    </v-card-text>
                                    <ul style="list-style: none;">
                                        <li v-for="emo in meetup.attendees" :key="emo.id" class="pt-2">
                                            <p>{{emo.emoji}}</p>
                                        </li>
                                    </ul>
                                    <v-divider></v-divider>
                                    <v-card-actions>
                                        <v-spacer></v-spacer>
                                        <v-btn
                                            color="primary"
                                            text
                                            @click="dialog.value = false; leaveMeetup(meetup.id)"
                                        >
                                            Leave
                                        </v-btn>
                                    </v-card-actions>
                                </v-card>
                            </template>
                        </v-dialog>
                    </v-card-actions>
                </v-card>
            </v-row>
        </div>
        <div v-if="!meetups.length" class="pt-5">
            <v-row>
                <h1>No Other Meetups To Show</h1>
            </v-row>
        </div>
        <div v-if="meetups.length" class="pt-5">
            <v-row class="pt-3">
                <h1>All Meetups</h1>
            </v-row>
            <v-row class="pt-3" v-for="meetup in meetups" :key="meetup.id">
                <v-card width="80%" class="mx-auto">
                    <v-card-title> {{ meetup.restaurant.name }} </v-card-title>
                    <v-card-subtitle> {{ meetup.start.split(' ')[1] }} </v-card-subtitle>
                    <v-card-subtitle> {{ meetup.restaurant.address.address }} </v-card-subtitle>
                    <v-card-actions>
                        <v-dialog width="500">
                            <template v-slot:activator="{ on, attrs }">
                                <v-btn color="red lighten-2" dark v-bind="attrs" v-on="on">See More</v-btn>
                            </template>
                            <template v-slot:default="dialog">
                                <v-card>
                                    <v-card-title class="text-h5 grey lighten-2">
                                        {{meetup.restaurant.name}}
                                    </v-card-title>
                                    <v-card-text class="pt-1"> {{ meetup.restaurant.address.address }} </v-card-text>
                                    <v-card-text> Maximum Attendees: {{ meetup.size }} </v-card-text>
                                    <v-card-text>
                                        <h2>Current Attendees</h2>
                                    </v-card-text>
                                    <ul style="list-style: none;">
                                        <li v-for="emo in meetup.attendees" :key="emo.id" class="pt-2">
                                            <p>{{emo.emoji}}</p>
                                        </li>
                                    </ul>
                                    <v-divider></v-divider>
                                    <v-card-actions>
                                        <v-spacer></v-spacer>
                                        <v-btn
                                            color="primary"
                                            text
                                            @click="dialog.value = false; joinMeetup(meetup.id)"
                                        >
                                            Join
                                        </v-btn>
                                    </v-card-actions>
                                </v-card>
                            </template>
                        </v-dialog>
                    </v-card-actions>
                </v-card>
            </v-row>
        </div>
    </v-container>
</template>

<script>
  export default {
    name: 'MeetUps',
    data: () => ({
    }),
    props: ['meetups', 'mymeetups', 'user'],
    methods: {
        joinMeetup(mid) {
            console.log(mid)
        },
        leaveMeetup(mid) {
            console.log(mid)
        }
    }
  }
</script>
