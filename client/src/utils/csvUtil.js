const splitCSVRow = (str) => {
  // return str.match(/(".*?"|[^",\s]+)(?=\s*,|\s*$)/g);
  const re_valid = /^\s*(?:'[^'\\]*(?:\\[\S\s][^'\\]*)*'|"[^"\\]*(?:\\[\S\s][^"\\]*)*"|[^,'"\s\\]*(?:\s+[^,'"\s\\]+)*)\s*(?:,\s*(?:'[^'\\]*(?:\\[\S\s][^'\\]*)*'|"[^"\\]*(?:\\[\S\s][^"\\]*)*"|[^,'"\s\\]*(?:\s+[^,'"\s\\]+)*)\s*)*$/;
  const re_value = /(?!\s*$)\s*(?:'([^'\\]*(?:\\[\S\s][^'\\]*)*)'|"([^"\\]*(?:\\[\S\s][^"\\]*)*)"|([^,'"\s\\]*(?:\s+[^,'"\s\\]+)*))\s*(?:,|$)/g;
  // Return NULL if input string is not well formed CSV string.
  if (!re_valid.test(str)) return null;
  const res = []; // Initialize array to receive values.
  str.replace(
    re_value, // "Walk" the string using replace with callback.
    (m0, m1, m2, m3) => {
      // Remove backslash from \' in single quoted values.
      if (m1 !== undefined) res.push(m1.replace(/\\'/g, "'"));
      // Remove backslash from \" in double quoted values.
      else if (m2 !== undefined) res.push(m2.replace(/\\"/g, '"'));
      else if (m3 !== undefined) res.push(m3);
      return ''; // Return empty string.
    },
  );

  // Handle special case of empty last value.
  if (/,\s*$/.test(str)) res.push('');
  return res;
};

const parseCSV = (data) => {
  let objKeyPulled = false;
  const allRows = data.split(/\r/);
  let objKeys = [];
  if (allRows.length <= 0) {
    return [];
  }
  const arr = [];
  // eslint-disable-next-line no-plusplus
  for (let i = 0; i < allRows.length; i++) {
    // Need to split each rows by comma,
    // But ignore comman within double quote. ex: a, "6, 7", c
    const cols = splitCSVRow(allRows[i]);

    // Need to skip empty row
    if (cols && cols.length !== 0) {
      if (!objKeyPulled) {
        objKeys = cols; // getKeys(allRows[i]);
        objKeyPulled = true;
        // eslint-disable-next-line no-continue
        continue;
      }
      const row = {};

      // eslint-disable-next-line no-plusplus
      for (let k = 0; k < objKeys.length; k++) {
        // if we export excel sheet to csv, it ends with new line, so we need to check null
        if (cols !== null) {
          if (!objKeys[k].includes('Tag-[')) {
            // eslint-disable-next-line prefer-destructuring
            row[objKeys[k]] = cols[k].split('\n')[0];
          } else row[objKeys[k]] = cols[k];
        }
      }
      arr.push(row);
    }
  }
  // res will look like [{id: 1, name: tax1, description: tax1}, ..., {...}]
  return arr;
};
export {
  splitCSVRow,
  parseCSV,
};
