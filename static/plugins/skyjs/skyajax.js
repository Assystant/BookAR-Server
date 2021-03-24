$(document).ready(function () {
    /*
     * SKY-FROM 
     */
    $(".sky-form").submit(function (e) {
        e.preventDefault();
        var url = $(this).attr("action");
        var formval = $(this)[0];
        var form = $(this);
        var data = new FormData(formval);
        $.when(callme(url, data)).then(
            function successHandler(result) {
                if (result.status) {
                    $(form)[0].reset();
                    message(result);
                } else {
                    message(result, 1);
                }
            },
            function errorHandler() {
                message({
                    message: "Something Went Wrong!!"
                }, 1);
            }
        );
    });
    /*
     * SKY-FROM REFRESH
     */
    $(".sky-form-refresh").submit(function (e) {
        e.preventDefault();
        var url = $(this).attr("action");
        var formval = $(this)[0];
        var form = $(this);
        var data = new FormData(formval);
        $.when(callme(url, data)).then(
            function successHandler(result) {
                if (result.status) {
                    message(result);
                    setTimeout(function (){
                        location.reload();
                    }, 1500);
                } else {
                    message(result, 1);
                }
            },
            function errorHandler() {
                message({
                    message: "Something Went Wrong!!"
                }, 1);
            }
        );
    });
    /*
     * SKY-FROM APPEND DATA
     */
    $(".sky-form-return").submit(function (e) {
        e.preventDefault();
        var url = $(this).attr("action");
        var div = $(this).attr("divid");
        var countid = $(this).attr("countid");
        console.log(countid);
        if (countid) {
            count_val = $('#' + countid).text();
            count_val = parseInt(count_val);
            count_val++;
        }
        var formval = $(this)[0];
        var form = $(this);
        var data = new FormData(formval);
        $.when(callme(url, data)).then(
            function successHandler(result) {
                console.log(result);
                if (result.status) {
                    $(form)[0].reset();
                    $('#' + div).prepend(result.content);
                    if (countid)
                        $('#' + countid).text(count_val);
                    message(result);
                } else {
                    message(result, 1);
                }
            },
            function errorHandler() {
                message({
                    message: "Something Went Wrong!!"
                }, 1);
            }
        );
    });
    /*
     * SKY FORM NOT RESET
     */
    $(".sky-form-nr").submit(function (e) {
        e.preventDefault();
        var url = $(this).attr("action");
        var formval = $(this)[0];
        var form = $(this);
        var data = new FormData(formval);
        $.when(callme(url, data)).then(
            function successHandler(result) {
                if (result.status) {
                    message(result);
                } else {
                    message(result, 1);
                }
            },
            function errorHandler() {
                message({
                    message: "Something Went Wrong!!"
                }, 1);
            }
        );
    });
    /*
     * DELETE TABLE ROW
     */
    $(".sky-rowdel").click(function (e) {
        e.preventDefault();
        if (confirm("Are you sure want to delete this???")) {
            var url = $(this).attr("href");
            var hid = $(this).attr("hid");
            var row = $(this);
            $.when(callmetest(url,'delete')).then(
                function successHandler(result) {
                    if (result.status) {
                        $(row).parent().parent().remove();
                        if (hid != undefined) {
                            $('#' + hid).hide();
                        }
                        message(result);
                    } else {
                        message(result, 1);
                    }
                },
                function errorHandler() {
                    message({
                        message: "Something Went Wrong!!"
                    }, 1);
                }
            );
        }
    });
    $(".sky-rowdel-nhide").click(function (e) {
        e.preventDefault();
        if (confirm("Are you sure want to delete this???")) {
            var url = $(this).attr("href");
            $.when(postcall(url)).then(
                function successHandler(result) {
                    if (result.status) {
                        message(result);
                    } else {
                        message(result, 1);
                    }
                },
                function errorHandler() {
                    message({
                        message: "Something Went Wrong!!"
                    }, 1);
                }
            );
        }
    });

    /**
     * 
     * TOGGLE CHANGE SEND DATA BY POST
     */
    $('.toggle_btn').change(function (e) {
        var name = $(this).attr('name');
        var url = $(this).attr('url');
        if ($(this).prop('checked'))
            status = 1;
        else status = 0;
        var formData = new FormData();
        formData.set('name', name);
        formData.set('status', status);
        if (confirm("Are you sure want to change ???"))
            whenthen_noform(url, formData);
        else {
            if (status == 1)
                $(this).prop('checked', false)
            else $(this).prop('checked', true)
        }
    });
    $('.toggle_btn_url').change(function (e) {
        var url = $(this).attr('url');
        if (confirm("Are you sure want to change ???"))
            postcall(url);
        else {
            if (status == 1)
                $(this).prop('checked', false)
            else $(this).prop('checked', true)
        }
    });
    /**
     * 
     * ON CHANGE SEND DATA BY POST
     */
    $('.toggle_input').change(function (e) {
        var name = $(this).attr('name');
        var input_value = $(this).val();
        var url = $(this).attr('url');
        var formData = new FormData();
        formData.set('name', name);
        formData.set('value', input_value);
        if (confirm("Are you sure want to change ???"))
            whenthen_noform(url, formData);
        else {
            return true;
        }
    });
    /*
        - For deleting data using post
    */
    function postcall(url) {
        return $.ajax({
            url: url,
        });
    }
    /*
       - AJAX CALL
    */
    function callme(url, data) {
        return $.ajax({
            url: url,
            method: "post",
            data: data,
            dataType: "json",
            processData: false,
            contentType: false,
            cache: false,
            timeout: 20000,
        });
    }
    /*
       - AJAX CALL TEST
    */
    function callmetest(url,method) {
        return $.ajax({
            url: url,
            method: method,
            dataType: "json",
            processData: false,
            contentType: false,
            cache: false,
            timeout: 20000,
        });
    }
    /**
     * 
     * WHEN THEN NO FORM INPUT
     */
    function whenthen_noform(url, formData) {
        $.when(callme(url, formData)).then(
            function successHandler(result) {
                if (result.status) {
                    message(result);
                } else {
                    message(result, 1);
                }
            },
            function errorHandler() {
                message({
                    message: "Something Went Wrong!!"
                }, 1);
            }
        );
    }
    /*
        - Success or failure message
     */
    function message(result, type = 0) {
        var color = "#e77324;";
        if (type == 0) {
            color = "#29ca8e";
        }
        $.toast({
            text: result.message,
            bgColor: color,
            position: "top-right",
        });
    }
});