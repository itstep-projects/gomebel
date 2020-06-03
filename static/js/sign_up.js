"use strict";

$(document).ready(() => {
    let correct1 = false;
    let correct2 = false; // Думаю лучше correct2 и correct3 совместить в общую переменную
    let correct3 = false; // true только если оба условия верны (равнество и проверка на регулярку)
    let correct4 = false;

    let regExp1 = /^[a-zA-Z][a-zA-Z0-9_\-]{4,15}$/; // Регулярка логина
    let regExp2 = /^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[_\-\$#&])[A-Za-z0-9_\-\$#&]{8,}$/; // Регулярка пароля
    let regExp3 = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/; // Регулярка email

    $("#login").blur(() => {
        let loginX = $("#login").val();
        if (regExp1.test(loginX)) {
            // ! Проверка занятости логина:
            $.ajax({
                url: "/accounts/ajax_reg",
                data: "login=" + loginX,
                success: function (result) {
                    if (result.message == "занят") {
                        $("#login_mess").html("Логин занят!");
                        correct1 = false;
                    } else {
                        $("#login_mess").html("");
                        correct1 = true;
                    }
                }
            });
        } else {
            correct1 = false;
            $("#login_mess").html("Логин не соответствует шаблону безопасности");
        }
    });

    $("#pass1").blur(() => {
        let passX = $("#pass1").val();  // Дополнительная перепроверка в случае если пользователь вернулся
        let passY = $("#pass2").val();  // в первое поле пароля и изменил его
        if (regExp2.test(passX)) {
            $("#pass1_mess").html("");
            if (passY == passX) {
                correct2 = true;
                correct3 = true;
                $("#pass1_mess").html("");
                $("#pass2_mess").html("");
            } else {
                correct2 = false;
                if (passY == "") {
                    $("#pass2_mess").html("");
                } else {
                    $("#pass2_mess").html("Пароли не совпадают");
                }
            }
        } else {
            correct2 = false;
            $("#pass1_mess").html("Пароль не соответствует шаблону безопасности");
        }
    });

    $("#pass2").blur(() => {
        let passX = $("#pass1").val();
        let passY = $("#pass2").val();
        if (passY == passX && regExp2.test(passX)) {
            correct2 = true;    // Думаю лучше correct2 и correct3 совместить в общую переменную
            correct3 = true;    // (true только если оба условия верны)
            $("#pass2_mess").html("");
        } else {
            correct3 = false;
            $("#pass2_mess").html("Пароли не совпадают");
        }
    });

    $("#email").blur(() => {
        let emailX = $("#email").val();
        if (regExp3.test(emailX)) {
            correct4 = true;
            $("#email_mess").html("");
        } else {
            correct4 = false;
            $("#email_mess").html("Email не соответствует шаблону безопасности");
        }
    });

    $("#submit").click(() => {
        alert(correct1);
        alert(correct2);
        alert(correct3);
        alert(correct4);
        if (correct1 == true && correct2 == true && correct3 == true && correct4 == true) {
            $("#form1").attr("onsubmit", "return true");
        } else {
            $("#form1").attr("onsubmit", "return false");
            alert("Форма содержит некорректные данный! \nОтправка данных заблокирована!");
        }
    });
 });

