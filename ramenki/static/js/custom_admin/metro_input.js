$(function () {
    let name_input = document.getElementById("id_city"),
    manual_input_field = document.getElementsByClassName("field-custom_metro_station")[0],
    auto_input_field = document.getElementsByClassName("field-moscow_metro_station")[0];

    name_input.addEventListener("input", metro_change)

    function metro_change () {
        if (name_input.value){
            let value = name_input.options[name_input.value].text;
            if (value === "Москва"){
                auto_input_field.style.display = "block";
                manual_input_field.style.display = "none";
            }
        }
        else{
            auto_input_field.style.display = "none";
            manual_input_field.style.display = "block";
        }
    }
    metro_change();

})