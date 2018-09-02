var specs = []
var specs_sum = []
var colors = []
var specs_sorted_sum = []

function compressArray(original) {

    var values = [];
    var counts = [];
    // make a copy of the input array
    var copy = original.slice(0);

    // first loop goes over every element
    for (var i = 0; i < original.length; i++) {

        var myCount = 0;
        // loop over every element in the copy and see if it's the same
        for (var w = 0; w < copy.length; w++) {
            if (original[i] == copy[w]) {
                // increase amount of times duplicate is found
                myCount++;
                // sets item to undefined
                delete copy[w];
            }
        }

        if (myCount > 0) {
            values.push(original[i]);
            counts.push(myCount);
        }
    }

    return [values, counts];
};

function compressSortedArrays(original) {

    var values = [];
    var counts = [];
    var arrays = [];
    // make a copy of the input array
    var copy = original.slice(0);

    // first loop goes over every element
    for (var i = 0; i < original.length; i++) {

        var myCount = 0;
        // loop over every element in the copy and see if it's the same
        for (var w = 0; w < copy.length; w++) {
            if (original[i] == copy[w]) {
                // increase amount of times duplicate is found
                myCount++;
                // sets item to undefined
                delete copy[w];
            }
        }

        if (myCount > 0) {
            arrays.push([original[i], myCount])
        }
    }

    arrays.sort(function (a, b) {
        return a[1] - b[1];
    })

    for (var i = 0; i < arrays.length; i++) {
        values.push(arrays[i][0]);
        counts.push(arrays[i][1]);
    }

    return [values.reverse(), counts.reverse()];
};

$(document).ready(function () {
    $('#load_data').click(function () {
        $.ajax({
            url: "2300.csv",
            dataType: "text",
            success: function (data) {
                var employee_data = data.split(/\r?\n|\r/);
                var table_data = '<table class="table table-bordered table-striped">';
                for (var count = 0; count < employee_data.length; count++) {
                    var cell_data = employee_data[count].split(",");
                    table_data += '<tr>';
                    for (var cell_count = 0; cell_count < cell_data.length; cell_count++) {
                        if (count === 0) {
                            table_data += '<th>' + cell_data[cell_count] + '</th>';
                        } else {
                            table_data += '<td>' + cell_data[cell_count] + '</td>';
                        }
                    }
                    table_data += '</tr>';
                }
                table_data += '</table>';
                $('#employee_table').html(table_data);
                console.log("1st button done")
            }
        });
    });

    $('#col_array').click(function () {
        console.log("Clicked 2nd button");
        specs = $('#employee_table td:nth-child(10)')
            .map(function () {
                return $(this).text();
            })
            .get();
        specs_sum = compressArray(specs)
        specs_sorted_sum = compressSortedArrays(specs)
        drawChart();
    });
});

    function dynamicColor(num, vis) {
        var lowVis = []
        var highVis = []
        for (var i = 0; i < num; i++) {
            var r = Math.floor(Math.random() * 255);
            var g = Math.floor(Math.random() * 255);
            var b = Math.floor(Math.random() * 255);
            lowColor = 'rgba(' + r + ', ' + g + ', ' + b + ', ' + vis + ')';
            lowVis.push(lowColor);
            highColor = 'rgba(' + r + ', ' + g + ', ' + b + ', 1)';
            highVis.push(highColor);
        }

        return [lowVis, highVis];
    };

    function drawChart() {
        colors = dynamicColor(20, 0.35);
        var ctx = document
            .getElementById("myChart")
            .getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                defaultFontStyle: 'bold',
                labels: specs_sorted_sum[0],
                datasets: [
                    {
                        defaultFontStyle: 'bold',
                        label: '# of characters',
                        data: specs_sorted_sum[1],
                        backgroundColor: colors[0],
                        borderColor: colors[1],
                        borderWidth: 1
                    }
                ]
            },
            options: {
                responsive: false,
                maintainAspectRatio: false,
                defaultFontStyle: 'bold',
                scales: {
                    yAxes: [
                        {
                            ticks: {
                                beginAtZero: true
                            }
                        }
                    ]
                }
            }
        });
    }