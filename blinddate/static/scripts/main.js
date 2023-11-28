document.addEventListener("DOMContentLoaded", main)

async function main(){
    // om te checken of js het doet
    console.log("main js script loaded and working")    
    // handle menu button 
    const menu_btn = document.querySelector("#menu-btn");
    menu_btn.addEventListener("click", show_menu);

    //chat box
    chatbox = document.querySelector("#chat-box");
    exchanged_messages = chatbox.childElementCount;
    chat_picture = document.querySelector("#match-foto");
    chat_picture.style.opacity = 0.1;
    chat_picture.style.filter = `blur(50px)`;

    // switch case for chatbox
    switch (true) {
        case exchanged_messages <= 10:
            chat_picture.style.opacity = 0.2;
            chat_picture.style.filter = `blur(50px)`;
          break;
        case exchanged_messages <= 20:
            chat_picture.style.opacity = 0.4;
            chat_picture.style.filter = `blur(40px)`;
          break;
        case exchanged_messages <= 30:
            chat_picture.style.opacity = 0.6;
            chat_picture.style.filter = `blur(30px)`;
          break;
        case exchanged_messages <= 40:
            chat_picture.style.opacity = 0.8;
            chat_picture.style.filter = `blur(20px)`;
          break;
        case exchanged_messages <= 50:
            chat_picture.style.opacity = 1;
            chat_picture.style.filter = `blur(10px)`;
          break;
        case exchanged_messages <= 60:
            chat_picture.style.filter = `blur(0px)`;
          break;
        default:
            chat_picture.style.opacity = 0.2;
            chat_picture.style.filter = `blur(50px)`;
          break;
      }
    
}


function show_menu(){
    const main_content = document.querySelector(".main-content");
    const menu_canvas = document.querySelector(".menu-canvas")
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

