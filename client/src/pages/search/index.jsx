import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';
import {
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  makeStyles,
 } from '@material-ui/core';

import marketService from 'src/services/marketService';

const useStyles = makeStyles({
  table: {
    minWidth: 650,
  },
});

function Search() {
  const classes = useStyles();
  const q = new URLSearchParams(useLocation().search);
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  useEffect(() => {
    setQuery(q.get('q'));
  }, [q]);

  useEffect(async () => {
    if (query) {
      try {
        const response = await marketService.yahooMarketAutoComplete({ query, region: 'US' });
        if (response.data && response.data.ResultSet.Result) {
          setResults(response.data.ResultSet.Result);
        }
      } catch (error) {
        setResults([]);
      }
    }
  }, [marketService, query, setResults]);

  return (
    <div>
      {/* <h2>{`Search Results for "${query}"`}</h2> */}
      {results.length > 0 && (
        <TableContainer component={Paper}>
          <Table className={classes.table} aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell>Symbol</TableCell>
                <TableCell>Name</TableCell>
                <TableCell>Exch</TableCell>
                <TableCell>Type</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {results.map((market) => (
                <TableRow key={market.symbol}>
                  <TableCell component="th" scope="row">
                    {market.symbol}
                  </TableCell>
                  <TableCell>{market.name}</TableCell>
                  <TableCell>{market.exchDisp}</TableCell>
                  <TableCell>{market.typeDisp}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      )}
    </div>
  );
}

export default Search;
