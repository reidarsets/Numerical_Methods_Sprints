function check() {
    let quantity = Number(document.getElementById("select_matrix").value)
    let matrix = new Array(quantity)
    if(document.getElementById("result_table").innerHTML == "Невозможно найти корни") {
        document.getElementById("check_results").innerHTML = "Невозможно найти корни"
        return
    }
    for(let i = 0; i < quantity; i++) {
        matrix[i] = new Array(quantity)
        for(let j = 0; j < quantity; j++) {
            matrix[i][j] = Number(document.querySelectorAll(".undefined")[i*quantity+j].value)
            if(!document.querySelectorAll(".undefined")[i*quantity+j].value) {
                matrix[i][j] = 0
            }
        }
    }
    let temp = 0
    let check_results = document.getElementById("check_results")
    check_results.innerHTML = ""
    for(let i = 0; i < matrix.length; i++) {
        for(let j = 0; j < matrix.length; j++) {
            check_results.innerHTML += matrix[i][j] + " * " + answers_global[j] + " "
            if(j != matrix.length-1) {
                check_results.innerHTML += "+ "
            }
            temp += matrix[i][j] * answers_global[j]
        }
        check_results.innerHTML += "= " + temp
        check_results.append(document.createElement("br"))
        temp = 0
    }
}