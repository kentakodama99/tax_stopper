<template>
  <v-container fluid>
    <v-row class = "pa-3">
      <v-col cols = "12">
        <h1 class = "pa-2 text-center">{{sum_money}}円</h1>
      </v-col>
      <v-col class = "pa-3">
        <v-progress-linear
        v-model="current_percent"
        height = "100"
        rounded
      >
        <strong>{{ current_percent }}%</strong>
        </v-progress-linear>
      </v-col>
    </v-row>
    <v-row class = "pa-3" justify = 'center'>
      <v-col cols = "12" md = "3">
        <v-dialog
          v-model = "add.dialog"
          fullscreen
          transition = "dialog-bottom-transition"
        >
          <template v-slot:activator = "{on , attrs}">
            <v-card v-on = "on" v-bind = "attrs" class = "pa-2 text-center" outlinedtile>
              <span>入力する</span>
            </v-card>
          </template>
          <v-card pa>
            <v-toolbar dark color = "primary">
              <v-btn icon dark @click = "closeInputDialog">
                <v-icon>mdi-close</v-icon>
              </v-btn>
            </v-toolbar>
            <v-row class = "pa-3" justify = 'center'>
              <v-card-title cols = 12 class = "text-h4">入力フォーム</v-card-title>
            </v-row>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols = "12" sm = "6">
                    <v-text-field v-model.number = "add.year" label="年"></v-text-field>
                  </v-col>
                  <v-col cols = "12" sm = "3">
                    <v-text-field v-model.number = "add.month" label="月"></v-text-field>
                  </v-col>
                  <v-col cols = "12" sm = "6">
                    <v-text-field v-model.number = "add.income1" counter="10" label="アルバイト1金額入力"></v-text-field>
                  </v-col>
                  <v-col cols = "12" sm = "6">
                    <v-text-field v-model.number = "add.income2" counter="10" label="アルバイト2金額入力"></v-text-field>
                  </v-col>
                </v-row>
                <v-row class = "pa-3">
                  <v-col cols = "12">
                    <span class = "subtitle-1 font-weight-bold">合計金額</span>
                  </v-col>
                  <v-col cols = "12">
                    <span class = "text-h2 font-weight-bold" >{{add.income1 + add.income2}}円</span>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-row class = "pa-3" justify = 'center'>
                <v-btn color="depressed" outlined @click="submitInputData">
                  <span class = "text-h5 ">保存する</span>
                </v-btn>
              </v-row>
            </v-card-actions>
          </v-card>
        </v-dialog>
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
    strict_money : number,
    add : {
      dialog : boolean,
      year : number,
      month : number,
      income1 : number,
      income2 : number
    },
  }
  export default Vue.extend({
    name: 'Home',
    data(): DataType {
      return {
        sum_money : 500000,
        strict_money : 0,
        add:{
          dialog : false,
          year : 2022,
          month : 1,
          income1 : 0,
          income2 : 0,
        }
      }
    },
    computed: {
      current_percent : {
        get()  : number {
          return Math.ceil(this.sum_money * 100/ 1030000)
        },
        set()  : number {
          return Math.ceil(this.sum_money * 100/ 1030000)
        },
      },
    },
    created() {
      this.strict_money = this.sum_money
    },
    methods: {
      scrictParcent() : void {
        this.sum_money = this.strict_money
      },
      submitInputData() : void {
        if(this.add.year && this.add.month) {
          if ((typeof this.add.income1 !== "number") || (this.add.income1 < 0)) {
            this.add.income1 = 0
          }
          if ((typeof this.add.income2 !== "number") || (this.add.income2 < 0)) {
            this.add.income2 = 0
          }
          if (confirm("本当によろしいでしょうか？\n" +
          this.add.year + "/" + this.add.month + "\n" +
          "アルバイト1 : " + this.add.income1 + "\n" + "アルバイト2 : " + this.add.income2)) {
            this.sum_money += this.add.income1 + this.add.income2
            this.closeInputDialog()
          }
        } else {
          alert("年月を入力してください")
        }
      },
      closeInputDialog() : void {
        this.add.year = 2022
        this.add.month = 1
        this.add.income1 = 0
        this.add.income2 = 0
        this.add.dialog =! this.add.dialog
      }
    }
  })
</script>
