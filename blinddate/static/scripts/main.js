document.addEventListener("DOMContentLoaded", main)

function main(){
    // om te checken of js het doet
    console.log("the page is loaded")
    
    // handle menu button 
    menu_btn = document.querySelector("#menu-btn");
    menu_btn.addEventListener("click", show_menu);
}



function show_menu(){
    main_content = document.querySelector(".main-content");
    menu_canvas = document.querySelector(".menu-canvas")
    if(main_content.style.display !== "none"){
    // show menu and hide main content
    main_content.style.display = "none";
    menu_canvas.style.display = "block";
    }else{
    // show main content and hide menu
    main_content.style.display = "block";
    menu_canvas.style.display = "none";
    }
}