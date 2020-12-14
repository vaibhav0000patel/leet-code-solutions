/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stack = [];
    let opening = ["(","[","{"];
    let closing = [")","]","}"];
    var i;
    if(s.length%2!=0) return false;
    for (i = 0; i < s.length; i++) {
        if (opening.includes(s[i])) stack.push(s[i]);
        else{
            if(stack.length==0) return false;
            if(stack[stack.length-1]!==opening[closing.indexOf(s[i])]) return false;
            stack = stack.slice(0, stack.length-1);
        }
    }
    if(stack.length!=0) return false;
    return true;
};