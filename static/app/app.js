import {createApp, h} from 'vue/dist/vue.esm-bundler';
import App from './App.vue'
import 'ant-design-vue/dist/antd.css';
import Antd from 'ant-design-vue';
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { fas } from '@fortawesome/free-solid-svg-icons'
import { library } from '@fortawesome/fontawesome-svg-core'
import { far } from '@fortawesome/free-regular-svg-icons';
library.add(fas, far)
createApp(App)
    .component("font-awesome-icon", FontAwesomeIcon).use(Antd)
    .mount('#app')
