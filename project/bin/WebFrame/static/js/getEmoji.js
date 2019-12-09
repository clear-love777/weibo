//var text = document.querySelector("#subText");
var we = new wantEmoji({
	wrapper : ".wrapper",
	callback : function(emojiCode){
	    var img_src=this.explain(emojiCode)
	    return img_src
	},
	autoInit : true
});
//console.log(we.callback("[wem:paopao_6_jpg:wem]"))
//console.log(we.explain(text.value))
//document.querySelector("#submit").onclick = function(e){
//	var val = text.value;
//	document.querySelector(".content").innerHTML = we.explain(val);
//};