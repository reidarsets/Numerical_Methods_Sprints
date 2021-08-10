function gauss_jordan_method(matrix, results) {
    let n = matrix.length
    let full_matrix = new Array(n)
    for(let i = 0; i < n; i++){
        full_matrix[i] = new Array(n+1)
        for(let j = 0; j < n+1; j++){
            if(j == n) {
                full_matrix[i][j] = results[i]
            }
            else {
                full_matrix[i][j] = matrix[i][j]
            }
        }
    }
    let x = new Array(n)
    let ratio = 0
    for(let i = 0; i < n; i++) {
        x[i] = 0
    }
    for(let i = 0; i < n; i++) {
        if(full_matrix[i][i] == 0) {
            return 0
        }
        for(let j = 0; j < n; j++) {
            if(i != j) {
                ratio = full_matrix[j][i]/full_matrix[i][i]
                for(let k = 0; k < n+1; k++) {
                    full_matrix[j][k] = full_matrix[j][k] - ratio * full_matrix[i][k]
                }
            }
        }
    }
    for(let i = 0; i < n; i++) {
        x[i] = full_matrix[i][n] / full_matrix[i][i]
    }
    return x
}