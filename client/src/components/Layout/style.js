import { makeStyles } from '@material-ui/styles';

import { DRAWER_WIDTH, HEADER_HEIGHT, MOBILE_HEADER_HEIGHT } from 'src/constants';
import { SECONDARY } from 'src/constants/colors';

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
  },
  logo: {
    fontWeight: 'bold',
  },
  drawer: {
    [theme.breakpoints.up('md')]: {
      width: DRAWER_WIDTH,
      flexShrink: 0,
    },
  },
  // necessary for content to be below app bar
  toolbar: theme.mixins.toolbar,
  drawerPaper: {
    width: DRAWER_WIDTH,
    backgroundColor: SECONDARY,
  },
  content: {
    height: '100vh',
    flexGrow: 1,
  },
  wrapper: {
    width: `calc(100vw - ${DRAWER_WIDTH}px)`,
    minHeight: `calc(100vh - ${HEADER_HEIGHT}px)`,
    padding: '45px 60px',
    backgroundColor: theme.palette.background.light,
    overflowY: 'auto',
    [theme.breakpoints.down('md')]: {
      minHeight: `calc(100vh - ${MOBILE_HEADER_HEIGHT}px)`,
      padding: '20px 30px',
    },
    [theme.breakpoints.down('sm')]: {
      padding: '10px 15px',
      width: '100vw',
    },
  },
  blur: {
    filter: 'blur(6px)',
  },
  backdrop: {
    top: HEADER_HEIGHT,
    left: DRAWER_WIDTH,
    backgroundColor: theme.palette.secondary.dark,
    opacity: '0.85 !important',
    zIndex: 1,
    [theme.breakpoints.down('sm')]: {
      top: `${MOBILE_HEADER_HEIGHT}px !important`,
      left: '0px !important',
    },
  },
  disableScroll: {
    overflow: 'hidden',
  },
}));

export default useStyles;
