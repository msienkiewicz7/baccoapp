$(document).ready(function() {

  console.log("jQuery magic starting...")

// Update price on changed selection
//   $("#id_ingredients").on("change", function(event){
//
//     var price = 0;
//     var all_selected_ingredient_ids = "";
//     var selection = $(this).find(":selected");
//     selection.each(function(){
//       price += Number($(this).attr("price"));
//
//       if (all_selected_ingredient_ids != ""){
//         all_selected_ingredient_ids += ",";
//       }
//       all_selected_ingredient_ids += $(this).attr("value");
//     });
//     // console.log(price);
//     // alert(all_selected_ingredient_ids);
//
//     $("#id_price").attr("value", price);
//     $("#id_all_selected_ingredient_ids").attr("value", all_selected_ingredient_ids);
//   });
  $("#id_price").attr("readonly", true)

// // Allow multiple selection without holding cmd
//   $('#id_ingredients option').mousedown(function(e) {
//       e.preventDefault();
//       $(this).prop('selected', !$(this).prop('selected'));
//       return false;
//   });


// Load preview images on chenged selection
  // $("#id_ingredients").on("change", function(event){
  //   console.log("Change event!");
  //
  //   $(".preview img").remove();
  //
  //   var selection = $(this).find(":selected");
  //   console.log(selection);
  //   selection.each(function(){
  //     let img_src = $(this).attr("img");
  //     let img = $("<img></img>").attr("src", img_src);
  //     $(".preview").append(img);
  //
  //   });
  //
  //
  // });


  $("#id_ingredients").mousedown(function(e){
    // console.log("Mouse down event!");
      e.preventDefault();
// Allow miltiple selections without holding extra key
      var select = this;
      var scroll = select .scrollTop;

      e.target.selected = !e.target.selected;

      setTimeout(function(){select.scrollTop = scroll;}, 0);

      $(select ).focus();

// Dynamicly change the price
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
      price = price.toFixed(2);
      $("#id_price").attr("value", price);
      $("#id_all_selected_ingredient_ids").attr("value", all_selected_ingredient_ids);

// Load preview images
      $(".preview img").remove();
      // var selection = $(this).find(":selected");

      let containsBread = false;
      let bottom_bread_src;
      let img;
      selection.each(function(){
        let ingr_type = $(this).attr("type");
        if (ingr_type == "BREAD") {
          containsBread = true;
          let top_bread_src = $(this).attr("img_small");
          bottom_bread_src = $(this).attr("img_large");
          img = $("<img></img>").attr("src", top_bread_src);
          $(".sandwich_images").prepend(img);
        } else {
          let img_src = $(this).attr("img_large");
          img = $("<img></img>").attr("src", img_src);
          $(".sandwich_images").append(img);
        }
      });

      if (containsBread) {
        img = $("<img></img>").attr("src", bottom_bread_src);
        $(".sandwich_images").append(img);
      }
  });

  $("#reset").click(function(){
    // $("option:selected").prop("selected", false)

    $("#id_ingredients option:selected").prop("selected", false)
  });





});
