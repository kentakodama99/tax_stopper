<template>
  <v-container fluid>
    <v-row class = "pa-3">
      <v-col cols="12">
        <h1 class = "pa-2 text-center">{{sum_money}}円</h1>
      </v-col>
      <v-col class = "pa-3">
        <v-progress-linear
        v-model="current_percent"
        height="100"
        rounded
      >
        <strong>{{ current_percent }}%</strong>
        </v-progress-linear>
      </v-col>
    </v-row>
    <v-row class = "pa-3" justify='center'>
      <v-col cols=12 md=3>
        <v-card class="pa-2 text-center" outlinedtile>
          <span>入力する</span>
        </v-card>
      </v-col>
      <v-col cols=12 md=3>
        <v-card class="pa-2 text-center" outlinedtile>
          <span>変更する</span>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
  import Vue from 'vue'

  export type DataType = {
    sum_money : number,
    strict_money : number
  }
  export default Vue.extend({
    name: 'Home',
    data(): DataType {
      return {
        sum_money : 500000,
        strict_money : 0
      }
    },
    computed: {
      current_percent() : number {
        return Math.ceil(this.sum_money * 100/ 1030000)
      }
    },
    created() {
      this.strict_money = this.sum_money
    },
    methods: {
      scrictParcent() : void {
        this.sum_money = this.strict_money
      }
    }
  })
</script>
