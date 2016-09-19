/**
 * Created by Chris on 2015/1/4.
 */
function downloadconfirm() {
    var r = confirm("确认?");

    if (r == true) {
        alert("You pressed OK!");
    }
    else {
        alert("You pressed Cancel!");
    }
}

function delconfirm() {
    if (!confirm("确认要删除？")) {
        window.event.returnValue = false;
    }
}

function deldraftconfirm() {
    if (!confirm("确认要清除草稿？")) {
        window.event.returnValue = false;
    }
}

function selectconfirm() {
    if (!confirm("确认选择此项？")) {
        window.event.returnValue = false;
    }
}

function dropconfirm() {
    if (!confirm("确认丢弃此数据？")) {
        window.event.returnValue = false;
    }
}