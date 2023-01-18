<template>
  <div  v-if="isFetch">
  <div class="add-product">
    <div class="btn-container">
       <a-button class="cancel-btn">Cancel</a-button>
      <a-button class="save-btn" @click="SaveProduct">Save</a-button>
    </div>

      <div class="widget-container">
        <p>Enable Widget</p>
        <a-switch v-model:checked="checked1" checked-children="On" un-checked-children="Off" />
      </div>

      <div class="recommend-container">
        <p class="manual">Manual Recommendation</p>
        <p class="choose">Choose recommendation product(s)</p>



      <div class="search-table">

        <div class="search-container"
        style="
          display: grid;
          grid-template-columns: 90% 10%;
          ">
           <input type="text"  class="search-input"
        placeholder="Search product by name"   v-model="searchRecommend"/>
          <div
          style="
          height: 40px;
          border: 1px solid;
          border-top-right-radius: 5px;
          border-bottom-right-radius: 5px;
          display: flex;
          justify-content: center;
          align-items: center;

          ">
            {{ num_recommend }} Selected
          </div>
      </div>


      <div class="selected-container" style="
        margin-left: 1rem;
         display: flex;
         gap: 1rem;
         margin-top: 1rem;
         margin-bottom: 1rem;

          ">
          <div v-for="item in namesRecommend" class="selected-box" style="
         display: flex;
         gap: 5px;
        justify-content: center;
        align-items: center;
">

            <div style="font-size: 14px;">{{item["item"]}}</div>
              <font-awesome-icon icon="fa fa-times-circle" style="font-size:15px;color:red" @click="unTagRecommend(item['id'])"/>
          </div>
      </div>



     <div  class="table-container">
        <table>
           <tr class="table-col-name" >
            <td></td>
            <td>Image</td>
            <td>Product Name</td>
             <td>Price</td>
             <td>Compare At Price</td>
             <td>In Stock</td>
          </tr>
           <tr v-for="(item,index) in filteredItemsRecommend" :key="item.product_id" class="table-row"  :class="{disabled:checked1===false}">
              <td>
                <input type="checkbox" :id="item.product_id" v-model="selected_recommend[index]" :true-value="{item:item.product_name,id:item.product_id,item_img:item.product_img,item_price:item.product_price,item_compare:item.product_compare_at_price}"  :disabled="checked1 === false"/>
              </td>
              <td>
              <img :src="item.product_img" alt="" style="width:200px; height:auto;">
              </td>
              <td>{{ item.product_name }}</td>
              <td>{{ item.product_price }}</td>
             <td>{{ item.product_compare_at_price }}</td>
             <td>{{ item.quantity }}</td>
           </tr>
        </table>
     </div>

      </div>

    </div>


    <div class="excluded-container">

        <p class="choose">Choose excluded product(s)</p>

          <div class="search-container"
        style="
          display: grid;
          grid-template-columns: 90% 10%;
          ">
           <input type="text"  class="search-input"
        placeholder="Search product by name"  v-model="searchExclude" />
          <div
          style="
          height: 40px;
          border: 1px solid;
          border-top-right-radius: 5px;
          border-bottom-right-radius: 5px;
          display: flex;
          justify-content: center;
          align-items: center;

          ">
           {{ num_exclude }} Selected
          </div>
      </div>

      <div class="selected-container"  style="
        margin-left: 1rem;
         display: flex;
         gap: 1rem;
         margin-top: 1rem;
         margin-bottom: 1rem;

          ">
          <div v-for="item in namesExclude" class="selected-box" style="
         display: flex;
         gap: 5px;
        justify-content: center;
        align-items: center;
