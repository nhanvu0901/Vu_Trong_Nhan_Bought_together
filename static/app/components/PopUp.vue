<template>
 <div class="pop-up-container">
   <p style="font-size: 10px;">You have reach the product limitation.
Please untick any products from the list to continue selecting</p>
   <font-awesome-icon @click="ClosePopUp" icon="fa fa-times-circle" style="font-size:15px;color:red;cursor: pointer"/>
 </div>
</template>

<script>
export default {
  name: "PopUp",
  data(){
    return{

    }
  },
  methods:{
    ClosePopUp(e){
      e.preventDefault()


         this.$emit('closePopUp',false)


    }
  }

}
</script>
<style scoped>
.pop-up-container{
  position: fixed;
  top: 4rem;

  height: 53px;
  width: 315px;

  background: #FFFFFF;
  box-shadow: 0px 4px 5px rgba(0, 0, 0, 0.25);
  border-radius: 4px;

  right: 0px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 3px 12px;
  gap: 3px;
}
</style>