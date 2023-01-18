<template>
  <div class="add-product">

    <div class="btn-container">
       <div class="rectangle-small"></div>
       <div class="rectangle-small"></div>
    </div>

    <div class="rectangle-vague"></div>
     <div class="rectangle-vague"></div>
     <div class="big-rectangle"></div>
    <div class="big-rectangle"></div>
  </div>
</template>

<script>
export default {
  name: "Loading"
}
</script>

<style scoped>
.btn-container{
  position: absolute;
top: 111px;
right: 20px;
width: 200px;
height: 200px;
display: flex;
  gap: 1rem;
flex-direction: row;
justify-content: flex-end;
}

.rectangle-vague{
    width: 25%;
  height:22px;
  background: #eee;
  background: linear-gradient(110deg, #ececec 8%, #f5f5f5 18%, #ececec 33%);
    background-size: auto;
  border-radius: 3px;
  margin: 1rem 0;
  background-size: 200% 100%;
  animation: 1.5s shine-5dcf5352 linear infinite;
}
.big-rectangle{
  width: 100%;
  height: 90%;
  background: #eee;
  background: linear-gradient(110deg, #ececec 8%, #f5f5f5 18%, #ececec 33%);
    background-size: auto;
  border-radius: 3px;
  margin: 1rem 0;
  background-size: 200% 100%;
  animation: 1.5s shine-5dcf5352 linear infinite;
}
.rectangle-small{
   width: 100%;
  height: 36px;
  background: #eee;
  background: linear-gradient(110deg, #ececec 8%, #f5f5f5 18%, #ececec 33%);
    background-size: auto;
  border-radius: 3px;
  margin: 1rem 0;
  background-size: 200% 100%;
  animation: 1.5s shine-5dcf5352 linear infinite;
}
@keyframes shine {
	 to {
		 background-position-x: -200%;
	}
}
</style>