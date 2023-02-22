
let script = document.createElement("SCRIPT")
script.src = "https://cdn.jsdelivr.net/npm/axios@1.1.2/dist/axios.min.js"
document.head.appendChild(script)
function initJQuery(e) {
    var t;
    "undefined" == typeof jQuery ? ((t = document.createElement("SCRIPT")).src = "https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js", t.type = "text/javascript", t.onload = e, document.head.appendChild(t)) : e()
}

initJQuery(function () {
    // if (window.ShopifyAnalytics.meta.page.pageType === "product") {
        console.log("Hello")

       var xmlhttp = new XMLHttpRequest();
       var self = this
        xmlhttp.open("POST", "https://odoo.website/get_widget_data");
        xmlhttp.setRequestHeader("Content-Type", "application/json");
        let param={
          data:"hello",
          shop_url:Shopify.shop
        }
        xmlhttp.onreadystatechange = function () {
            if (xmlhttp.readyState == 4) {
                if (xmlhttp.status == 200) {
                    let list_widget = JSON.parse(JSON.parse(xmlhttp.responseText).result);

                    console.log(list_widget)
                    let product_list = JSON.parse(JSON.parse(list_widget.list_product).replace(/'/g, '"'))
                    console.log(product_list)
                    if(list_widget.status === 'True') {
                        if (window.ShopifyAnalytics.meta.product) {
                            let product_id = window.ShopifyAnalytics.meta.product.id
                            let flag = false
                            product_list.forEach(product => {
                                if (product_id === parseInt(product.id)) {
                                    console.log(product.id)
                                    flag = true
                                }
                            })
                            if (flag === true) {

                                let currency = ShopifyAnalytics.meta.currency


                                let widget_title_preview = list_widget.widget_title
                                let title_font_size_value_preview = list_widget.title_font_size_value
                                let title_color_preview = list_widget.title_color

                                let widget_description_preview = list_widget.widget_description
                                let description_font_size_value_preview = list_widget.description_font_size_value
                                let des_color_preview = list_widget.des_color


                                let button_text_preview = list_widget.button_text
                                let border_color_preview = list_widget.border_color
                                let text_color_preview = list_widget.text_color
                                let background_color_preview = list_widget.background_color

                                // let shopify_section = document.getElementById('shopify-section-template--16642483388661__main')
                                let main = document.querySelector('main[role="main"]')
                                let preview_container = document.createElement('DIV')
                                preview_container.classList.add("preview-container")
                                preview_container.style.cssText = " width: 895px;\n" +
                                    "       min-height: 400px;\n" +
                                    "       padding:1rem;\n" +
                                    "border: 1px solid #BFBFBF;\n"+
                                    "      border-radius: 5px;margin:auto;  \n"

                                let widget_title = document.createElement("DIV")
                                widget_title.innerHTML = widget_title_preview
                                widget_title.style.cssText = "text-align: center; color:" + title_color_preview + ";font-size:" + title_font_size_value_preview + ";"
                                preview_container.appendChild(widget_title)

                                let widget_description = document.createElement("DIV")
                                widget_description.innerHTML = widget_description_preview

                                widget_description.style.cssText = "text-align: center;margin: 1rem 0; font-weight: 700;color:" + des_color_preview + ";font-size:" + description_font_size_value_preview + ";"
                                preview_container.appendChild(widget_description)


                                let image_button_price = document.createElement('DIV')
                                image_button_price.style.cssText = "display: flex;align-items: center ;justify-content: space-evenly; margin-bottom: 2rem;"

                                let list_image_container = document.createElement("DIV")
                                list_image_container.style.cssText = "display: flex;align-items: center; gap:10px"
                                product_list.forEach((product, index) => {
                                    let product_image = document.createElement("IMG")
                                    product_image.style.cssText = 'width: 65px;height: 61px; border: 1px solid #E2E2E2;\n' +
                                        '    border-radius: 6px;'
                                    if (index === product_list.length - 1) {
                                        product_image.src = product.item_img
                                        list_image_container.appendChild(product_image)
                                    } else {
                                        product_image.src = product.item_img
                                        let plus = document.createElement("DIV")
                                        plus.style.cssText = 'font-weight: 600;font-size: 16px;line-height: 22px;color: #000000;'
                                        plus.innerHTML = '+'
                                        list_image_container.appendChild(product_image)
                                        list_image_container.appendChild(plus)
                                    }

                                })
                                let price_button_container = document.createElement("DIV")
                                price_button_container.style.cssText = "display: flex; flex-direction: column;justify-content: center;align-items: center"
                                let total_container = document.createElement("DIV")
                                total_container.style.cssText = "display: flex"
                                let total_h3 = document.createElement("H3")
                                total_h3.style.cssText = "font-weight: 600; color: #000000;white-space: normal;"
                                total_h3.innerHTML = "Total:"
                                total_container.appendChild(total_h3)
                                 let total_money = document.createElement("H3")
                                total_money.style.cssText = "color:#FF0000;font-weight: 600;"
                                total_money.innerHTML = list_widget.total_price + currency
                                total_container.appendChild(total_money)

                                price_button_container.appendChild(total_container)

                                let button = document.createElement("DIV")
                                button.style.cssText= "color:" + text_color_preview+";"+"background-color:" +background_color_preview+";"+ "border: 1px solid"+border_color_preview+";"+"width: 100%;padding: 10px; border-radius: 3px; text-align: center;cursor: pointer;"

                                button.innerHTML = button_text_preview





                                button.addEventListener("click", function(){
                                   var xmlhttp = new XMLHttpRequest();
                                   var self = this
                                    xmlhttp.open("POST", "https://odoo.website/make_draft_order");
                                    xmlhttp.setRequestHeader("Content-Type", "application/json");
                                     let param={
                                              data:"hello",
                                              product_list:product_list,
                                            shop_url:Shopify.shop
                                            }
                                    xmlhttp.onreadystatechange = function () {
                                        if (xmlhttp.readyState == 4) {
                                            if (xmlhttp.status == 200) {


                                               console.log(xmlhttp.responseText)

                                             window.open(JSON.parse(JSON.parse(xmlhttp.responseText).result), '_blank');

                                            }
                                        }
                                    };
                                    xmlhttp.send(JSON.stringify(param))

                                });










                                price_button_container.appendChild(button)

                                image_button_price.appendChild(list_image_container)
                                image_button_price.appendChild(price_button_container)
                                preview_container.appendChild(image_button_price)

                                let checkbox_name_container = document.createElement("DIV")
                                checkbox_name_container.style.cssText="display: flex; flex-direction: column"
                                product_list.forEach(item=>{
                                    let row_item = document.createElement("DIV")
                                    row_item.style.cssText = "display: grid;  display: inline-grid;  grid-template-columns:70% 30%; height: 3rem; align-content: center; padding: 0 12rem;"
                                    let check_box = document.createElement("DIV")
                                    check_box.style.cssText ="display: flex; justify-self: flex-start;  gap: 1rem;"
                                    let input_check = document.createElement("INPUT")
                                    input_check.setAttribute('type', 'checkbox');
                                    input_check.checked = true
                                    check_box.appendChild(input_check)
                                    let item_name = document.createElement("div")
                                    item_name.innerHTML = item.item
                                    check_box.appendChild(item_name)
                                    row_item.appendChild(check_box)

                                    let price_container = document.createElement("DIV")
                                    price_container.style.cssText = "display: grid;gap: 1rem;grid-template-columns: 1fr 1fr;width: 300px;"
                                    let price_real = document.createElement("DIV")
                                    price_real.style.cssText = "color: red"
                                    price_real.innerHTML = item.item_price+currency
                                    price_container.appendChild(price_real)

                                     let price_compare = document.createElement("DIV")
                                    price_compare.style.cssText = "color: #444444; text-decoration: line-through"
                                    if(item.item_compare === null){
                                        price_compare.innerHTML = ''
                                    }
                                    else{
                                        price_compare.innerHTML = item.item_compare+currency
                                    }

                                    price_container.appendChild(price_compare)

                                    row_item.appendChild(price_container)

                                    checkbox_name_container.appendChild(row_item)
                                })


                                 preview_container.appendChild(checkbox_name_container)

                                main.insertBefore(preview_container, main.children[0].nextSibling)

                            }

                        }
                    }
                }
            }
        };
        xmlhttp.send(JSON.stringify(param))












    }
)




