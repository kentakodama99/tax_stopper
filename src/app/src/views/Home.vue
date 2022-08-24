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
      <v-col cols = "12" md = "6">
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
          <v-card>
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
                    <v-text-field v-if="add.editedidx >= 0" v-model.number = "add.year" label="年" disabled></v-text-field>
                    <v-text-field v-else v-model.number = "add.year" label="年"></v-text-field>
                  </v-col>
                  <v-col cols = "12" sm = "3">
                    <v-text-field v-if="add.editedidx >= 0" v-model.number = "add.month" label="月" disabled></v-text-field>
                    <v-text-field v-else v-model.number = "add.month" label="月"></v-text-field>
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
                <v-btn color="depressed" outlined @click="submitInputItem">
                  <span class = "text-h5 ">保存する</span>
                </v-btn>
              </v-row>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols = "12">
      <v-data-table
        :headers = "table.headers"
        :items = "table.items"
        :items-per-page = -1
        hide-default-footer
        class="elevation-1 mt-3"
      >
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon
          small
          class="mr-2"
          @click="editItem(item)"
        >
          mdi-pencil
        </v-icon>
        <v-icon
          small
          @click="submitdeleteItem(item)"
        >
          mdi-delete
        </v-icon>
      </template>
      </v-data-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
  import Vue from 'vue';
  import { client } from '../client'

  export type HeadersType = {
    text : string,
    value : string,
    sortable : boolean
  }

  export type ItemsType = {
    year : number,
    month : number,
    income1 : number,
    income2 : number
  }
  export type DataType = {
    sum_money : number,
    add : {
      dialog : boolean,
      year : number,
      month : number,
      income1 : number,
      income2 : number,
      editedidx : number
    },
    table : {
      headers : HeadersType[]
      items : ItemsType[]
    }
  }

  export default Vue.extend({
    name: 'Home',
    data(): DataType {
      return {
        sum_money : 0,
        add:{
          dialog : false,
          year : 2022,
          month : 1,
          income1 : 0,
          income2 : 0,
          editedidx : -1,
        },
        table : {
          headers: [
            {
              text: '年',
              value: "year",
              sortable : true
            },
            {
              text: '月',
              value: "month",
              sortable : true
            },
            {
              text: '収入1',
              value: "income1",
              sortable : true
            },
            {
              text: '収入2',
              value: "income2",
              sortable : true
            },
            {
              text: 'Actions',
              value: 'actions',
              sortable: false
            },
          ],
          items : []
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
      this.getData()
    },
    methods: {
      getData() : void {
        const endpoint = "api/paycheck"
        client.get(endpoint).then(res => {
          const data : ItemsType[] = res.data
          if (!data) {
            return
          }
          this.table.items = []
          this.sum_money = 0
          data.forEach(e => {
            this.table.items.push({
              year : Number(e.year),
              month : Number(e.month),
              income1 : Number(e.income1),
              income2 : Number(e.income2),
            })
            this.sum_money += e.income1;
            this.sum_money += e.income2;
          })
        })
      },
      submitInputItem() : void {
        if(this.add.year && this.add.month) {
          if ((typeof this.add.income1 !== "number") || (this.add.income1 < 0)) {
            this.add.income1 = 0
          }
          if ((typeof this.add.income2 !== "number") || (this.add.income2 < 0)) {
            this.add.income2 = 0
          }
          if (
            confirm("本当によろしいでしょうか？\n" +
            this.add.year + "/" + this.add.month + "\n" +
            "収入1 : " + this.add.income1 + "\n" + "収入2 : " + this.add.income2)
          ) {
            const data = {
              "year" : this.add.year,
              "month" : this.add.month,
              "income1" : this.add.income1,
              "income2" : this.add.income2
            }
            if(this.add.editedidx >= 0) { // update
              const endpoint = "api/paycheck/update"
              const targetItem = this.table.items[this.add.editedidx]
              const pre_imcome1 = targetItem.income1
              const pre_imcome2 = targetItem.income2
              client.put(endpoint, data).then(() => {
                Object.assign(targetItem, data);
                this.sum_money -= pre_imcome1
                this.sum_money -= pre_imcome2
                this.sum_money += this.add.income1;
                this.sum_money += this.add.income2;
              })
            } else { // new
              const endpoint = "api/paycheck"
              client.post(endpoint, data).then(() => {
              this.table.items.push(data)
                this.sum_money += this.add.income1;
                this.sum_money += this.add.income2;
              })
            }
            this.closeInputDialog()
          }
        } else {
          alert("年月を入力してください")
        }
      },
      submitdeleteItem(item : any) : void {
        const delete_idx = this.table.items.indexOf(item)
        const deleteItem = Object.assign({}, item)
        if (
          confirm("本当に削除してよろしいでしょうか？\n" +
          deleteItem.year + "/" + deleteItem.month + "\n" +
          "収入1 : " + deleteItem.income1 + "\n" + "収入2 : " + deleteItem.income2)
        ) {
          const data = {
            "year" : deleteItem.year,
            "month" : deleteItem.month,
          }
          const endpoint = "api/paycheck/delete"
          client.post(endpoint, data).then(() => {
            this.table.items.splice(delete_idx, 1);
            this.sum_money -= deleteItem.income1
            this.sum_money -= deleteItem.income2
          })
        }
      },
      editItem (item : any) : void {
        this.add.editedidx = this.table.items.indexOf(item)
        const editedItem = Object.assign({}, item)
        this.add.year = editedItem.year
        this.add.month = editedItem.month
        this.add.income1 = editedItem.income1
        this.add.income2 = editedItem.income2
        this.add.dialog = true
      },
      closeInputDialog() : void {
        this.add.year = 2022
        this.add.month = 1
        this.add.income1 = 0
        this.add.income2 = 0
        this.add.editedidx = -1
        this.add.dialog = false
      }
    }
  })
</script>
