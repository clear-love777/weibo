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

do{
    var pwd=prompt("请输入密码:");
    if(pwd=="123"){
        alert("正确");
        break
    }
}while(true)
//console.log(sum)