">
            <div style="font-size: 14px;" >{{item['item']}}</div>
            <font-awesome-icon icon="fa fa-times-circle" style="font-size:15px;color:red" @click="unTagExclude(item['id'])"/>
          </div>
      </div>


     <div  class="table-container">
        <table>
           <tr class="table-col-name">
            <td></td>
            <td>Image</td>
            <td>Product Name</td>
             <td>Price</td>
             <td>Compare At Price</td>
             <td>In Stock</td>
          </tr>
           <tr v-for="(item,index) in filteredItemsExclude" :key="item.product_id" class="table-row" :class="{disabled:checked1===false}">
              <td>
                <input type="checkbox" :id="item.product_id" v-model="selected_excluded[index]"  :true-value="{item:item.product_name,id:item.product_id,item_img:item.product_img,item_price:item.product_price,item_compare:item.product_compare_at_price}" :disabled="checked1 === false"/>
              </td>
              <td><img :src="item.product_img" alt="" style="width:200px; height:auto;"></td>
              <td>{{ item.product_name }}</td>
              <td>{{ item.product_price }}</td>
             <td>{{ item.product_compare_at_price }}</td>
             <td>{{ item.quantity }}</td>
           </tr>
        </table>
     </div>


    </div>

  </div>
  </div>
  <div v-else>
    <Loading/>
  </div>
</template>

