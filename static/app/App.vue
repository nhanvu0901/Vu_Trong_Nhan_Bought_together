<template>
  <div class="main-container">
    <SideBarMenu :tabs="tabs" :currentTab="currentTab" @setTab="setTab" class="side-menu"/>
      <NavHeader class="header"/>


    <div class="content-container">
     <div v-if="currentTab !=='DashBoard' && currentTab !=='Integration'">
       <NavbarMenu :tabs="tabs" :currentTab="currentTab" @setTab="setTab"/>
     </div>

      <component @setHome = setHome @reset_array="reset_array" @fetch_to_custom="fetch_save_array" :shop_url="shop_url"  :array_save="array_save"  :data="data" :is="currentTab"  class="tab" :isOpenPopUp="isOpenPopUp" @setPopUp="setPopUp"></component>
    </div>

   <div  v-if="isOpenPopUp" class="active">
      <PopUp  @closePopUp="closePopUp"/>
   </div>

  </div>
</template>

<script>
import NavHeader from "./components/NavHeader.vue";
import NavbarMenu from "./components/NavbarMenu.vue";
import SideBarMenu from "./components/SideBarMenu.vue";
import AddProduct from "./components/page/AddProduct.vue";
import Customization from "./components/page/Customization.vue";
import Installation from "./components/page/Installation.vue";
import PopUp from "./components/PopUp.vue";
import Loading from "./components/page/Loading.vue";
import DashBoard from "./components/page/DashBoard.vue";
import Integration from "./components/page/Integration.vue";
window.value = [];
window.widget_title = ''
window.title_font_size_value = '20px'
window.title_color = '#000000'

window.widget_description = ''
window.description_font_size_value= '15px'
window.des_color= '#000000'


window.button_text= "BUY NOW"
window.border_color= '#000000'
window.text_color= '#000000'
window.background_color= "#1890FF"



window.global_recommend_list =[]
window.global_exclude_list =[]

window.list_widget =''


export default {
    name: "App",
    components:{
      DashBoard,
      Loading,
      PopUp,
      NavHeader,
      NavbarMenu,
      SideBarMenu,
      AddProduct,
      Customization,
      Installation,
      Integration
    },
  data() {
        return {
            currentTab: 'AddProduct',
            tabs: ['AddProduct', 'Customization','Installation','DashBoard','Integration'],
            isOpenPopUp : false,

            data:[],
            array_save:[],
            shop_url:'',

        }
    },
  methods: {
    reset_array(data){
      this.array_save =data
    },
    fetch_save_array(selected_array){
     this.array_save = selected_array
    },
    setTab(tab) {
      this.currentTab = tab
    },
     setHome(tab) {
      this.currentTab = tab
    },
    setPopUp(flag){
       this.isOpenPopUp = flag
       setTimeout(() => this.isOpenPopUp = false, 3000);
    },
    closePopUp(flag){

      this.isOpenPopUp = flag
    }
  },
 mounted() {
  let queryString = window.location.search
   let urlParams = new URLSearchParams(queryString);
  this.shop_url = urlParams.get('shop_url')



   console.log(this.shop_url)



 }
}

</script>
<style>
#app{
  height: auto;
  margin: 0;
  box-sizing: 0;
}
.page-component{
  position: absolute;
  top: 9rem;
  left: 18rem;
  width: 80vw;

  height: auto;
  overflow: hidden;
}
.side-menu{
  grid-area: menu;
}
.header{
  grid-area: header;
}

.content-container{
  height: 100%;
  grid-area: main;
  padding: 0 1rem;
  overflow-y: scroll;
  margin-top:14px;
  }

.main-container{
  width: 100%;
  height: 100%;
  display: grid;
  grid-template-areas:
    'menu header'
    'menu main'

    ;
  grid-template-rows: 83px 1fr;
  grid-template-columns: 276px
  /*gap: 10px;*/
}
</style>