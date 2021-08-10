import React, { useRef, useState } from 'react';
import { useDispatch } from 'react-redux';
import {
  Box,
  Drawer,
  Hidden,
  List,
  Typography,
} from '@material-ui/core';
import {
  Dashboard as DashboardIcon,
  Business as BusinessIcon,
  Assessment as AnalysisIcon,
  AccountBalance as MarketIcon,
  HighQuality as HedgeIcon,
  Gavel as SandboxIcon,
  Description as DocIcon,
  Help as SupportIcon,
  PermIdentity as AccountIcon,
} from '@material-ui/icons';

import IdleTimer from 'react-idle-timer';

import { logout } from 'src/store/actions/auth';

import Logo from 'src/components/images/Logo';
import { HEADER_HEIGHT, IDLE_TIMEOUT } from 'src/constants';
import { LAST_PATH } from 'src/constants/localStorageKeys';
import Header from './Header';
import NavItem from './NavItem';

import useStyles from './style';

const items = [
  {
    href: '/main/dashboard',
    icon: DashboardIcon,
    title: 'Dashboard',
  },
  {
    icon: BusinessIcon,
    title: 'Business',
    subItems: [
      { href: '/business/basic-info', title: 'Basic Info' },
      { href: '/business/condition', title: 'Condition' },
      { href: '/business/finance', title: 'Finance' },
      { href: '/business/preference', title: 'Preference' },
    ],
  },
  {
    icon: AnalysisIcon,
    title: 'Risk Analysis',
    subItems: [
      { href: '/risk-analysis/financial-forecast', title: 'Financial Forecast' },
      { href: '/risk-analysis/systemic-risk', title: 'Systemic Risk' },
      { href: '/risk-analysis/structural-risk', title: 'Structural Risk' },
      { href: '/risk-analysis/conditional-risk', title: 'Conditional Risk' },
      { href: '/risk-analysis/hedgeability', title: 'Hedgeability' },
    ],
  },
  {
    href: '/markets',
    icon: MarketIcon,
    title: 'Markets',
  },
  {
    href: '/hedging',
    icon: HedgeIcon,
    title: 'Hedging',
  },
  {
    href: '/sandbox',
    icon: SandboxIcon,
    title: 'Sandbox',
  },
  {
    href: '/docs',
    icon: DocIcon,
    title: 'Docs',
  },
  {
    href: '/support',
    icon: SupportIcon,
    title: 'Support',
  },
  {
    icon: AccountIcon,
    title: 'User',
    subItems: [
      { href: '/user/setting', title: 'Setting' },
      { href: '/user/notification', title: 'Notification' },
    ],
  },
];

function Layout({ children }) {
  const classes = useStyles();
  const idleTimerRef = useRef(null);

  const [drawerOpen, setDrawerOpen] = React.useState(false);
  const toggleDrawer = () => setDrawerOpen((open) => !open);

  // User Idle logout variables
  const [isTimedOut, setIsTimedout] = useState(false);
  const [timeout] = useState(IDLE_TIMEOUT);

  const dispatch = useDispatch();

  // If action detected, set timeout false
  const onAction = () => {
    setIsTimedout(false);
  };

  // If active tab detected, set timeout false
  const onActive = () => {
    setIsTimedout(false);
  };

  // Navigate to login page
  const handleLogout = () => {
    // Before logout, save last path to session storage so user back again after login
    if (window !== undefined || window !== null) {
      const currentPath = window.location.pathname;
      window.sessionStorage.setItem(LAST_PATH, currentPath);
    }
    dispatch(logout());
  };

  // If no action detected, and timed out, go to login
  const onIdle = () => {
    if (isTimedOut) {
      handleLogout();
    } else {
      idleTimerRef.current.reset();
      setIsTimedout(true);
    }
  };

  const content = (
    <Box height="100%">
      <Box display="flex" alignItems="center" height={`${HEADER_HEIGHT}px`} px="30px" py="20px" color="#fff">
        <Logo color="#fff" />
        <Typography variant="h5" style={{ marginLeft: 16 }}>Prussian AI</Typography>
      </Box>
      <Box height={`calc(100% - ${HEADER_HEIGHT}px)`}>
        <List disablePadding>
          {items.map((item) => (
            <NavItem key={item.title} item={item} />
          ))}
        </List>
      </Box>
    </Box>
  );

  const container = window !== undefined ? () => window.document.body : undefined;

  return (
    <>
      <IdleTimer
        ref={idleTimerRef}
        element={document}
        onActive={onActive}
        onIdle={onIdle}
        onAction={onAction}
        debounce={250}
        timeout={timeout}
      />

      <Box className={classes.root}>
        <nav className={classes.drawer} aria-label="sidebar">
          {/* The implementation can be swapped with js to avoid SEO duplication of links. */}
          <Hidden mdUp implementation="css">
            <Drawer
              container={container}
              variant="temporary"
              anchor="left"
              open={drawerOpen}
              onClose={toggleDrawer}
              classes={{
                paper: classes.drawerPaper,
              }}
              ModalProps={{
                keepMounted: true, // Better open performance on mobile.
              }}
            >
              {content}
            </Drawer>
          </Hidden>
          <Hidden smDown implementation="css">
            <Drawer
              classes={{
                paper: classes.drawerPaper,
              }}
              variant="permanent"
              open
            >
              {content}
            </Drawer>
          </Hidden>
        </nav>
        <Box component="main" className={classes.content}>
          <Header toggleDrawer={toggleDrawer} />
          <Box className={classes.wrapper}>
            {children}
          </Box>
        </Box>
      </Box>
    </>
  );
}

export default Layout;
