let answers_global
function choose_method() {
    document.getElementById("result_table").innerHTML = ""
    document.getElementById("check_results").innerHTML = ""

    let quantity = Number(document.getElementById("select_matrix").value)
    let results = new Array(quantity)
    let matrix = new Array(quantity)
    let answers = new Array(quantity)
    for(let i = 0; i < quantity; i++) {
        matrix[i] = new Array(quantity)
        for(let j = 0; j < quantity; j++) {
            matrix[i][j] = Number(document.querySelectorAll(".undefined")[i*quantity+j].value)
            if(!document.querySelectorAll(".undefined")[i*quantity+j].value) {
                matrix[i][j] = 0
            }
        }
    }
    for(let i = 0; i < quantity; i++) {
        results[i] = Number(document.querySelectorAll(".result")[i].value)
        if(!document.querySelectorAll(".result")[i].value) {
            results[i] = 0
        }
    }
    switch(document.getElementById("select_method").value) {
        case 'Крамера': 
            answers = cramer_method(matrix, results)
            if(answers == 0) {
                answers = NaN
            }
            break
        case 'Гаусса':
            answers = gauss_method(matrix, results)
            if(answers == 0) {
                answers = NaN
            }
            break
        case 'Зейделя':
            answers = seidel_method(matrix, results)
            if(answers == 0) {
                answers = NaN
            }
            break
        case 'Гаусса-Жордана':
            answers = gauss_jordan_method(matrix, results)
            if(answers == 0) {
                answers = NaN
            }
            break
        case 'Якоби':
            answers = jacobi_method(matrix, results)
            if(answers == 0) {
                answers = NaN
            }
            break
        default :
            alert('Please select method')
            return
    }
    answers_global = new Array(quantity)
    for(let i = 0; i < quantity; i++) {
        answers_global[i] = answers[i]
    }
    document.getElementById("result_table").innerHTML = ""
    for(let i = 0; i < quantity; i++) {
        if(isNaN(answers[i])) {
            document.getElementById("result_table").innerHTML = "Невозможно найти корни"
            return
        }
        document.getElementById("result_table").innerHTML += "x" + (i+1) + "= " + answers[i]
        if(i+1 != quantity) {
            document.getElementById("result_table").innerHTML += "; "
        }
        document.getElementById("result_table").append(document.createElement("br"))
    }
}