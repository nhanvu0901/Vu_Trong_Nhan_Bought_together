<template xmlns="http://www.w3.org/1999/html">
   <div class="btn-container">
       <button  @click="$emit('setHome', 'DashBoard')"   style="
        padding: 4px 12px;
        gap: 4px;
        width: 64px;
        height: 32px;
        background: #E2E2E2;
        border-radius: 4px;
        border: none;
        cursor: pointer;
        color: #FFFFFF;
">Home</button>
      <button style="
      cursor: pointer;
      border: none;
padding: 4px 12px;
width: 219px;
height: 32px;background: #1D1E21;
border-radius: 4px;
color: #FFFFFF;
" class="save-btn" @click="redirectStore">Go to Themes Customization</button>
    </div>
  <div class="add-product" style="
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      color: #000000;
      margin-top: 3rem;
">

    <h1 style="font-weight: 700;
font-size: 20px;
line-height: 22px;">CONGRATULATION! YOU HAVE CREATED WIDGET SUCCESSFULLY! </h1>
<h3 style="font-weight: 700;
font-size: 14px;
line-height: 22px;

/* identical to box height, or 157% */

color: #000000;

">Now please follow these steps below to display it on your product pages</h3>



    <div class="preview">

      <div class="preview-container"
      style="

      min-width: 553px;
       min-height: 335px;
       padding:1rem;
       border: 1px solid #BFBFBF;
      border-radius: 5px;">
        <div :style="{ color: title_color_preview, fontSize: title_font_size_value_preview}"
           style="text-align: center">
          {{widget_title_preview}}
        </div>

        <div :style="{ color: des_color_preview, fontSize: description_font_size_value_preview}"
           style="text-align: center;margin: 1rem 0; font-weight: 700;">
          {{widget_description_preview}}
        </div>



        <div class="image-button-price" style="display: flex;align-items: center ;justify-content: space-evenly;">
           <div class="list-image-container" style="display: flex;align-items: center">
                <div v-for="(item,index) in list_product">
                  <div v-if="index === list_product.length-1">
                      <img :src="item.item_img" style="width: 65px;height: 61px; border: 1px solid #E2E2E2;
    border-radius: 6px;">
                  </div>
                  <div v-else style="display: flex; align-items: center">
                     <img :src="item.item_img" style="width: 65px;height: 61px; border: 1px solid #E2E2E2;
    border-radius: 6px;">
                     <div style="font-size: 20px">+</div>
                  </div>
                </div>
           </div>


          <div class="price-button-container" style="display: flex; flex-direction: column;justify-content: center;align-items: center">
            <div style="display: flex"><h3 style="font-weight: 600; color: #000000;">Total:</h3><h3 style="color:#FF0000;font-weight: 600;">{{total_money}} {{currency}}</h3></div>
             <div style="width: 183px;
                        padding: 10px;
                        border-radius: 3px;

                        text-align: center"
                   :style="{ color: text_color_preview, backgroundColor:background_color_preview,border:'1px solid'+border_color_preview}">
             {{button_text_preview}}
             </div>
          </div>
      </div>

      <div   class="checkbox-name-container" style="display: flex; flex-direction: column">
         <div v-for="(item,index) in list_product" class="row-item" style="display: grid;  display: inline-grid;
  grid-template-columns:70% 30%; height: 3rem; align-content: center; padding: 0 4rem;
">
                <div style="display: flex; justify-self: flex-start;  gap: 1rem;">
                <input type="checkbox" :checked="true">
                <div >{{item.item}} {{currency}}</div>
                  </div>

              <div style="display: grid;gap: 1rem;grid-template-columns: 1fr 1fr;width: 220px;">
               <div style="color: red">{{item.item_price}} {{currency}}</div>
                <div   style="color: #444444; text-decoration: line-through">{{item.item_compare}}</div>
              </div>

         </div>
      </div>
      </div>
    </div>


    </div>


</template>

<script>
export default {
  name: "Customization",
  data(){
    return{
      total_money:0,

      title_color:'#000000',
      des_color:'#000000',
      text_color:'#000000',
      background_color:'#000000',
      border_color:'#000000',
      widget_title:'',
      title_font_size_value:'20px',

      description_font_size_value:'15px',
      widget_description:'',
      button_text:'BUY NOW',
      layout_style:'',
      number_product_show:'3',


      //preview
      title_color_preview:'#000000',
      des_color_preview:'#000000',
      text_color_preview:'#000000',
      background_color_preview:'#000000',
      border_color_preview:'#000000',
      widget_title_preview:'',
      title_font_size_value_preview:'20px',

      description_font_size_value_preview:'15px',
      widget_description_preview:'',
      button_text_preview:'BUY NOW',
      layout_style_preview:'',
      number_product_show_preview:'3',


      //list product
      list_product:[],
      currency:''


    }
  },
  props:{
    array_save:Array,
    shop_url:String,

  },
  methods:{
    redirectStore(){
      window.location.href ="https://shoplify-odoo.myshopify.com/"
    }
  },
  mounted() {
    console.log(this.array_save)

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
                let list_widget = JSON.parse(JSON.parse(xmlhttp.responseText).result);

                self.widget_title= list_widget.widget_title
                self.title_font_size_value= list_widget.title_font_size_value
                self.title_color= list_widget.title_color

                self.widget_description= list_widget.widget_description
                self.description_font_size_value= list_widget.description_font_size_value
                self.des_color= list_widget.des_color


                self.button_text=list_widget.button_text
                self.border_color= list_widget.border_color
                self.text_color= list_widget.text_color
                self.background_color= list_widget.background_color





               self.widget_title_preview =  list_widget.widget_title
                self.title_font_size_value_preview = list_widget.title_font_size_value
                self.title_color_preview = list_widget.title_color

                self.widget_description_preview = list_widget.widget_description
                self.description_font_size_value_preview =  list_widget.description_font_size_value
                self.des_color_preview =  list_widget.des_color


                self.button_text_preview = list_widget.button_text
                self.border_color_preview = list_widget.border_color
                self.text_color_preview = list_widget.text_color
                self.background_color_preview = list_widget.background_color
                self.currency = list_widget.currency

                if(self.array_save.length === 0){
                  self.list_product = JSON.parse(JSON.parse(list_widget.list_product).replace(/'/g, '"'))
                self.total_money =0
                self.list_product.forEach(item =>{
                      self.total_money += parseInt(item.item_price)
                    })
                }
                else{
                  self.list_product = JSON.parse(JSON.stringify(self.array_save))
                  self.$emit('reset_array',[])
                }




            }
        }
    };
    xmlhttp.send(JSON.stringify(param))



  },

}
</script>

<style scoped>
.customization{
  width: 100%;
  height: 100%;
}
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
.setting-container{
  display: grid;
  grid-template-columns: 50% 50%;
  gap: 1rem;
}
.highlight{
  color: #000000;
  font-weight: 600;
}

.config{
  display: flex;
  gap: 1rem;
  flex-direction: column;
}

#color-picker {
  border: 1px solid;
  border-radius: 25px;
  height: 50px;
  padding: 0;
  width: 50px;
}
.color-input{
  display: none;
}

.flex-row-container{
  display: flex;
  justify-content: space-between;
}
.header-label{
  font-size: 18px;
}
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
</style>