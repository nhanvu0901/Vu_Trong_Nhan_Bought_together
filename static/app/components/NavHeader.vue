<template>
 <div class="nav-bar">

    <div class="frame-50">
<!--        <a-button type="primary">Click me!</a-button>-->
       <font-awesome-icon icon="fa-solid  fa-circle-question"/>
       <font-awesome-icon icon="fa-regular fa-bell" />
       <img :src="current_user_image">
    </div>
 </div>
</template>

<script>
import { library } from '@fortawesome/fontawesome-svg-core'
// import { Button } from 'ant-design-vue';
import {faBell} from "@fortawesome/free-regular-svg-icons";
import {faCircleQuestion} from "@fortawesome/free-solid-svg-icons";

library.add(faBell,faCircleQuestion)

export default {
  name: "NavHeader",
  components: {
      // 'a-button': Button,
    },

  data() {
    return{
       current_user_name:'',
       current_user_image:''
    }
  },
   mounted() {


   let queryString = window.location.search
   let urlParams = new URLSearchParams(queryString);
   let shop_url = urlParams.get('shop_url')




     var xmlhttp = new XMLHttpRequest();
      var self = this
      xmlhttp.open("POST", "https://odoo.website/get_current_user_info");
      xmlhttp.setRequestHeader("Content-Type", "application/json");
      let param={


        shop_url:shop_url,
      }
      xmlhttp.onreadystatechange = function () {
          if (xmlhttp.readyState == 4) {
              if (xmlhttp.status == 200) {

                  console.log(xmlhttp.responseText)
                  if(xmlhttp.responseText){
                    self.current_user_image ="data:image/png;base64,"+JSON.parse(JSON.parse(xmlhttp.responseText).result).image_url

                  }


              }
          }
      };
      xmlhttp.send(JSON.stringify(param))
   }
}
</script>

<style scoped>
 .nav-bar{
   z-index: -1  ;

  display: flex;
justify-content: flex-end;

align-items: center;
   height: 83px;
   background: #EFEFEF;
 }
 .frame-50{
   display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
  padding: 0px;
  gap: 26px;


  width: 133px;
  height: 34px;
  right: 25px;

 }
 .frame-50 img{
   width: 34px;
  height: 34px;
   flex: none;
  order: 2;
  flex-grow: 0;
   border-radius: 50%;
   }
 .frame-50 svg{
   width: 17px;
  height: 34px;
 }
</style>