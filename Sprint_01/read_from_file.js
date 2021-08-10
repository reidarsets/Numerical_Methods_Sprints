function readFile(object) {
    var file = object.files[0]
    var reader = new FileReader()
    let arr
    let quantity
    let matrix
    let results
    reader.onload = function() {
        arr = reader.result.split(" ")
        quantity = Number(arr[0])
        matrix = new Array(quantity)
        results = new Array(quantity)
        if(arr.length != (1+quantity*(quantity+1)) || quantity > 6) {
            alert("Неправильное содержимое файла")
            return
        }
        for(let i = 0; i < quantity; i++) {
            matrix[i] = new Array(quantity)
            for(let j = 0; j < quantity; j++) {
                matrix[i][j] = Number(arr[(j*quantity)+i+1])
            }
        }
        for(let i = 0; i < quantity; i++) {
            results[i] = arr[arr.length-quantity+i]
        }
        document.getElementById("select_matrix").value = quantity
        create_matrix()
        for(let i = 0; i < quantity; i++) {
            for(let j = 0; j < quantity+1; j++) {
                if(j == quantity) {
                    document.getElementsByClassName("matrix_node")[(i*(quantity+1))+j].value = results[i]
                }
                else {
                    document.getElementsByClassName("matrix_node")[(i*(quantity+1))+j].value = matrix[i][j]
                }
            }
        }
        document.getElementById("result_table").innerHTML = ""
        document.getElementById("check_results").innerHTML = ""
    }   
    reader.readAsText(file)
}