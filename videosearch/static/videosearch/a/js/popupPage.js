/**
 * Created by Chris on 2014/12/31.
 */
function popupUserDetail(url, webname, iWidth, iHeight) {

    var url;                             //转向网页的地址;
    var webname;                            //网页名称，可为空;
    var iWidth;                          //弹出窗口的宽度;
    var iHeight;                         //弹出窗口的高度;
    //获得窗口的垂直位置
    var iTop = (window.screen.availHeight - 30 - iHeight) / 2;
    //获得窗口的水平位置
    var iLeft = (window.screen.availWidth - 10 - iWidth) / 2;
    window.open(url, webname, 'height=' + iHeight + ',,innerHeight=' + iHeight + ',width=' + iWidth + ',' +
        'innerWidth=' + iWidth + ',top=' + iTop + ',left=' + iLeft + ',' +
        'status=no,toolbar=no,menubar=no,location=no,resizable=no,scrollbars=yes,titlebar=no');
}

function popupPage(url, webname, iWidth, iHeight) {

    var url;                             //转向网页的地址;
    var webname;                            //网页名称，可为空;
    var iWidth;                          //弹出窗口的宽度;
    var iHeight;                         //弹出窗口的高度;
    //获得窗口的垂直位置
    var iTop = (window.screen.availHeight - 30 - iHeight) / 2;
    //获得窗口的水平位置
    var iLeft = (window.screen.availWidth - 10 - iWidth) / 2;
    window.open(url, webname, 'height=' + iHeight + ',,innerHeight=' + iHeight + ',width=' + iWidth + ',' +
        'innerWidth=' + iWidth + ',top=' + iTop + ',left=' + iLeft + ',' +
        'status=no,toolbar=no,menubar=no,location=no,resizable=no,scrollbars=yes,titlebar=no');
}

function popupAddressChoose() {
    window.open("http://www.baidu.com", "", "toolbar=no,height=600,width=880");
    return false;
}