function solve_determinant_2(array) {
    return array[0][0] * array[1][1] - array[0][1] * array[1][0]
}
function solve_determinant_3(array) {
    return array[0][0] * solve_determinant_2([[array[1][1],array[1][2]],
                                            [array[2][1],array[2][2]]]) -
            array[0][1] * solve_determinant_2([[array[1][0],array[1][2]],
                                            [array[2][0],array[2][2]]]) +
            array[0][2] * solve_determinant_2([[array[1][0],array[1][1]],
                                            [array[2][0],array[2][1]]])
}
function solve_determinant_4(array) {
    return array[0][0] * solve_determinant_3([[array[1][1],array[1][2],array[1][3]],
                                            [array[2][1],array[2][2],array[2][3]],
                                            [array[3][1],array[3][2],array[3][3]]]) -
            array[0][1] * solve_determinant_3([[array[1][0],array[1][2],array[1][3]],
                                            [array[2][0],array[2][2],array[2][3]],
                                            [array[3][0],array[3][2],array[3][3]]]) +
            array[0][2] * solve_determinant_3([[array[1][0],array[1][1],array[1][3]],
                                            [array[2][0],array[2][1],array[2][3]],
                                            [array[3][0],array[3][1],array[3][3]]]) -
            array[0][3] * solve_determinant_3([[array[1][0],array[1][1],array[1][2]],
                                            [array[2][0],array[2][1],array[2][2]],
                                            [array[3][0],array[3][1],array[3][2]]])
}
function cramer_method(matrix, results) {
    let determinant = 0
    let quantity = matrix.length
    if(quantity > 4) {
        alert("Максимальный ранг матрицы для этого метода равен 4!")
        return 0
    }
    let matrix_temp = new Array(quantity) 
    let answers = new Array(quantity)
    for(let i = 0; i < quantity; i++) {
        matrix_temp[i] = new Array(quantity) 
        for(let j = 0; j < quantity; j++) {
            matrix_temp[i][j] = matrix[i][j]
        }
    }
    switch(quantity) {
        case 2:
            determinant = solve_determinant_2(matrix)
            if(determinant == 0) {
                alert("Определитель равен 0. Данная матрица вырожденная")
            }
            for(let i = 0; i < quantity; i++) {
                for(let i = 0; i < quantity; i++) {
                    for(let j = 0; j < quantity; j++) {
                        matrix_temp[i][j] = matrix[i][j]
                    }
                }
                for(let j = 0; j < quantity; j++) {
                    matrix_temp[j][i] = results[j]
                }
                answers[i] = solve_determinant_2(matrix_temp)/determinant
            }
            break
        case 3:
            determinant = solve_determinant_3(matrix)
            if(determinant == 0) {
                alert("Определитель равен 0. Данная матрица вырожденная")
            }
            for(let i = 0; i < quantity; i++) {
                for(let i = 0; i < quantity; i++) {
                    for(let j = 0; j < quantity; j++) {
                        matrix_temp[i][j] = matrix[i][j]
                    }
                }
                for(let j = 0; j < quantity; j++) {
                    matrix_temp[j][i] = results[j]
                }
                answers[i] = solve_determinant_3(matrix_temp)/determinant
            }
            break
        case 4:
            determinant = solve_determinant_4(matrix)
            if(determinant == 0) {
                alert("Определитель равен 0. Данная матрица вырожденная")
            }
            for(let i = 0; i < quantity; i++) {
                for(let i = 0; i < quantity; i++) {
                    for(let j = 0; j < quantity; j++) {
                        matrix_temp[i][j] = matrix[i][j]
                    }
                }
                for(let j = 0; j < quantity; j++) {
                    matrix_temp[j][i] = results[j]
                }
                answers[i] = solve_determinant_4(matrix_temp)/determinant
            }
            break
    }
    return answers
}