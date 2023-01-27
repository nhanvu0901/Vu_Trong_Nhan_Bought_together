<template>
  <div class="customization">

     <div class="btn-container">
       <a-button class="cancel-btn">Cancel</a-button>
      <a-button class="save-btn" @click="savePreview" style="background-color: #1D1E21; color:#FFFFFF ">Save</a-button>
    </div>
    <h2
        style="font-style: normal;
    font-weight: 600;
    font-size: 20px;
    line-height: 22px;

    /* identical to box height, or 110% */

    color: #000000;

    ">Settings             <svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M0 6C0 2.6865 2.6865 0 6 0C9.3135 0 12 2.6865 12 6C12 9.3135 9.3135 12 6 12C2.6865 12 0 9.3135 0 6ZM6.67501 7.20115H5.39337V7.11654C5.39992 5.93719 5.68836 5.76447 6.21774 5.44746C6.27369 5.41396 6.33232 5.37885 6.3936 5.34077C6.83188 5.06548 7.16874 4.71775 7.16874 4.21065C7.16874 3.64197 6.72322 3.27251 6.16903 3.27251C5.6583 3.27251 5.1748 3.51123 5.1422 4.1922H3.78223C3.81845 2.81578 4.90852 2.1 6.17627 2.1C7.55994 2.1 8.51256 2.96825 8.51256 4.19254C8.51256 5.02202 8.09601 5.56534 7.42954 5.96378C7.37879 5.99491 7.33125 6.02353 7.28673 6.05034C6.81326 6.33539 6.68163 6.41464 6.67501 7.11654V7.20115ZM6.77747 9.00841C6.77384 9.45031 6.40801 9.80528 5.98059 9.80528C5.53869 9.80528 5.18009 9.45031 5.18372 9.00841C5.18009 8.57375 5.53869 8.21877 5.98059 8.21877C6.40801 8.21877 6.77384 8.57375 6.77747 9.00841Z" fill="#5C5F62"/>
</svg>
</h2>

    <div class="setting-container">

    <div class="config">
      <h3 class="header-label"><svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M0 6C0 2.6865 2.6865 0 6 0C9.3135 0 12 2.6865 12 6C12 9.3135 9.3135 12 6 12C2.6865 12 0 9.3135 0 6ZM6.67501 7.20115H5.39337V7.11654C5.39992 5.93719 5.68836 5.76447 6.21774 5.44746C6.27369 5.41396 6.33232 5.37885 6.3936 5.34077C6.83188 5.06548 7.16874 4.71775 7.16874 4.21065C7.16874 3.64197 6.72322 3.27251 6.16903 3.27251C5.6583 3.27251 5.1748 3.51123 5.1422 4.1922H3.78223C3.81845 2.81578 4.90852 2.1 6.17627 2.1C7.55994 2.1 8.51256 2.96825 8.51256 4.19254C8.51256 5.02202 8.09601 5.56534 7.42954 5.96378C7.37879 5.99491 7.33125 6.02353 7.28673 6.05034C6.81326 6.33539 6.68163 6.41464 6.67501 7.11654V7.20115ZM6.77747 9.00841C6.77384 9.45031 6.40801 9.80528 5.98059 9.80528C5.53869 9.80528 5.18009 9.45031 5.18372 9.00841C5.18009 8.57375 5.53869 8.21877 5.98059 8.21877C6.40801 8.21877 6.77384 8.57375 6.77747 9.00841Z" fill="#5C5F62"/>
</svg>
    General Configuration</h3>

      <div class="padding-container" style="padding-left: 23px;
