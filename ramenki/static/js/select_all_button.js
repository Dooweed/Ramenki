$( document ).ready(function() {
    $("#photo_set-group fieldset.module h2")
        .css("display", "flex")
        .css("justify-content", "space-between")
        .html("<p style='margin: 0'>Изображения</p>" +
            "<div style='display: flex;'><input id='select_all' type='checkbox'>" +
            "<label style='color: #fff; text-transform: none; padding-left: 5px' for='select_all'>Выбрать все</label>" +
            "</div>")

    let $select_all = $("#select_all"),
    $delete_tags = $(".delete input");

    $delete_tags.on("change", function () {
        $select_all.prop("checked", check_values())
    })
    $select_all.on('change', function() {
        set_values($select_all.prop("checked"));
    });

    function check_values() {
        let value = true;
        $delete_tags.each(function (index) {
            value = value && $delete_tags.eq(index).prop("checked");
        })
        return value
    }

    function set_values(value) {
        $delete_tags.each(function (index) {
            $delete_tags.eq(index).prop("checked", value);
        })
    }
});