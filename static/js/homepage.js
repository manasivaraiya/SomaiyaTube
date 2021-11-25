if(typeof jQuery!=='undefined'){
    console.log('jQuery Loaded');
}
else{
    console.log('not loaded yet');
}

document.getElementById("sidebar-row").onclick = function() {  
    console.log("In javascript");
    $(this).addClass("selected").siblings().removeClass("selected");
};  