$(document).ready(function() {

  $("#ingredients_selector option").each(function() {

    var option = $(this)
    var data = option.attr("data").split(",")
    var ingredient_name = data[0]
    var ingredient_price = data[1]
    var ingredient_type = data[2]
    option.html(ingredient_name)
    option.attr("price", ingredient_price)
    option.attr("type", ingredient_type)
    // console.log(option.attr("data"));
  });

  $("#ingredients_selector").on("change", function(event) {

    var price = 0;
    var selection = $(this).find(":selected");
    selection.each(function(){
      price += Number($(this).attr("price"));
    });
    // console.log(price);

    $("#id_price").attr("value", price)

  });

  $("#id_pub_date").attr("hidden", true)
  $("#id_price").attr("readonly", true)

});
