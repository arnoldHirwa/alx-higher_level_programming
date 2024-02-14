#!/usr/bin/node
const dict = require('./101-data').dict;

const allList = Object.entries(dict);
const values = Object.values(dict);
const valuesUniq = [...new Set(values)];
const newDict = {};
for (const j in valuesUniq) {
  const list = [];
  for (const k in allList) {
    if (allList[k][1] === valuesUniq[j]) {
      list.unshift(allList[k][0]);
    }
  }
  newDict[valuesUniq[j]] = list;
}
console.log(newDict);
