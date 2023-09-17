// /**
//  * @param {string} val
//  * @return {Object}
//  */
// var expect = function(val) {
//     return{
//     toBe: function(newVal){
//         if (val !== newVal){
//             return Error("Not Equal")
//         }
//         else return true
        
//     },
//     notToBe: function(newVal){
//         if (val ===newVal){
//             return Error("Equal")
//         }
//         else return True
//     }
//     }
// };
var expect = function(val) {
  return {
    toBe: (val2) => {
      if(val !== val2) throw new Error("Not Equal");
      return true;
    },
    notToBe: (val2) => {
      if(val === val2) throw new Error("Equal");
      return true;
    }
  };
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */