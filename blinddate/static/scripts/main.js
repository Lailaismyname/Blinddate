document.addEventListener("DOMContentLoaded", main)

async function main(){
    // om te checken of js het doet
    console.log("the page is loaded")
    
    // handle menu button 
    const menu_btn = document.querySelector("#menu-btn");
    menu_btn.addEventListener("click", show_menu);

    // find love page functionality:
    //Fetch the profiles
    const profiles = await fetch_profiles()
    // show a profile on the page, when the page is loaded
    make_profile(profiles);
    //onload load 1 profile

    //on click load next profile, and save yes or no in db
    const no_btn = document.querySelector("#no-btn");
    const yes_btn = document.querySelector("#yes-btn");
    no_btn.addEventListener("click", async e=>{
        console.log("The Profilesssss: ", profiles)
    })
    yes_btn.addEventListener("click", async e=>{
        console.log("The Profilesssss: ", profiles)
    })    
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

async function fetch_profiles() {
    console.log("Getting the profiles");
    try {
        const response = await fetch('/fetch_profiles');
        const data = await response.json();
        return data;
    } catch (err) {
        console.error("fetch_profiles function produced the following error: ", err);
    }
}

function make_profile(profiles){
    //get element and remove it from list
    const profile = profiles.shift()
    // get fields that need to be filled with data:
    const username_field = document.querySelector("#fl_username");
    username_field.textContent = profile.profile_owner__username; // username not working
    const city_field  = document.querySelector("#fl_city");
    city_field.textContent = profile.city;
    const country_field  = document.querySelector("#fl_country");
    country_field.textContent = profile.country;
    const age_field  = document.querySelector("#fl_age");
    age_field.textContent = profile.age;
    const about_me_field  = document.querySelector("#fl_about_me");
    about_me_field.textContent = profile.about_me;
    const interests_field = document.querySelector("#fl_interests");
    interests_field.textContent = profile.interests;
    const hobbys_field = document.querySelector("#fl_hobbys");
    hobbys_field.textContent = profile.interests;
    //remove profile from list, as it has been seen. then return new list 
    console.log(profiles)
    return profiles
}

/*TODO in the make profile funkytown:
    - make sure profile is not the same profile as the user
    - make sure the profile hasnt already been seen and swiped on
    - also make sure user is the right gender, and looking for gender
*/