function gauss_method(matrix, results)  {
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
    let tmp
    let xx = new Array(n)
    for (let i = 0; i<n; i++) {
        tmp = full_matrix[i][i];
        for (let j = n; j >= i; j--){
            full_matrix[i][j] /= tmp
        }
        for (let j = i + 1; j<n; j++) {
            tmp = full_matrix[j][i]
            for (let k = n; k >= i; k--) {
                full_matrix[j][k] -= tmp*full_matrix[i][k]
            }
        }
    }
    xx[n - 1] = full_matrix[n - 1][n]
    for (let i = n - 2; i >= 0; i--) {
        xx[i] = full_matrix[i][n]
        for (let j = i + 1; j<n; j++) {
          xx[i] -= full_matrix[i][j] * xx[j]
        }
    }
    return xx
}