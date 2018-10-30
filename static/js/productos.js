$(function () {

  /* Funciones*/

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-product .modal-content").html("");
        $("#modal-product").modal("show");
      },
      success: function (data) {
        $("#modal-product .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#product-table tbody").html(data.html_product_list);
          $("#modal-product").modal("hide");
        }

        else {
          $("#modal-product .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create product
  $(".js-create-product").click(loadForm);
  $("#modal-product").on("submit", ".js-product-create-form", saveForm);

  // Update product
  $("#product-table").on("click", ".js-update-product", loadForm);
  $("#modal-product").on("submit", ".js-product-update-form", saveForm);

  // Delete product
  $("#product-table").on("click", ".js-delete-product", loadForm);
  $("#modal-product").on("submit", ".js-product-delete-form", saveForm);

});

$(function () {

  /* Funciones*/

  var loadForm1 = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-categoria .modal-content").html("");
        $("#modal-categoria").modal("show");
      },
      success: function (data) {
        $("#modal-categoria .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm1 = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#categoria-table tbody").html(data.html_categoria_list);
          $("#modal-categoria").modal("hide");
        }

        else {
          $("#modal-categoria .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create categoria
  $(".js-create-categoria").click(loadForm1);
  $("#modal-categoria").on("submit", ".js-categoria-create-form", saveForm1);

  // Update categoria
  $("#categoria-table").on("click", ".js-update-categoria", loadForm1);
  $("#modal-categoria").on("submit", ".js-categoria-update-form", saveForm1);

  // Delete categoria
  $("#categoria-table").on("click", ".js-delete-categoria", loadForm1);
  $("#modal-categoria").on("submit", ".js-categoria-delete-form", saveForm1);

  // Restore categoria
  $("#categoria-table").on("click", ".js-restore-categoria", loadForm1);
  $("#modal-categoria").on("submit", ".js-categoria-restore-form", saveForm1);

});

