import { makeStyles } from '@material-ui/core';

export default makeStyles((theme) => ({
  root: {
    display: 'flex',
    width: '100vw',
    height: '100vh',
    backgroundColor: theme.palette.background.light,
    alignItems: 'center',
    justifyContent: 'center',
  },
  wrapper: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    width: '100%',
    maxWidth: 520,
    padding: 24,
    backgroundColor: '#fff',
    borderRadius: 4,
    [theme.breakpoints.up('sm')]: {
      padding: 40,
    },
  },
  logo: {
    width: 100,
    height: 100,
    marginBottom: 24,
  },
}));
