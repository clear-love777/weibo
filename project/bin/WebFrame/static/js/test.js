//var height=prompt("请输入您的身高(m)");
//var weight=prompt("请输入您的体重(kg)");
//var bmi=weight/height**2;
//bmi=bmi.toFixed(2);
//console.log(bmi)
//bmi>=23.9?alert("该减肥了"):alert("nmsl")
function run_year(year){
//var year=prompt("请输入年份:");
if(year%4==0 && year%100!=0 || year%400==0){
return true;
}else{
return false;
}
}
function month_days(){
var year=prompt("请输入年份:");
var month_dict={"1":"31","3":"31","4":"30","5":"31","6":"30","7":"31","8":"31","9":"30","10":"31","11":"30","12":"31"};
if (run_year(year)){
    month_dict["2"]=29;
}
else{
    month_dict["2"]=28;
}
return month_dict
}
function days(dict){
    var month=prompt("请输入月份");
    var day=parseInt(prompt("请输入日期"))
    var days=0;
    for(i in dict){
        if(parseInt(i)<month){
            day+=parseInt(dict[i])
            }
    }
    days+=day
    console.log(days)
}
//days(month_days())

function mima(){
do{
    var pwd=prompt("请输入密码:");
    if(pwd=="123"){
        alert("正确");
        break
    }
}while(true)
}
//mima()
var a=1;
function fm(){
    var b=2;//局部的变量
    console.log(a)
}
//fm()
//var arr1=[];
//var arr2=[10,20,30,40];
//var arr3=new Array();
//var arr4=new Array(10,20,30,40);
//console.log(arr1);
//console.log(arr2);
//console.log(arr3);
//console.log(arr4);
//
//var arr5=new Array(10);
//console.log(arr5)
//var arr=[1,2,3,4,5];
//for(var i=arr.length-1;i>=0;i--){
//    console.log(arr[i])
//}
//var arr=[1,2,3,4];
//var s=arr.toString();
//console.log(s);
//var s2=arr.join("-");
//console.log(s2)
//function sortAsc(a,b){
//    return a-b;
//}
//var res=window.confirm("是否确定")
//console.log(res)
//var timer=setInterval(function(){alert("haha")},1000);
var timer=null;
function startinterval(){
    var timer=setInterval(function(){
    console.log("nmsl")},3000)
}
function stoptinterval(){
    clearInterval(timer);
}
//var timer01=setTimeout(function(){
//alert("nmsl")
//},3000)
//var h1=document.getElementsByTagName("h1")[0];
//console.log(h1);

//var elems=document.getElementsByClassName("category");
//console.log(elems)
//var hobbys=document.getElementsByName("hobby");
//var bt1=document.getElementsByName("bt1")[0];
//var div1=document.getElementById("show");
//var t1=document.getElementsByName("usertext")[0];
//console.log(bt1);
//console.log(t1);
//console.log(div1);
//bt1.onclick=function(){
////    div1.innerText=t1.value;
//    div1.innerHTML="<b>"+t1.value+"<b>";
//}
var bt1=document.getElementById("bt1")
var t1=document.getElementsByName("uname")[0]
var div1=document.getElementById("show")
console.log(bt1);
console.log(t1);
console.log(div1);
bt1.onclick=function(){
    if (t1.value.length>18 || t1.value.length<6){
        div1.innerHTML="非法";
        div1.setAttribute("class","green");
    }else{
        div1.innerHTML="用户名合法";
        div1.setAttribute("class","red");
    }
}
var div=document.createElement("div");
div.id="content";
div.innerText="动态创建的div";
document.body.appendChild(div);

var h1=document.createElement("h1");
h1.innerText="text";
document.body.insertBefore(h1,div);

//document.body.removeChild(h1);
h1.parentNode.removeChild(h1);
var table=document.createElement("table");
var tr=document.createElement("tr");
var th=document.createElement("th");
table.setAttribute("style","border:1px solid;")
document.body.appendChild(table)
table.appendChild(tr)
tr.appendChild(th)

var json=[
{"ename":"a","salary":15000}
]