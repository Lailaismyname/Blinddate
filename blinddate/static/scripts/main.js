document.addEventListener("DOMContentLoaded", main)

async function main(){
    // om te checken of js het doet
    console.log("the page is loaded")

    //Fetch the profiles
    const profiles = await fetch_profiles()

    //get user data 
    const logged_in_username = document.querySelector("#logged_in_username").value;
    const logged_in_id = document.querySelector("#logged_in_id").value;
    const user_data = get_user_data(profiles,logged_in_username,logged_in_id);
    
    // handle menu button 
    const menu_btn = document.querySelector("#menu-btn");
    menu_btn.addEventListener("click", show_menu);

    // find love page functionality:

    //Filter out the profiles that aren't compatible
    const match_profiles = remove_incompatible_profiles(user_data, profiles);

    // show a profile on the page, when the page is loaded
    make_profile(match_profiles);
    //onload load 1 profile

    //on click load next profile, and save yes or no in db
    const no_btn = document.querySelector("#no-btn");
    const yes_btn = document.querySelector("#yes-btn");
    no_btn.addEventListener("click", async e=>{
        make_profile(match_profiles);
    })
    yes_btn.addEventListener("click", async e=>{
        make_profile(match_profiles);
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
    try {
        const response = await fetch('/fetch_profiles');
        const data = await response.json();
        return data;
    } catch (err) {
        console.error("fetch_profiles function produced the following error: ", err);
    }
}

function get_user_data(profiles, username, id){
    const user_data = {};
    const profile = profiles.find(profile => profile.profile_owner__username === username);
    if (profile) {
        // get username
        const username = profile.profile_owner__username;
        user_data.username = username;
        // get gender
        const user_gender = profile.gender;
        user_data.gender = user_gender;
        // get preferences
        const looking_for = profile.looking_for_gender;
        user_data.looking_for = looking_for;
    } else {
        console.log("No user data found");
    }
    return user_data;
}

function remove_incompatible_profiles(user_data, profiles){
    let new_profiles = [];
    //if the profile is not from the user
    profiles.forEach(profile => {
        if(profile.profile_owner__username !== user_data.username){
            if(user_data.looking_for === "all"){
                new_profiles.push(profile);
            }
            else if(user_data.looking_for === "female" && profile.gender === "female"){
                new_profiles.push(profile);
            }
            else if(user_data.looking_for === "male" && profile.gender === "male"){
                new_profiles.push(profile);
            }
            else if(user_data.looking_for === "Non-Binary" && profile.gender === "Non-Binary"){
                        new_profiles.push(profile);
            }
        }
    });
    return new_profiles;
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
    hobbys_field.textContent = profile.hobbys;
    // remove profile from list, as it has been seen. then return new list 
    return profiles
}
/*TODO in the make profile funkytown:
    - make sure the profile hasnt already been seen and swiped on
    - testen of alle genders goed gefiltered worden
    - en een melding geven als alle profiles geswiped zijn. 
    -  als er ja geswiped word, updaten in database. Model ervoor maken
*/