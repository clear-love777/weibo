//刷新or取消
//            document.getElementById('i77').onclick = function(){
//                location.reload();
//            }
//            document.getElementById('i222').onclick = function(){
//                location.reload();
//            }

            //用户名验证
            function checkname(){
                var div = document.getElementById("div1");
                div.innerHTML = "";
                var name1 = document.tijiao.text1.value;
                if (name1 == "") {
                div.innerHTML = "用户名不能为空！";
                <!--document.tijiao.text1.select();-->
                return false;
            }
                if (name1.length < 4 || name1.length > 16) {
                div.innerHTML = "长度4-16个字符";
                <!--document.tijiao.text1.select();-->
                return false;
            }
                var charname1 = name1.toLowerCase();
                console.log(charname1);
                for (var i = 0; i < name1.length; i++) {
                var charname = charname1.charAt(i);
                if (!(charname >= 0 && charname <= 9) && (!(charname >= 'a' && charname <= 'z' || isChinese(charname))) &&
                (charname !=
                '_')
                || (charname==" ")) {
                    div.innerHTML = "用户名包含非法字符";
                    <!--document.tijiao.text1.select();-->
                    return false;
                }
            }
                return true;
        }
//判断是否是中文
function isChinese(temp){
//    var re=/[^/u4e00-/u9fa5]/;
    var re=new RegExp("[\\u4E00-\\u9FFF]+");
    if (re.test(temp)) return true ;
    return false ;
}
            //密码验证
            function checkpassword(){
                var div = document.getElementById("div2");
                div.innerHTML = "";
                var password = document.tijiao.text2.value;
                if (password == "") {
                div.innerHTML = "密码不能为空";
                <!--document.tijiao.text2.focus();-->
                return false;
            }
                if (password.length < 4 || password.length > 16) {
                div.innerHTML = "密码长度为4-16位";
                <!--document.tijiao.text2.select();-->
                <!--document.tijiao.text2.focus();-->
                return false;
                }
                return true;
        }

            function checkrepassword(){
                var div = document.getElementById("div3");
                div.innerHTML = "";
                var password = document.tijiao.text2.value;
                var repass = document.tijiao.text3.value;
                if (repass == "") {
                div.innerHTML = "密码不能为空";
                <!--document.tijiao.text3.focus();-->
                return false;
            }
                if (password != repass) {
                div.innerHTML = "密码不一致";
                <!--document.tijiao.text3.select();-->
                return false;
            }
                return true;
        }
        //邮箱验证
        <!--function checkEmail(){-->
            <!--var div = document.getElementById("div4");-->
            <!--div.innerHTML = "";-->
            <!--var email = document.tijiao.text4.value;-->
            <!--var sw = email.indexOf("@", 0);-->
            <!--var sw1 = email.indexOf(".", 0);-->
            <!--var tt = sw1 - sw;-->
            <!--if (email.length == 0) {-->
            <!--div.innerHTML = "邮箱不能为空";-->
            <!--document.tijiao.text4.focus();-->
            <!--return false;-->
        <!--}-->

            <!--if (email.indexOf("@", 0) == -1) {-->
            <!--div.innerHTML = "必须包含@符号";-->
            <!--document.tijiao.text4.select();-->
            <!--return false;-->
        <!--}-->

            <!--if (email.indexOf(".", 0) == -1) {-->
            <!--div.innerHTML = "必须包含.符号";-->
            <!--document.tijiao.text4.select();-->
            <!--return false;-->
        <!--}-->

            <!--if (tt == 1) {-->
            <!--div.innerHTML = "@和.不能一起";-->
            <!--document.tijiao.text4.select();-->
            <!--return false;-->
        <!--}-->

            <!--if (sw > sw1) {-->
            <!--div.innerHTML  = "@符号必须在.之前";-->
            <!--document.tijiao.text4.select();-->
            <!--return false;-->
        <!--}-->
            <!--else {-->
            <!--return true;-->
            <!--}-->
        <!--return ture;-->
        <!--}-->

            function check(){
            var regis_submit=document.getElementById("i111").value;
            var exit=document.getElementById("i112").value;
            var submit=document.getElementById("myform").action;
            var localhostPaht=window.location.protocol + '//' + window.location.host;
            <!--alert(regis_submit);-->
            <!--alert(exit);-->
            <!--alert(submit);-->
            <!--alert(localhostPaht+"/regis_submit");-->
            if(submit!=localhostPaht+"/exit"){

                if (checkname() && checkpassword() && checkrepassword()) {
                return true;
                }
                else {
                return false;
                }
            }else{
                return true;
            }
        }

        function onclick_submit(){
            document.tijiao.action="/regis_submit";
        }
        function onclick_exit(){
            document.tijiao.action="/exit";
        }