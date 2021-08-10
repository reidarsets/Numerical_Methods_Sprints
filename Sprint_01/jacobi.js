
function jacobi_method (matrix, results) {
	let n = matrix.length
	let tmp_arr = new Array(n)
	let x = new Array(n)
	for(let i = 0; i < n; i++){
		x[i] = 0
	}
	let exp = 0
	let eps = 0.0001
	do{
		for(let i = 0; i < n; i++){
			tmp_arr[i] = 0
			for(let j = 0; j < n; j++){
				if(i != j){
					tmp_arr[i] = tmp_arr[i] + (matrix[i][j] * x[j])
				}
			}
			tmp_arr[i] = (results[i] - tmp_arr[i]) / matrix[i][i]
		}
		exp = 0
		for(let i = 0; i < n; i++){
			if(Math.abs(x[i] - tmp_arr[i]) > exp){
				exp = Math.abs(x[i] - tmp_arr[i])
			}
			x[i] = tmp_arr[i]
		}
	}while(exp > eps)
	return x
}
