let search_term = document.getElementById("search_term");
let submit_button = document.getElementById("submit_button");
let modal_ = document.getElementById("dob-verification")
let tableCard = $("#search-result-table");
tableCard.hide()

function render(res) {
    let table_ = document.getElementById("table");
    let selected_student = ''
    let row =
        "<tr><td>Name</td><td>Class</td><td>Section</td><td>Roll No.</td><td>Action</td></tr>";

    function test(index) {
        selected_student = index
        console.log(selected_student)
    }

    res["results"].forEach((result, index) => {
        // console.log(result);

        row += "<tr>";
        row += "<td>" + result.first_name + "  " + result.last_name + "</td>";
        row += "<td>" + result.stu_class + "</td>";
        row += "<td>" + result.stu_section + "</td>";
        row += "<td>" + 0 + "</td>";
        // test(index)
        row += "<td>" + '<button value="' + result.id + '" type="button" class="select-button btn btn-primary" data-toggle="modal" data-target="#dob-verification" >' +
            'select' + '</button>' + "</td>"
        // $( "input[name=id]" ).val( index )
        // row += "<td>" + '<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#dob-verification" onclick="selected_student=(' + index + ')" >' +
        //     'select' + '</button>' + "</td>"

        row += "</tr>";
    });
    // console.log(table_.innerHTML)
    table_.innerHTML = row;
    tableCard.show()

    $(".select-button").click(function () {
        let selected_value = $(this).val();
        $("input[name=id]").val(selected_value)
        console.log(selected_value);

    });
}

function search_func(term) {
    fetch("studentapi/?search=" + term)
        .then((res) => {
            return res.json();
        })
        .then((res) => {
            render(res);
        });
}

function sleep(milliseconds) {
    var start = new Date().getTime();
    for (var i = 0; i < 1e7; i++) {
        if (new Date().getTime() - start > milliseconds) {
            break;
        }
    }
}

submit_button.addEventListener("click", (event) => {
    event.preventDefault();
    console.log("clicked " + search_term.value);
    search_func(search_term.value);
});

search_term.addEventListener("keyup", (event) => {
    console.log("something new typed !!!");
    search_func(search_term.value);
    sleep(100);
});