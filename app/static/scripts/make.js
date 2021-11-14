/**
 * make.js: all the comforts of a JavaScript framework, without the
 * JavaScript framework.  Code by Jason Knight, available at 
 * https://medium.com/codex/part-of-why-i-think-react-is-junk-e4db95e15ef4.
 *
 * Licensing status of this code is uncertain, I will remove and adapt
 * if there are issues.
 */
function makeAppend(e, data) {
  if(data instanceof Array) {
    for(let row of data) {
      e.append(row instanceof Array ? make(...row) : row);
    }
  } else {
    e.append(data);
  }
}

function setAttribute(e, name, value) {
  if(value instanceof Array
     || ("object" == typeof value)
     || ("function" == typeof value)) {
    e[name] = value;
  } else {
    e.setAttribute(name === "className" ? "class" : name, value);
  }
}

function make(tagName, data) {
  let e = document.createElement(tagName);
  if(data) {
    if(data instanceof Array
       || data instanceof Node
       || ("object" !== typeof data)) {
      return makeAppend(e, data), e;
    }
  }

  if(data.append) {
    makeAppend(e, data.append);
  }

  if(data.attr) {
    for(let [name, value] of Object.entries(data.attr)) {
      setAttribute(e, name, value);
    }
  }

  if(data.style) {
    Object.assign(e.style, data.style);
  }

  if(data.repeat) {
    while(data.repeat[0]--) {
      e.append(make(data.repeat[1], data.repeat[2]));
    }
  }

  if(data.parent) {
    data.parent.append(e);
  }

  return e;
}

function purge(e, amt) {
  let dir = amt < 0 ? "firstChild" : "lastChild";
  amt = Math.abs(amt);
  while(amt--) {
    e.removeChild(e[dir]);
  }
}

