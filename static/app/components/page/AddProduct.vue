<template>
  <div  v-if="isFetch">
  <div class="add-product">
    <div class="btn-container">
       <a-button class="cancel-btn">Cancel</a-button>
      <a-button class="save-btn" @click="SaveProduct">Save</a-button>
    </div>

      <div class="widget-container">
        <p style="margin-left: 15px;">Enable Widget</p>
        <a-switch v-model:checked="checked1" checked-children="On" un-checked-children="Off" />
      </div>

      <div class="recommend-container">
        <p class="manual">Manual Recommendation <svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M0 6C0 2.6865 2.6865 0 6 0C9.3135 0 12 2.6865 12 6C12 9.3135 9.3135 12 6 12C2.6865 12 0 9.3135 0 6ZM6.67501 7.20115H5.39337V7.11654C5.39992 5.93719 5.68836 5.76447 6.21774 5.44746C6.27369 5.41396 6.33232 5.37885 6.3936 5.34077C6.83188 5.06548 7.16874 4.71775 7.16874 4.21065C7.16874 3.64197 6.72322 3.27251 6.16903 3.27251C5.6583 3.27251 5.1748 3.51123 5.1422 4.1922H3.78223C3.81845 2.81578 4.90852 2.1 6.17627 2.1C7.55994 2.1 8.51256 2.96825 8.51256 4.19254C8.51256 5.02202 8.09601 5.56534 7.42954 5.96378C7.37879 5.99491 7.33125 6.02353 7.28673 6.05034C6.81326 6.33539 6.68163 6.41464 6.67501 7.11654V7.20115ZM6.77747 9.00841C6.77384 9.45031 6.40801 9.80528 5.98059 9.80528C5.53869 9.80528 5.18009 9.45031 5.18372 9.00841C5.18009 8.57375 5.53869 8.21877 5.98059 8.21877C6.40801 8.21877 6.77384 8.57375 6.77747 9.00841Z" fill="#5C5F62"/>
</svg>
</p>
        <p class="choose"> <svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M0 6C0 2.6865 2.6865 0 6 0C9.3135 0 12 2.6865 12 6C12 9.3135 9.3135 12 6 12C2.6865 12 0 9.3135 0 6ZM6.67501 7.20115H5.39337V7.11654C5.39992 5.93719 5.68836 5.76447 6.21774 5.44746C6.27369 5.41396 6.33232 5.37885 6.3936 5.34077C6.83188 5.06548 7.16874 4.71775 7.16874 4.21065C7.16874 3.64197 6.72322 3.27251 6.16903 3.27251C5.6583 3.27251 5.1748 3.51123 5.1422 4.1922H3.78223C3.81845 2.81578 4.90852 2.1 6.17627 2.1C7.55994 2.1 8.51256 2.96825 8.51256 4.19254C8.51256 5.02202 8.09601 5.56534 7.42954 5.96378C7.37879 5.99491 7.33125 6.02353 7.28673 6.05034C6.81326 6.33539 6.68163 6.41464 6.67501 7.11654V7.20115ZM6.77747 9.00841C6.77384 9.45031 6.40801 9.80528 5.98059 9.80528C5.53869 9.80528 5.18009 9.45031 5.18372 9.00841C5.18009 8.57375 5.53869 8.21877 5.98059 8.21877C6.40801 8.21877 6.77384 8.57375 6.77747 9.00841Z" fill="#5C5F62"/>
</svg>
 Choose recommendation product(s)</p>



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
              <img :src="item.product_img" alt="" style="width:200px; height:auto;" :class="{disabled:checked1===false}">
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

        <p class="choose"><svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M0 6C0 2.6865 2.6865 0 6 0C9.3135 0 12 2.6865 12 6C12 9.3135 9.3135 12 6 12C2.6865 12 0 9.3135 0 6ZM6.67501 7.20115H5.39337V7.11654C5.39992 5.93719 5.68836 5.76447 6.21774 5.44746C6.27369 5.41396 6.33232 5.37885 6.3936 5.34077C6.83188 5.06548 7.16874 4.71775 7.16874 4.21065C7.16874 3.64197 6.72322 3.27251 6.16903 3.27251C5.6583 3.27251 5.1748 3.51123 5.1422 4.1922H3.78223C3.81845 2.81578 4.90852 2.1 6.17627 2.1C7.55994 2.1 8.51256 2.96825 8.51256 4.19254C8.51256 5.02202 8.09601 5.56534 7.42954 5.96378C7.37879 5.99491 7.33125 6.02353 7.28673 6.05034C6.81326 6.33539 6.68163 6.41464 6.67501 7.11654V7.20115ZM6.77747 9.00841C6.77384 9.45031 6.40801 9.80528 5.98059 9.80528C5.53869 9.80528 5.18009 9.45031 5.18372 9.00841C5.18009 8.57375 5.53869 8.21877 5.98059 8.21877C6.40801 8.21877 6.77384 8.57375 6.77747 9.00841Z" fill="#5C5F62"/>
</svg>
 Choose excluded product(s)</p>

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
        alert("Products have been saved in customization page.")
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


               var xmlhttpSecond = new XMLHttpRequest();

                xmlhttpSecond.open("POST", "https://odoo.website/get_widget_data");
                xmlhttpSecond.setRequestHeader("Content-Type", "application/json");

                // xmlhttpSecond.onreadystatechange = function () {
                //     if (xmlhttpSecond.readyState == 4) {
                //         if (xmlhttpSecond.status == 200) {
                //
                //             console.log(xmlhttpSecond.responseText)
                //             let list_widget = JSON.parse(JSON.parse(xmlhttpSecond.responseText).result);
                //             let list_product = JSON.parse(JSON.parse(list_widget.list_product).replace(/'/g, '"'))
                //
                //             const result = list_product.filter(item1 => window.value.some(item2 => item1.id === item2.product_id));
                //
                //
                //              result.forEach((item,index)=>{
                //                  self.selected_recommend.splice(index,0,item)
                //              })
                //           console.log(self.selected_recommend)
                //
                //
                //         }
                //     }
                // };
                xmlhttpSecond.send(JSON.stringify(param))



                console.log(self.items_recommend)
            }
        }
    };
    xmlhttp.send(JSON.stringify(param))
    }
    else{
       this.items_recommend = window.value
      this.items_excluded = window.value
      this.isFetch = true
      console.log(window.global_recommend_list)
      this.selected_recommend = window.global_recommend_list
       this.selected_excluded = window.global_exclude_list
    }

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
  opacity: 0.9;
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