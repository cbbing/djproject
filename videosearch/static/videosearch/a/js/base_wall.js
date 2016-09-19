/**
 * Created by Chris on 2014/12/30.
 */
$(document).ready(function () {
    $("#overlay").css("display", "none");
    $("#prompt").css("display", "none");
    $("#api_manage").click(function () {
        $("#overlay").css("display", "block");
        $("#prompt").css("display", "block");
        $("#overlay").width($(document).width());
        $("#overlay").height($(document).height());
        location.href = "/aums/";
    });
});