display: flex;
flex-direction: column;
gap: 1.5rem;">

      <h3 class="highlight">Widget Title</h3>
      <input type="text" v-model="widget_title" name="title"  style="
          border: 1px solid;
          border-radius: 5px;
          height: 30px;
          width: 75%;
            "/>


      <div class="flex-row-container">
        <div class="input-flex-container">
          <h3>Title Color</h3>

          <div class="input-flex" style="
          display: flex;
          flex-direction: row;
          gap: 1rem;">
            <div id="color-picker" @click="colorTitlePicker" :style="{ 'background-color': title_color  }">
            <input type="color" class="color-input" id="color" v-model="title_color"  @input="InputTitleColorPicker"/>
          </div>

            <input type="text" v-model="title_color" name="title_color"  style="
            border: 1px solid;
            border-radius: 5px;
            height: 30px;"/>
          </div>

        </div>

        <div class="font-size-box">
          <h3>Font Size</h3>


          <select v-model="title_font_size_value" style="
          border: 1px solid;
          border-radius: 5px;
          height: 30px;
           width: 190px;">
            <option disabled value="">Please select one</option>
            <option value="10px">Extra Small</option>
            <option value="15px">Small</option>
            <option value="20px">Medium</option>
            <option value="25px">Large</option>
            <option value="30px">Extra Large</option>
          </select>

        </div>
      </div>






      <h3 class="highlight">Widget Description</h3>
      <input type="text" v-model="widget_description" name="title"  style="
          border: 1px solid;
          border-radius: 5px;
          height: 30px;
          width: 75%;
            "/>

      <div class="flex-row-container">

        <div class="input-flex-container">
          <h3>Description Color</h3>

          <div class="input-flex" style="
          display: flex;
          flex-direction: row;
          gap: 1rem;

          ">
            <div id="color-picker" @click="colorDesPicker" :style="{ 'background-color': des_color  }">
            <input type="color" class="color-input" id="des_color" v-model="des_color"  @input="InputDesColorPicker"/>
          </div>

            <input type="text" v-model="des_color" name="des_color"  style="
            border: 1px solid;
            border-radius: 5px;
            height: 30px;"/>
          </div>

        </div>

        <div class="font-size-box">
          <h3>Font Size</h3>


          <select v-model="description_font_size_value" style="
          border: 1px solid;
          border-radius: 5px;
          height: 30px;width: 190px;">
          <option value="5px">Extra Small</option>
            <option value="10px">Small</option>
            <option value="15px">Medium</option>
            <option value="20px">Large</option>
            <option value="25px">Extra Large</option>
          </select>
        </div>
      </div>




<div class="layout-numpro"
          style="display: flex;
                 justify-content: space-between;




"
        >
          <div class="layout-div">
            <h3 class="highlight">Layout Style</h3>
            <input type="radio" id="layout_style" value="List" v-model="layout_style" />
            <label for="one">List</label>
          </div>

          <div class="num-select">
            <h3 class="highlight">Number of products to show</h3>
            <select v-model="number_product_show" style="
          border: 1px solid;
          border-radius: 5px;
          height: 30px;">
            <option disabled value="">Please select one</option>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
          </select>
          </div>
        </div>

        </div>

       <h3 style="font-size: 18px"><svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M0 6C0 2.6865 2.6865 0 6 0C9.3135 0 12 2.6865 12 6C12 9.3135 9.3135 12 6 12C2.6865 12 0 9.3135 0 6ZM6.67501 7.20115H5.39337V7.11654C5.39992 5.93719 5.68836 5.76447 6.21774 5.44746C6.27369 5.41396 6.33232 5.37885 6.3936 5.34077C6.83188 5.06548 7.16874 4.71775 7.16874 4.21065C7.16874 3.64197 6.72322 3.27251 6.16903 3.27251C5.6583 3.27251 5.1748 3.51123 5.1422 4.1922H3.78223C3.81845 2.81578 4.90852 2.1 6.17627 2.1C7.55994 2.1 8.51256 2.96825 8.51256 4.19254C8.51256 5.02202 8.09601 5.56534 7.42954 5.96378C7.37879 5.99491 7.33125 6.02353 7.28673 6.05034C6.81326 6.33539 6.68163 6.41464 6.67501 7.11654V7.20115ZM6.77747 9.00841C6.77384 9.45031 6.40801 9.80528 5.98059 9.80528C5.53869 9.80528 5.18009 9.45031 5.18372 9.00841C5.18009 8.57375 5.53869 8.21877 5.98059 8.21877C6.40801 8.21877 6.77384 8.57375 6.77747 9.00841Z" fill="#5C5F62"/>
