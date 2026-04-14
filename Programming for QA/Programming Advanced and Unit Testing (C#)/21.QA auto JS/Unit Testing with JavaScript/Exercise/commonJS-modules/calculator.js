// This is commonJS module

function sum(a, b) {
    return a + b;
}

function subtract(a, b) {
    return a - b;
}

// Named exports
exports.sum = sum;
exports.subtract = subtract;

// export default sum;
// module.exports = sum;

// Export default object
// module.exports = {
//     sum,
//     subtract,
// };
