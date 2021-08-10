import * as React from 'react';
import { useDispatch } from 'react-redux';
import {
  AppBar,
  Badge,
  Box,
  IconButton,
  Menu,
  MenuItem,
  Toolbar,
  makeStyles,
} from '@material-ui/core';
import {
  PermIdentity as AccountIcon,
  NotificationsNone as NotificationsIcon,
  Menu as MenuIcon,
} from '@material-ui/icons';

import SearchBox from 'src/components/SearchBox';
import { logout } from 'src/store/actions/auth';
import { HEADER_HEIGHT, MOBILE_HEADER_HEIGHT } from 'src/constants';

const useStyles = makeStyles((theme) => ({
  appBar: {
    background: '#fff',
    boxShadow: 'none',
    [theme.breakpoints.up('md')]: {
      width: '100%',
      height: 64,
    },
  },
  toolbar: {
    height: MOBILE_HEADER_HEIGHT,
    [theme.breakpoints.up('md')]: {
      height: HEADER_HEIGHT,
      paddingLeft: 60,
      paddingRight: 60,
    },
  },
  menuButton: {
    marginRight: theme.spacing(2),
    color: '#000',
    [theme.breakpoints.up('md')]: {
      display: 'none',
    },
  },
  breadcrumb: {
    width: '100%',
    whiteSpace: 'nowrap',
    overflow: 'hidden',
    textOverflow: 'ellipsis',
    textTransform: 'capitalize',
  },
}));

function Header({ toggleDrawer }) {
  const classes = useStyles();

  const [anchorEl, setAnchorEl] = React.useState(null);

  const dispatch = useDispatch();
  const open = Boolean(anchorEl);

  const handleMenu = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const handleLogout = () => {
    setAnchorEl(null);
    dispatch(logout());
  };

  return (
    <AppBar className={classes.appBar} position="relative">
      <Toolbar className={classes.toolbar}>
        <IconButton
          className={classes.menuButton}
          aria-label="open drawer"
          edge="start"
          onClick={toggleDrawer}
        >
          <MenuIcon />
        </IconButton>
        <SearchBox />
        <Box flexGrow={1} />
        <IconButton aria-label="show 17 new notifications" color="secondary">
          <Badge badgeContent={17} color="primary">
            <NotificationsIcon />
          </Badge>
        </IconButton>
        <div>
          <IconButton
            edge="end"
            aria-label="account of current user"
            aria-haspopup="true"
            color="secondary"
            onClick={handleMenu}
          >
            <AccountIcon />
          </IconButton>
          <Menu
            id="menu-appbar"
            anchorEl={anchorEl}
            anchorOrigin={{
              vertical: 'top',
              horizontal: 'right',
            }}
            keepMounted
            transformOrigin={{
              vertical: 'top',
              horizontal: 'right',
            }}
            open={open}
            onClose={handleClose}
          >
            <MenuItem>Profile</MenuItem>
            <MenuItem onClick={handleLogout}>Logout</MenuItem>
          </Menu>
        </div>
      </Toolbar>
    </AppBar>
  );
}

export default Header;
