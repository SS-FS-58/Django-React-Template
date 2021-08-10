import * as React from 'react';
import { Box, CircularProgress } from '@material-ui/core';

function Loader() {
  return (
    <Box width="100%" height="100%" display="flex" alignItems="center" justifyContent="center">
      <CircularProgress color="primary" />
    </Box>
  );
}

export default Loader;
