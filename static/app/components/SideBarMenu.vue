<template>
 <div class="sidebar-menu">

    <div class="company-icon">
      <div class="black-circle"></div>
      <p class="company-name">NestScale</p>
    </div>

   <div class="menu-item">

       <div  v-for="tab in tabs" :key="tab" :class="['item', { active: currentTab === tab }]" @click="$emit('setTab', tab)">{{tab}}</div>
<!--     <div class="item">Add Product</div>-->
<!--      <div class="item">Customization</div>-->
<!--      <div class="item">Installation</div>-->
   </div>
 </div>
</template>

<script>
import DashBoard from "./page/DashBoard.vue";

export default {
  name: "SideBarMenu",
  components: {DashBoard},
   props: {
    currentTab:String,
    tabs:Array
  },
}
</script>

<style scoped>
.sidebar-menu{
  /* Auto layout */
z-index: 2;
display: flex;
flex-direction: column;
align-items: flex-start;
padding: 24px 20px 0px;
gap: 32px;


width: 276px;
height: 100%;


background: #EFEFEF;
}
.company-icon{
  display: flex;
flex-direction: row;


padding: 0px;
gap: 12px;

width: 181px;
height: auto;


/* Inside auto layout */

flex: none;
order: 0;
flex-grow: 0;
}
.black-circle{
  width: 46px;
height: 46px;

background: #000000;
border-radius: 50%;
}
.company-name{
  width: 123px;
height: 24px;


font-style: normal;
font-weight: 600;
font-size: 27px;

/* identical to box height, or 89% */


color: #17181A;
}
.menu-item{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 0px;
  gap: 16px;

  width: 236px;
  height: 128px;
}
.menu-item .item{
  display: flex;
flex-direction: row;
align-items: center;
padding: 0px;
gap: 16px;
  cursor: pointer;
  width: 236px;
height: 32px;
justify-content: center;
background: #FFFFFF;
}
</style>