</svg>
 Button Configuration</h3>

      <div style="padding-left: 23px">

      <h3 class="highlight">Button Text</h3>
      <input type="text" v-model="button_text" name="title"  style="
          border: 1px solid;
          border-radius: 5px;
          height: 30px;
          width: 75%;
            "/>
      <h3>Text Color</h3>
      <div id="color-picker" @click="colorTextPicker" :style="{ 'background-color': text_color  }">
            <input type="color" class="color-input" id="text_color" v-model="text_color"  @input="InputTextColorPicker"/>
      </div>

        <input type="text" v-model="text_color" name="text_color"  style="
        border: 1px solid;
        border-radius: 5px;
        height: 30px;
        width: 190px"/>


      <div class="last-two"
      style="
      display: flex;
      justify-content: space-between;
      margin-bottom: 15px;
"

      >
        <div>
          <h3>Background Color</h3>



          <div class="input-flex" style="
          display: flex;
          flex-direction: row;
          gap: 1rem;

          ">
            <div id="color-picker" @click="colorBackgroundColorPicker" :style="{ 'background-color': background_color  }">
                  <input type="color" class="color-input" id="background_color" v-model="background_color"  @input="InputBackgroundColorColorPicker"/>
            </div>

              <input type="text" v-model="background_color" name="background_color"  style="
              border: 1px solid;
              border-radius: 5px;
              height: 30px;
              width: 190px"/>
          </div>
        </div>

        <div>
          <h3>Border Color</h3>

          <div class="input-flex" style="
          display: flex;
          flex-direction: row;
          gap: 1rem;

          ">
              <div id="color-picker" @click="colorBorderColorPicker" :style="{ 'background-color': border_color  }">
                <input type="color" class="color-input" id="border_color" v-model="border_color"  @input="InputBorderColorColorPicker"/>
                </div>

                  <input type="text" v-model="border_color" name="border_color"  style="
                  border: 1px solid;
                  border-radius: 5px;
                  height: 30px;
                  width: 190px"/>
              </div>
          </div>
      </div>



</div>
    </div>

    <div class="preview">
     <h3 class="header-label"><svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M0 6C0 2.6865 2.6865 0 6 0C9.3135 0 12 2.6865 12 6C12 9.3135 9.3135 12 6 12C2.6865 12 0 9.3135 0 6ZM6.67501 7.20115H5.39337V7.11654C5.39992 5.93719 5.68836 5.76447 6.21774 5.44746C6.27369 5.41396 6.33232 5.37885 6.3936 5.34077C6.83188 5.06548 7.16874 4.71775 7.16874 4.21065C7.16874 3.64197 6.72322 3.27251 6.16903 3.27251C5.6583 3.27251 5.1748 3.51123 5.1422 4.1922H3.78223C3.81845 2.81578 4.90852 2.1 6.17627 2.1C7.55994 2.1 8.51256 2.96825 8.51256 4.19254C8.51256 5.02202 8.09601 5.56534 7.42954 5.96378C7.37879 5.99491 7.33125 6.02353 7.28673 6.05034C6.81326 6.33539 6.68163 6.41464 6.67501 7.11654V7.20115ZM6.77747 9.00841C6.77384 9.45031 6.40801 9.80528 5.98059 9.80528C5.53869 9.80528 5.18009 9.45031 5.18372 9.00841C5.18009 8.57375 5.53869 8.21877 5.98059 8.21877C6.40801 8.21877 6.77384 8.57375 6.77747 9.00841Z" fill="#5C5F62"/>
</svg>
 Preview</h3>
      <div class="preview-container"
      style="
       min-height: 335px;
       width: 95%;
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
            <div style=" display: flex"><h3 style="font-weight: 600; color: #000000;">Total:</h3><h3 style="color:#FF0000;font-weight: 600;">{{total_money}} {{currency}}</h3></div>
             <div style="width: 183px;;
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
  grid-template-columns:70% 30%; height: 3rem; align-content: center; padding: 0 7rem 0 2rem;
