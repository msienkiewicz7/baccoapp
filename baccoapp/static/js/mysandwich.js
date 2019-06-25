$(document).ready(function() {

  $("#ingredients_selector option").each(function() {

    let option = $(this)
    let data = option.attr("data").split(",")
    let ingredient_name = data[0]
    let ingredient_price = data[1]
    let ingredient_type = data[2]
    let img_small = data[3]
    let img_large = data[4]

    option.html(ingredient_name)
    option.attr("price", ingredient_price)
    option.attr("type", ingredient_type)
    // option.attr("img_small", img_small)
    // option.attr("img_large", img_large)

    // option.css("background-image", `url(${img_small})`)
    console.log(img_small);
  });

  $("#ingredients_selector").on("change", function(event) {

    let price = 0;
    let selection = $(this).find(":selected");
    selection.each(function(){
      price += Number($(this).attr("price"));
    });
    // console.log(price);

    $("#id_price").attr("value", price)

  });



  $("#id_pub_date").attr("hidden", true)
  $("#id_price").attr("readonly", true)

});
