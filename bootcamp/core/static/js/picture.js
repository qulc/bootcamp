$(function () {

  var jcrop_api,
      xsize = 200,
      ysize = 200;
  
  $("#crop-picture").Jcrop({
    aspectRatio: xsize / ysize,
    onSelect: updateCoords,
    setSelect: [0, 0, 200, 200]
  });

  function updateCoords(c) {
    $("#x").val(c.x);
    $("#y").val(c.y);
    $("#width").val(c.w);
    $("#height").val(c.h);
  };

  $("#btn-upload-picture").click(function () {
    $("#picture-upload-form input[name='picture']").click();
  });

  $("#picture-upload-form input[name='picture']").change(function () {
    $("#picture-upload-form").submit();
  });

});
