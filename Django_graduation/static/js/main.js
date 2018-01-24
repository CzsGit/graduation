$(function(){
	$(".panel").css({"height":$(window).height()});
	$.scrollify({
		section:".panel"
	});
	$(".scroll").click(function(e) {
		e.preventDefault();
		$.scrollify("move",$(this).attr("href"));
	});




	var now=0;
	function next(){
		now++;
        $("ol>li").removeClass("active");
        tab();

	}
	function tab(){
		var w=$(".lunbo>ul>li").width();
		if(now==4){
			$(".lunbo>ul").animate({
				"left":-4*w+"px"
			},1000,function(){
				$(".lunbo>ul").css("left",0);
				now=0;
				$("ol>li").eq(now).addClass("active");
			})
		}else{
			$(".lunbo>ul").animate({
				"left":-now*w+"px"
			},1000);
			$("ol>li").eq(now).addClass("active");
		}
	}
	var timer=setInterval(next,3000);
	$("ol>li").mouseover(function(){
		var index=$(this).index();
		 $("ol>li").removeClass("active");
		 now=index;
		 tab();
		$("ol>li").eq(index).addClass("active");
		clearInterval(timer);
	})
	$("ol>li").mouseout(function(){
		timer=setInterval(next,3000);
	})


})