">
                <div style="display: flex; justify-self: flex-start;  gap: 1rem;">
                <input type="checkbox" :checked="true">
                <div >{{item.item}}</div>
                  </div>

              <div style="display: grid;grid-template-columns: 2fr 3fr;;width: 280px;">
               <div style="color: red">{{item.item_price}} {{currency}}</div>
                <div   style="color: #444444; text-decoration: line-through">{{item.item_compare}} {{currency}}</div>
              </div>

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
  methods:{
    colorTitlePicker(){
      let input = document.getElementById("color")
      input.click()
    },
    InputTitleColorPicker(){
      console.log(this.title_color);
    },

    colorDesPicker(){
      let input = document.getElementById("des_color")
      input.click()
    },
    InputDesColorPicker(){
      console.log(this.des_color);
    },

    colorTextPicker(){
      let input = document.getElementById("text_color")
      input.click()
    },
    InputTextColorPicker(){
      console.log(this.text_color);
    },

    colorBackgroundColorPicker(){
      let input = document.getElementById("background_color")
      input.click()
    },
    InputBackgroundColorColorPicker(){
      console.log(this.background_color);
    },

    colorBorderColorPicker(){
      let input = document.getElementById("border_color")
      input.click()
    },
    InputBorderColorColorPicker(){
      console.log(this.border_color);
    },

    savePreview(){
      this.widget_title_preview = this.widget_title
      this.title_font_size_value_preview = this.title_font_size_value
      this.title_color_preview = this.title_color

      this.widget_description_preview = this.widget_description
      this.description_font_size_value_preview = this.description_font_size_value
      this.des_color_preview = this.des_color

      this.button_text_preview = this.button_text
      this.border_color_preview = this.border_color
      this.text_color_preview = this.text_color
      this.background_color_preview = this.background_color
      this.total_money = 0
      this.list_product.forEach(item =>{
        this.total_money += parseInt(item.item_price)
      })



      let save_item ={//bo sung them vi kkhi add len trang that minh se dung du lieu cua cai nay
        id:1,
        widget_title: this.widget_title,
        widget_description:this.widget_description,
        num_product: this.number_product_show,
        total_price:this.total_money,
        status:true,


        title_color:this.title_color,
        des_color:this.des_color,
        text_color:this.text_color,
        background_color:this.background_color,
        border_color:this.border_color,

        title_font_size_value:this.title_font_size_value,

        description_font_size_value:this.description_font_size_value,

        button_text:this.button_text,
        layout_style:this.layout_style,
        number_product_show:this.number_product_show,
        list_product:JSON.stringify(this.list_product),
         shop_url:this.shop_url,
      }

      console.log(save_item)
      var xmlhttp = new XMLHttpRequest();
       var self = this
        xmlhttp.open("POST", "https://odoo.website/widget_data");
        xmlhttp.setRequestHeader("Content-Type", "application/json");

        xmlhttp.onreadystatechange = function () {
            if (xmlhttp.readyState == 4) {
                if (xmlhttp.status == 200) {


                   console.log(xmlhttp.responseText)
                    // self.isFetch = true
                    // console.log(JSON.parse(JSON.parse(xmlhttp.responseText).result))
                }
            }
        };
        xmlhttp.send(JSON.stringify(save_item))

      // window.list_widget = save_item // ve sau co database thi ko can bien global nay nua

    }

  },
  props:{
    array_save:Array,
    shop_url:String,

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

              self.currency= list_widget.currency



                if(self.array_save.length === 0){
                  self.list_product = JSON.parse(JSON.parse(list_widget.list_product).replace(/'/g, '"'))
                self.total_money =0
                  let count_product = 0
                self.list_product.forEach(item =>{
                      self.total_money += parseInt(item.item_price)
                  count_product++;
                    })
                self.number_product_show = count_product
                }
                else{
                  let count_product = 0
                  self.list_product = JSON.parse(JSON.stringify(self.array_save))
                  self.$emit('reset_array',[])
                  self.list_product.forEach(item =>{

                  count_product++;
                    })
                  self.number_product_show = count_product
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
  grid-template-columns: 48% 52%;
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
  height: 30px;
  padding: 0;
  width: 30px;
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
</style>