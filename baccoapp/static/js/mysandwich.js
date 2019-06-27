$(document).ready(function() {

  console.log("jQuery magic starting...")

  // $("#id_ingredients option").each(function() {
  //
  //   let option = $(this)
  //   let data = option.attr("data").split(",")
  //   let ingredient_name = data[0]
  //   let ingredient_price = data[1]
  //   let ingredient_type = data[2]
  //   let img_small = data[3]
  //   let img_large = data[4]
  //
  //   option.html(ingredient_name)
  //   option.attr("price", ingredient_price)
  //   option.attr("type", ingredient_type)
  //   option.attr("img_small", img_small)
  //   option.attr("img_large", img_large)
  //
  //   option.css("background-image", `url(/${img_small})`)
  //   // option.css("background-size", "5%")
  //   // console.log(img_small);
  // });

  // $("#id_ingredients").on("change", function(event) {
  //
  //   let price = 0;
  //   let selection = $(this).find(":selected");
  //   selection.each(function(){
  //     price += Number($(this).attr("price"));
  //   });
  //   console.log(price);
  //
  //   $("#id_price").attr("value", price)
  //
  // });

  $("#id_ingredients").on("change", function(event){

    var price = 0;
    var all_selected_ingredient_ids = "";
    var selection = $(this).find(":selected");
    selection.each(function(){
      price += Number($(this).attr("price"));

      if (all_selected_ingredient_ids != ""){
        all_selected_ingredient_ids += ",";
      }
      all_selected_ingredient_ids += $(this).attr("value");
    });
    // console.log(price);
    // alert(all_selected_ingredient_ids);

    $("#id_price").attr("value", price);
    $("#id_all_selected_ingredient_ids").attr("value", all_selected_ingredient_ids);

  });



  // $("#id_pub_date").attr("hidden", true)
  $("#id_price").attr("readonly", true)

});
