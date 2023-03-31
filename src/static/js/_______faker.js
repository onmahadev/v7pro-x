/**
 * Skipped minification because the original files appears to be already minified.
 * Original file: /npm/@faker-js/faker@7.3.0/dist/cjs/index.js
 *
 * Do NOT use SRI with dynamically generated files! More information: https://www.jsdelivr.com/using-sri-with-dynamic-files
 */
"use strict";var c=Object.create;var t=Object.defineProperty;var l=Object.getOwnPropertyDescriptor;var p=Object.getOwnPropertyNames;var y=Object.getPrototypeOf,C=Object.prototype.hasOwnProperty;var d=(e,i)=>{for(var n in i)t(e,n,{get:i[n],enumerable:!0})},f=(e,i,n,s)=>{if(i&&typeof i=="object"||typeof i=="function")for(let o of p(i))!C.call(e,o)&&o!==n&&t(e,o,{get:()=>i[o],enumerable:!(s=l(i,o))||s.enumerable});return e};var F=(e,i,n)=>(n=e!=null?c(y(e)):{},f(i||!e||!e.__esModule?t(n,"default",{value:e,enumerable:!0}):n,e)),u=e=>f(t({},"__esModule",{value:!0}),e);var S={};d(S,{Faker:()=>r.Faker,FakerError:()=>a.FakerError,Gender:()=>D.Gender,faker:()=>x});module.exports=u(S);var r=require("./faker"),m=F(require("./locales")),a=require("./errors/faker-error"),D=require("./modules/name");const x=new r.Faker({locales:m.default});0&&(module.exports={Faker,FakerError,Gender,faker});