<script>
import {  reactive, toRefs } from 'vue';
import Loading from "./Loading.vue";
export default {
  name: "AddProduct",
 components:{
      Loading,
 },
  data() {
    return {
      shop_url:'',
      isFetch:false,
      searchRecommend:'',
      searchExclude:'',
      selected_recommend: [],
      // items_recommend: [
      //         { product_id: 1, product_img: 'Row 1, Column 1', product_name: 'Nhan', product_price: 'Row 1, Column 3',product_compare_at_price: 'Row 1, Column 3',quantity: 'Row 1, Column 3' },
      //         { product_id: 2, product_img: 'Row 2, Column 1', product_name: 'Row 2, Column 2', product_price: 'Row 2, Column 3',product_compare_at_price: 'Row 1, Column 3',quantity: 'Row 1, Column 3'},
      //     { product_id: 3, product_img: 'Row 2, Column 1', product_name: 'Row 2, Column 2', product_price: 'Row 2, Column 3',product_compare_at_price: 'Row 1, Column 3',quantity: 'Row 1, Column 3' },
      //     { product_id: 4, product_img: 'Row 2, Column 1', product_name: 'Row 2, Column 2', product_price: 'Row 2, Column 3',product_compare_at_price: 'Row 1, Column 3',quantity: 'Row 1, Column 3' },
      //      { product_id: 5, product_img: 'Row 2, Column 1', product_name: 'Row 2, Column 2', product_price: 'Row 2, Column 3',product_compare_at_price: 'Row 1, Column 3',quantity: 'Row 1, Column 3' },
      //      { product_id: 6, product_img: 'Row 2, Column 1', product_name: 'Row 2, Column 2', product_price: 'Row 2, Column 3',product_compare_at_price: 'Row 1, Column 3',quantity: 'Row 1, Column 3'},
      //     { product_id: 7, product_img: 'Row 2, Column 1', product_name: 'Linh', product_price: 'Row 2, Column 3',product_compare_at_price: 'Row 1, Column 3',quantity: 'Row 1, Column 3'},
      //     { product_id: 8, product_img: 'Row 2, Column 1', product_name: 'Row 2, Column 2', product_price: 'Row 2, Column 3',product_compare_at_price: 'Row 1, Column 3',quantity: 'Row 1, Column 3' }
      //       ],
      items_recommend:[],

      selected_excluded: [],
      items_excluded: [],
          //     { product_id: 1, product_img: 'Row 1, Column 1', product_name: 'Nhan', product_price: 'Row 1, Column 3',product_compare_at_price: 'Row 1, Column 3',quantity: 'Row 1, Column 3' },
          //     { product_id: 2, product_img: 'Row 2, Column 1', product_name: 'Row 2, Column 2', product_price: 'Row 2, Column 3',product_compare_at_price: 'Row 1, Column 3',quantity: 'Row 1, Column 3'},
          // { product_id: 3, product_img: 'Row 2, Column 1', product_name: 'Row 2, Column 2', product_price: 'Row 2, Column 3',product_compare_at_price: 'Row 1, Column 3',quantity: 'Row 1, Column 3' },
          // { product_id: 4, product_img: 'Row 2, Column 1', product_name: 'Row 2, Column 2', product_price: 'Row 2, Column 3',product_compare_at_price: 'Row 1, Column 3',quantity: 'Row 1, Column 3' },
          //  { product_id: 5, product_img: 'Row 2, Column 1', product_name: 'Row 2, Column 2', product_price: 'Row 2, Column 3',product_compare_at_price: 'Row 1, Column 3',quantity: 'Row 1, Column 3' },
          //  { product_id: 6, product_img: 'Row 2, Column 1', product_name: 'Row 2, Column 2', product_price: 'Row 2, Column 3',product_compare_at_price: 'Row 1, Column 3',quantity: 'Row 1, Column 3'},
          // { product_id: 7, product_img: 'Row 2, Column 1', product_name: 'Linh', product_price: 'Row 2, Column 3',product_compare_at_price: 'Row 1, Column 3',quantity: 'Row 1, Column 3'},
          // { product_id: 8, product_img: 'Row 2, Column 1', product_name: 'Row 2, Column 2', product_price: 'Row 2, Column 3',product_compare_at_price: 'Row 1, Column 3',quantity: 'Row 1, Column 3' }



    }
  },
   setup() {
    const state = reactive({
      checked1: true,

    });
    return { ...toRefs(state) };
  },



   methods: {

    SaveProduct(e){
      e.preventDefault()
      let sumNum = this.num_recommend

      if(sumNum > 5){
        if(this.isOpenPopUp === false){
          this.$emit('setPopUp',true)
        }
      }
      else{

         if(this.namesExclude.length > 0){

           let fetch_product_list= JSON.parse(JSON.stringify(this.namesRecommend)).filter( (item) => !JSON.parse(JSON.stringify(this.namesExclude)).find((itemFilter) => itemFilter.id == item.id))

           this.$emit('fetch_to_custom',fetch_product_list)
         }
         else{
           this.$emit('fetch_to_custom',JSON.parse(JSON.stringify(this.namesRecommend)))
         }

      }
      window.global_recommend_list = this.selected_recommend

    },

     unTagRecommend(id){
      let indexOfList = 0
      this.selected_recommend.forEach((item,index)=>{
        if( JSON.parse(JSON.stringify(item))['id'] == id){
          indexOfList = index
        }
      })
      delete this.selected_recommend[indexOfList]

      // this.selected_recommend= this.selected_recommend.filter((item) => JSON.parse(JSON.stringify(item))['id'] !== id)
      //  // window.global_recommend_list = this.window.global_recommend_list.filter((item) => JSON.parse(JSON.stringify(item))['id'] !== id)
      // console.log(this.selected_recommend)
     },
     unTagExclude(id){
      let indexOfList = 0
      this.selected_excluded.forEach((item,index)=>{
        if( JSON.parse(JSON.stringify(item))['id'] == id){
          indexOfList = index
        }
      })
      delete this.selected_excluded[indexOfList]
     }
  },

  computed: {
    namesRecommend: function() { return this.selected_recommend.filter(e => e !== false); },
    namesExclude: function() { return this.selected_excluded.filter(e => e !== false); },


    filteredItemsRecommend() {
      return this.items_recommend.filter(item => {
         return item.product_name.toLowerCase().indexOf(this.searchRecommend.toLowerCase()) > -1
      })
    },
    filteredItemsExclude() {
      console.log("Hello")
      return this.items_excluded.filter(item => {
         return item.product_name.toLowerCase().indexOf(this.searchExclude.toLowerCase()) > -1
      })
    },

    num_recommend:function (){

      let num = this.namesRecommend.length
      return num
    },
    num_exclude: function (){
      let num = this.namesExclude.length
      return num
    }




  },
 props: {
    isOpenPopUp:Boolean,
    array_save:Array,

    // data:Array,
  },
   mounted() {
   let queryString = window.location.search
   let urlParams = new URLSearchParams(queryString);
   this.shop_url = urlParams.get('shop_url')
    if(window.value.length === 0 || this.checked1===false){

    var xmlhttp = new XMLHttpRequest();
    var self = this
    xmlhttp.open("POST", "https://odoo.website/fetch_product");
    xmlhttp.setRequestHeader("Content-Type", "application/json");
    let param={
      data:"hello",
      shop_url:this.shop_url,
    }
    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == 4) {
            if (xmlhttp.status == 200) {



                // self.items_recommend =JSON.parse(JSON.parse(xmlhttp.responseText).result);
                window.value = JSON.parse(JSON.parse(xmlhttp.responseText).result);
                self.items_recommend = JSON.parse(JSON.parse(xmlhttp.responseText).result);
                self.items_excluded =  JSON.parse(JSON.parse(xmlhttp.responseText).result);
                self.isFetch = true
                // console.log(JSON.parse(JSON.parse(xmlhttp.responseText).result))
            }
        }
    };
    xmlhttp.send(JSON.stringify(param))
    }
    else{
       this.items_recommend = window.value
      this.items_excluded = window.value
      this.isFetch = true

    }
    console.log(window.global_recommend_list)
    this.selected_recommend = window.global_recommend_list
     this.selected_excluded = window.global_exclude_list
  },
  watch: {
    // whenever question changes, this function will run
   checked1(newOne){
     if(this.checked1 === false){
        var xmlhttp = new XMLHttpRequest();
   var self = this
    xmlhttp.open("POST", "https://odoo.website/fetch_product");
    xmlhttp.setRequestHeader("Content-Type", "application/json");
    let param={
      data:"hello",
      shop_url:this.shop_url,
    }
    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == 4) {
            if (xmlhttp.status == 200) {
                // self.items_recommend =JSON.parse(JSON.parse(xmlhttp.responseText).result);
                window.value = JSON.parse(JSON.parse(xmlhttp.responseText).result);
                self.items_recommend = JSON.parse(JSON.parse(xmlhttp.responseText).result);
                self.items_excluded =  JSON.parse(JSON.parse(xmlhttp.responseText).result);

                // console.log(JSON.parse(JSON.parse(xmlhttp.responseText).result))
            }
        }
    };
    xmlhttp.send(JSON.stringify(param))
     }

   },
  },


}
</script>

