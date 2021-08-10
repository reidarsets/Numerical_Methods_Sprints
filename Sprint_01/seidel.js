function conv(x, p, EPS) {
	let n = x.length
	let norm = 0
	for (let i = 0; i < n; i++) {
		norm += (x[i] - p[i]) * (x[i] - p[i])
	}
	return (Math.sqrt(norm) < EPS)
}
function accur(x, EPS) {
	let i = 0
	let neweps = EPS
	while (neweps < 1) {
		i++
		neweps *= 10
	}
	let accur = Math.pow(10, i)
	x = (x * accur + 0.5) / (accur)
	return x
}
function diagonal(matrix) {
	let k = 1
	let n = matrix.length
	let sum = 0
	for (let i = 0; i < n; i++) {
		sum = 0
		for (let j = 0; j < n; j++) {
			sum += Math.abs(matrix[i][j])
		}
		sum -= Math.abs(matrix[i][i])
		if (sum > matrix[i][i]) {
			k = 0
		}
	}
	return (k == 1)
}
function seidel_method(matrix,results) {
	let n = matrix.length
	let EPS = 0.0001
	let x = new Array(n)
	let answers = new Array(n)
	let p = new Array(n)
	let m = 0
	for(let i = 0; i < n; i++) {
		x[i] = 1
	}
	if (diagonal(matrix)) {
		do {
			for (let i = 0; i < n; i++) {
				p[i] = x[i]
			}
			for (let i = 0; i < n; i++)
			{
				let temp = 0
				for (let j = 0; j < n; j++) {
                    if(j!=i) {
						temp += (matrix[i][j] * x[j])
					}
				}
				x[i] = (results[i] - temp) / matrix[i][i]
			}
			m++
			if(m > 100000) {
				return 0
			}
		} while (!conv(x, p, EPS))
		for (i = 0; i < n; i++) {
			answers[i] = accur(x[i], EPS)
		}
		return answers
	}
	else {
		alert("Не выполняется преобладание диагоналей!")
		return 0
	}
}