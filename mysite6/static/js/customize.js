

//article_column.html
	function add_column(){
		var index = layer.open({
			type:1,
			skin:"layui-layer-rim",
			area: ["400px", "200px"],
			title: "新增栏目",
			content: '<div class="text-center" style="margin-top:20px">' +
            '<p>请输入新的栏目名称</p>' +
            '<p><input type="text" name="column" id="id_column" maxlength="200"></p></div>',
			btn:['确定', '取消'],
			yes: function(index, layero){
				column_name = $('#id_column').val();
				$.ajax({
					//url:'{% url "article:article_column" %}',
					url:'/article/article-column/',
					type:'POST',
					data:{"column":column_name},
					success:function(e){
						if(e=="1"){
							parent.location.reload();
							layer.msg("good");
						}else{
							layer.msg("此栏目已有，请更换名称")
						}
					},
				});
			},
			btn2: function(index, layero){
				layer.close(index);
			}
		});
    }



//imagecrop.html
$(window).load(function() {
	var options =
	{
		thumbBox: '.thumbBox',
		spinner: '.spinner',
		imgSrc: ''
	}
	var cropper = $('.imageBox').cropbox(options);
	var img="";
	$('#upload-file').on('change', function(){
		var reader = new FileReader();
		reader.onload = function(e) {
			options.imgSrc = e.target.result;
			cropper = $('.imageBox').cropbox(options);
			getImg();
		};
		reader.readAsDataURL(this.files[0]);
		this.files = [];
		//getImg();
	})
	$('#btnCrop').on('click', function(){
        //alert("图片上传喽");
        $.ajax({
		//url: '{% url "account:my_image" %}',
		url: '',  //???为什么不用加路径？？？？很重要
		type: 'POST',
		data: {"img": img},
		success: function(e){
            //location.href= "{% url 'account:my_information' %}"
            if(e == "1"){
				parent.location.reload();
			} else {
				alert("sorry, you are not lucky. the picutre can't been uploaded.")
			}
		},
	  });
	})
	function getImg(){
		img = cropper.getDataURL();
		$('.cropped').html('');
		$('.cropped').append('<img src="'+img+'" align="absmiddle" style="width:180px;margin-top:4px;border-radius:180px;box-shadow:0px 0px 12px #7E7E7E;"><p>180px*180px</p>');
		$('.cropped').append('<img src="'+img+'" align="absmiddle" style="width:128px;margin-top:4px;border-radius:128px;box-shadow:0px 0px 12px #7E7E7E;"><p>128px*128px</p>');
		$('.cropped').append('<img src="'+img+'" align="absmiddle" style="width:64px;margin-top:4px;border-radius:64px;box-shadow:0px 0px 12px #7E7E7E;" ><p>64px*64px</p>');
		}

	$(".imageBox").on("mouseup",function(){
 		getImg();
  		});

	$('#btnZoomIn').on('click', function(){
		cropper.zoomIn();
	})
	$('#btnZoomOut').on('click', function(){
		cropper.zoomOut();
	})
});




