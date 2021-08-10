function create_matrix() {
    let matrix = document.getElementsByClassName("matrix")[0]
    let dimension = document.getElementById("select_matrix").value
    document.querySelectorAll(".matrix_node").forEach(element => {//удаление прошлых "нод"
        element.remove()
    })
    if(document.querySelector(".matrix > br")) {//удаление прошлых br если они есть
        document.querySelectorAll(".matrix > br").forEach(element => {
            element.remove()
        })
    }
    if(document.querySelector(".matrix > span")) {//удаление прошлых span если они есть
        document.querySelectorAll(".matrix > span").forEach(element => {
            element.remove()
        })
    }
    for(let i = 0; i < dimension; i++) {// создание новых
        for(let j = 0; j <= dimension; j++) {
            let input = document.createElement("input")
            let span = document.createElement("span")
            span.innerHTML = "x"+(j+1)
            if(j == dimension) {
                span.innerHTML = "= "
                matrix.append(span)
            }
            input.setAttribute("type", "text")
            if(j == dimension) {
                input.classList.add("result")
            }
            if(j != dimension) {
                input.classList.add("undefined")
            }
            input.classList.add("matrix_node")
            matrix.append(input)
            if(j != dimension) {
                matrix.append(span)
            }
        }
        matrix.append(document.createElement("br"))
    }
}