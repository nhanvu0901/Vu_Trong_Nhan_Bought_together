<template>
<div class="add-product">
  <h1 class="title-main">WELCOME, NHAN VU</h1>

  <div  class="table-container">
        <table>
           <tr class="table-col-name" >
            <td>#</td>
            <td>Widget Title</td>
            <td>Widget Description</td>
             <td>Products included</td>
             <td>Total Price</td>
             <td>Status</td>

          </tr>
           <tr class="table-row" >
              <td>1</td>
              <td>{{ this.list_widget.widget_title }}</td>
             <td>{{ this.list_widget.widget_description }}</td>
             <td>{{ this.list_widget.num_product }}</td>
              <td>{{ this.list_widget.total_price }}</td>
             <td><a-switch v-on:click="switchClicked()" v-model:checked="this.list_widget.status"  checked-children="On" un-checked-children="Off" /></td>
           </tr>
        </table>
     </div>
</div>
</template>

<script>
export default {
  name: "DashBoard",
  data(){
    return{
      list_widget :[]
    }
  },
  methods:{
    switchClicked(id){
       var xmlhttp = new XMLHttpRequest();
       var self = this
        xmlhttp.open("POST", "https://odoo.website/modify_status");
        xmlhttp.setRequestHeader("Content-Type", "application/json");
        let param={
          status: this.list_widget.status,
          shop_url:this.shop_url,
        }
        xmlhttp.onreadystatechange =  function () {
            if (xmlhttp.readyState == 4) {
                if (xmlhttp.status == 200) {

                    console.log(xmlhttp.responseText)



                }
            }
        };
        xmlhttp.send(JSON.stringify(param))

    }

  },
 props:{
    array_save:Array,

    shop_url:String
  },
  mounted() {

   if(this.array_save.length === 0){
         var xmlhttp = new XMLHttpRequest();
       var self = this
        xmlhttp.open("POST", "https://odoo.website/get_widget_data");
        xmlhttp.setRequestHeader("Content-Type", "application/json");
       let param={
      data:"hello",
      shop_url:this.shop_url,


    }
        xmlhttp.onreadystatechange = function () {
            if (xmlhttp.readyState == 4) {
                if (xmlhttp.status == 200) {

                    console.log(xmlhttp.responseText)
                    self.list_widget = JSON.parse(JSON.parse(xmlhttp.responseText).result);

                    // self.data =JSON.parse(JSON.parse(xmlhttp.responseText).result);
                    if(self.list_widget.status === 'True'){
                      self.list_widget.status = (self.list_widget.status === 'True')
                    }
                }
            }
        };
        xmlhttp.send(JSON.stringify(param))
   }
   else{
     this.list_widget =[]
   }






  }
}
</script>

<style scoped>
.title-main{
  color: #000000;font-size: 27px;
font-weight: 600;
}
.table-container{

  width: 95%;
 height: 20%;
 overflow-y: scroll;
  margin-left: 1rem;
  margin-top: 1rem;
}
.table-container table{
  width: 100%;
  height: 100%;

}
.table-container table .table-row{
  height: 3rem;
  border-bottom: 1px solid;
}
.table-container table .table-col-name{
   height: 3rem;
   border-bottom: 1px groove #979191;
  border-top: 1px groove #979191;
  color: rgba(0, 0, 0);
  font-weight: 700;
font-size: 14px;
}
</style>