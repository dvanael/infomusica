$(function(){
    var loadForm = function(){
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $("#modal-evento").modal("show");
            },
            success: function(data){
                $("#modal-evento .modal-content").html(data.html_form);
            }
        });
    };
    var saveForm = function(){
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function(data){
                if(data.form_is_valid){
                    $("#table-evento tbody").html(data.html_list);
                    $("#modal-evento").modal("hide");
                }
                else{
                    $("#modal-evento .modal-content").html(data.html_form)
                }
            }
        });
        return false
    };
   
    // CREATE
    $(".js-create").click(loadForm);
    $("#modal-evento").on("submit", ".js-create-form", saveForm);

    // UPDATE
    $("#table-evento").on("click", ".js-update", loadForm);
    $("#modal-evento").on("submit", ".js-update-form", saveForm);

    // DELETE
	$("#table-evento").on("click", ".js-delete", loadForm);
	$("#modal-evento").on("submit", ".js-delete-form", saveForm);
});
