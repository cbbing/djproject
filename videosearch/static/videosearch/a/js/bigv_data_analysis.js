$(function () {
    $("input[name='btn_status']").click(function () {
        alert("btn_status1");
        //var btn_status = $(this).attr("value");
        //alert("btn_status" + btn_status);
        //var disabledv = $(this).parents("tr").find("[name='textarea_model']").attr("disabled");
        //var textarea_model = $(this).parents("tr").find("[name='textarea_model']");
        //var btn_model = $(this);
        //var status_value = $(this).parents("tr").find("[name='status']");
        //
        //if (disabledv == true) {
        //    textarea_model.attr("disabled", false);
        //    textarea_model.attr("style", "background: white");
        //    btn_model.attr("value", "保存");
        //} else {
        //
        //    var oidv = $(this).parents("tr").find("[name='oid']").text();
        //    var manual_summaryv = $(this).parents("tr").find("[name='textarea_model']").val();
        //
        //
        //    if (manual_summaryv.trim().length && manual_summaryv.trim() == "None") {
        //        manual_summaryv = "";
        //    }
        //
        //    $.post("/article_shixi/manual_summary",
        //        {
        //            oid: oidv,
        //            manual_summary: manual_summaryv
        //        },
        //        function (data, status) {
        //            //alert("数据：" + data + "\n状态：" + status);
        //            if (status == "success") {
        //                textarea_model.attr("disabled", true);
        //                textarea_model.attr("style", "background: darkgray");
        //                btn_model.attr("value", "编辑");
        //                status_value.text("1");
        //                alert("更新成功！");
        //            } else {
        //                alert("更新失败，请重试！");
        //            }
        //        });
        //}
    });
});