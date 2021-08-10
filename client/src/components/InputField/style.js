import { makeStyles } from '@material-ui/core';

export default makeStyles(() => ({
  input: {
    width: '100%',
    fontSize: 14,

    '& input': {
      '&::placeholder': {
        fontSize: '14px !important',
        fontWeight: 400,
        color: '#9E9E9E',
        opacity: 1,
      },
    },
  },
}));