<style scoped>
.btn-container{

   display: flex;

  gap: 1rem;
  flex-direction: row;
  justify-content: flex-end;
  margin-top: 1rem;

}
.btn-container button{
  width: 71px;
height: 32px;
  background: #E2E2E2;
border-radius: 4px;
}
.save-btn{
font-family: 'Inter';
font-style: normal;
font-weight: 700;
font-size: 14px;
line-height: 24px;
color: #000000;
}
.add-product{
  width: 100%;

    height: auto;
}
.widget-container{

  display: flex;
}
.widget-container p {
  width: 164px;
height: 22px;
  font-family: 'Inter';
font-style: normal;
font-weight: 600;
font-size: 18px;
line-height: 22px;
}
.recommend-container{
  box-sizing: border-box;


width: 100%;
height: 420px;

background: #FFFFFF;
border: 1px solid #E2E2E2;
}
.manual{
  font-style: normal;
font-weight: 600;
font-size: 20px;
line-height: 22px;

/* identical to box height, or 110% */

color: #000000;
}
 .choose{
  width: 660px;
height: 28px;

margin: 1rem;
font-style: normal;
font-weight: 500;
font-size: 18px;
line-height: 28px;

color: #202223;
}
.search-input{

height: 40px;
margin-left: 1rem;
  border: 1px solid;
border-top-left-radius: 5px;
border-bottom-left-radius: 5px;
border-right: none;
padding-left: 1rem;
}


.table-container{

  width: 95%;
  height: 50%;
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

.disabled{
  color: #D9D9D9;
}

.excluded-container{
  box-sizing: border-box;

width: 100%;
height: 420px;

background: #FFFFFF;
border: 1px solid #E2E2E2;
  margin:1rem 0;
}
.selected-box{
  width: 185px;
  height: 24px;
  border: 1px solid #E2E2E2;
border-radius: 6px;
}
</style>