<template>
 <div class="nav-menu">
<!--    <div class="nav-item">Add Product</div>-->
<!--   <div class="nav-item">Customization</div>-->
<!--   <div class="nav-item">Installation</div>-->
      <div  v-for="tab in navbar" :key="tab" :class="['nav-item', { active: currentTab === tab }]" @click="$emit('setTab', tab)">
           {{tab}}
      </div>
 </div>
</template>

<script>
export default {
  name: "NavbarMenu",
  props: {

    currentTab:String,
    tabs:Array
  },
  computed: {
    navbar:function(){
      return this.tabs.filter((item) => item !=="DashBoard" && item !=="Integration")
    }
  }

}
</script>

<style scoped>
.nav-menu{
display: grid;
grid-template-columns:auto auto auto;


margin: auto;
width: 560px;
height: 42px;


/* Grey 2 */

background: #C8C8C8;
border-radius: 4px;
align-items: center;
  padding-right: 5px;
  padding-left: 5px;

}
.nav-item {
  border-radius: 4px;
  padding: 6px 0;
  text-align: center;
  cursor: pointer;
}
.active {
 background: #ffff;
  color: #0F0A19;
}
</style>