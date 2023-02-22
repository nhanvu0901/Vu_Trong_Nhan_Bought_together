<template>
  <div class="main-integration" style="width: 50vw;
margin: auto;">
    <h1 style="text-align: center">App Owner Infomation</h1>

    <div class="contain">

      <div class="label">


        <h3>Shop URL:</h3>
      </div>

      <div class="flex-input" >


        <input type="text" class="input-integrate"  id="shop_url" v-model="shop_url" />
     </div>



</div>
     <div style="display: flex; justify-content: center; width: 100%;margin-top: 1rem">
       <a-button class="save-btn" @click="savePreview" style="background-color: #1D1E21; color:#FFFFFF;margin-top: 1rem">Save</a-button>
     </div>
    </div>



</template>

<script>
export default {
  name: "Integration",
  data(){
    return{

      shop_url:''
    }
  },
  methods:{
    savePreview(){
      var xmlhttp = new XMLHttpRequest();
      var self = this
      xmlhttp.open("POST", "https://odoo.website/authenticate/user");
      xmlhttp.setRequestHeader("Content-Type", "application/json");
      let param={


        shop_url:this.shop_url,
      }
      xmlhttp.onreadystatechange = function () {
          if (xmlhttp.readyState == 4) {
              if (xmlhttp.status == 200) {

                  console.log(JSON.parse(JSON.parse(xmlhttp.responseText).result))
                  let result = JSON.parse(JSON.parse(xmlhttp.responseText).result);
                  if (result === true){
                    alert("Shop da co user ")
                  }
                  else{
                     alert("Thanh cong")
                  }

              }
          }
      };
      xmlhttp.send(JSON.stringify(param))
    }
  }
}

</script>

<style scoped>
.flex-input{
  display: flex;
flex-direction: column;
  gap: 1rem;
}
.flex-input input{
  border: 1px solid #444;
  width: 35vw;
}
.label{
  display: flex;
flex-direction: column;
  gap: 1rem;
}
.label h3{
  margin: 0px;
  margin-bottom: 0px;
}
.contain{
  display: flex;
justify-content: center;
gap: 2rem;
margin-top: 1rem;
}
</style>