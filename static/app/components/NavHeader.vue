<template>
 <div class="nav-bar">

    <div class="frame-50">
<!--        <a-button type="primary">Click me!</a-button>-->
       <font-awesome-icon icon="fa-solid  fa-circle-question"/>
       <font-awesome-icon icon="fa-regular fa-bell" />
       <img src="https://s3-alpha-sig.figma.com/img/3a1e/e072/dfbc1dba6a6021fefb76f78e9fa363d0?Expires=1673222400&Signature=VCTofqxzRa-~zTmavUlxnf7vYzWvGFtYR6h9M3alsvXlmo45x60qlsK-Pa7McSRgkrXoIox0lzJ34Y30RpAvs9aB4J4bxLMGAtbXSiMvEKVNPpsZBhenWCFOWG2wrXwLI~HI2L0UZmb09SnlpTfOq1vTvjYX3kQzlZXWQcIbB~0m5veMuk2wfZU578xJzEjuXipJRWIpVtaFmUTKNI8faxDRPJhBR106RAKbkzCecK8sRM377pyYfG3CaMvOeMb3BjDPwu59LIhAKprWE4MLcpAA2Q~yl77P1p5p0Ng1TXSJNVovD~9UPyuzDi55KBZ0yYevaXB7ufAMN8i4P7-cDg__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4">
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