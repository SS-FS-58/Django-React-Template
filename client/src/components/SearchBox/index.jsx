import _ from 'lodash';
import React, { useCallback, useEffect, useState } from 'react';
import { useHistory } from 'react-router-dom';
import {
  fade,
  InputBase,
  makeStyles,
} from '@material-ui/core';
import Autocomplete from '@material-ui/lab/Autocomplete';
import { Search as SearchIcon } from '@material-ui/icons';

import marketService from 'src/services/marketService';

const useStyles = makeStyles((theme) => ({
  inputRoot: {
    color: theme.palette.text.primary,
  },
  inputInput: {
    padding: theme.spacing(1, 1, 1, 0),
    // vertical padding + font size from searchIcon
    paddingLeft: `calc(1em + ${theme.spacing(4)}px)`,
    transition: theme.transitions.create('width'),
    width: '100%',
    [theme.breakpoints.up('md')]: {
      width: '20ch',
    },
  },
  search: {
    position: 'relative',
    borderRadius: theme.shape.borderRadius,
    backgroundColor: fade(theme.palette.secondary.main, 0.05),
    '&:hover': {
      backgroundColor: fade(theme.palette.secondary.main, 0.15),
    },
    marginRight: theme.spacing(2),
    marginLeft: 0,
    width: '100%',
    [theme.breakpoints.up('sm')]: {
      width: 'auto',
    },
  },
  searchIcon: {
    padding: theme.spacing(0, 2),
    height: '100%',
    position: 'absolute',
    pointerEvents: 'none',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    color: theme.palette.text.primary,
  },
}));

function Loader() {
  const classes = useStyles();
  const history = useHistory();
  const [query, setQuery] = useState('');
  const [autoCompletes, setAutoCompletes] = useState([]);

  useEffect(async () => {
    if (query) {
      try {
        const response = await marketService.yahooAutoComplete({ q: query, region: 'US' });
        if (response.data) {
          const tickers = response.data.quotes ? response.data.quotes.map((ticker) => ({ ...ticker, type: 'Ticker' })) : [];
          const navs = response.data.navs ? response.data.navs.map((nav) => ({ ...nav, type: 'Market' })) : [];
          setAutoCompletes(_.concat([], tickers, navs));
        }
      } catch (error) {
        setAutoCompletes([]);
      }
    } else {
      setAutoCompletes([]);
    }
  }, [query, marketService]);

  function onSearchTextHandler(event, value, reason) {
    if (reason === 'input') {
      setQuery(event.target.value);
    }
    if (reason === 'clear') {
      setQuery('');
    }
  }

  function gotoSearch(q) {
    history.push(`/search?q=${q}`);
  }

  const onKeyPress = useCallback((e) => {
    if (e.code === 'Enter' && query) {
      gotoSearch(query);
    }
  }, [query, history]);

  const getTypedName = (option) => (
    option.type === 'Ticker' ? option.symbol
        : option.type === 'Market' ? option.navName
        : ''
  );

  return (
    <Autocomplete
      disableClearable
      options={autoCompletes}
      // groupBy={(option) => option.type}
      getOptionLabel={(option) => getTypedName(option)}
      getOptionSelected={(option, value) => getTypedName(option) === getTypedName(value)}
      onChange={(event, newOption) => {
        const q = getTypedName(newOption);
        setQuery(q);
        gotoSearch(q);
      }}
      value={undefined}
      onInputChange={onSearchTextHandler}
      inputValue={query}
      renderInput={(params) => (
        <div className={classes.search}>
          <div className={classes.searchIcon}>
            <SearchIcon />
          </div>
          <InputBase
            ref={params.InputProps.ref}
            inputProps={params.inputProps}
            placeholder="Search…"
            classes={{
              root: classes.inputRoot,
              input: classes.inputInput,
            }}
            onKeyPress={onKeyPress}
          />
        </div>
      )}
    />
  );
}

export default Loader;
