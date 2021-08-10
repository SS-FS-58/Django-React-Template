import React from 'react';
import { NavLink as RouterLink, useLocation } from 'react-router-dom';
import clsx from 'clsx';
import {
  Box,
  Button,
  Collapse,
  List,
  ListItem,
  makeStyles,
} from '@material-ui/core';
import {
  ExpandLess as ExpandLessIcon,
  ExpandMore as ExpandMoreIcon,
} from '@material-ui/icons';

const useStyles = makeStyles((theme) => ({
  item: {
    display: 'flex',
    paddingTop: 0,
    paddingBottom: 0,
  },
  button: {
    width: '100%',
    justifyContent: 'flex-start',
    alignItems: 'center',
    fontSize: '1rem',
    color: '#fff',
    letterSpacing: 0,
    padding: '20px 30px',
    textTransform: 'none',
    borderRadius: 0,
    fontWeight: 400,
  },
  icon: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    width: 30,
    height: 20,
    marginRight: 15,
  },
  active: {
    backgroundColor: '#1E293A',
  },
  subItem: {
    paddingLeft: '75px',
    backgroundColor: theme.palette.background.dark,
  },
  activeColor: {
    backgroundColor: '#1E293A',
  },
}));

function NavItem({
  className, item, ...rest
}) {
  const classes = useStyles();
  const location = useLocation();
  const [open, setOpen] = React.useState(false);

  const { icon: Icon } = item;

  React.useEffect(() => {
    if (item.subItems && location.pathname.includes(item.prefix)) {
      setOpen(true);
    }
  }, [location.pathname, item.subItems, item.prefix]);

  const toggleOpen = () => {
    setOpen(!open);
  };

  return (
    <ListItem className={clsx(classes.item, className)} disableGutters {...rest}>
      {item.href ? (
        <Button
          activeClassName={classes.active}
          className={classes.button}
          component={RouterLink}
          to={item.href}
        >
          {item.icon && <Box className={classes.icon}><Icon /></Box>}
          <span>{item.title}</span>
        </Button>
      ) : (
        <Box width="100%">
          <Button
            className={clsx({
              [classes.button]: true,
              [classes.activeColor]: location.pathname.includes(item.prefix),
            })}
            onClick={toggleOpen}
          >
            {item.icon && <Box className={classes.icon}><Icon /></Box>}
            <span>{item.title}</span>
            <Box flexGrow={1} />
            {item.subItems && item.subItems.length > 0 && open ? (
              <ExpandLessIcon />
            ) : (
              <ExpandMoreIcon />
            )}
          </Button>
          <Collapse in={open} timeout="auto" unmountOnExit>
            <List className={classes.subNav} component="div" disablePadding>
              {item.subItems && item.subItems.map(({ href: subHref, title: subTitle }, index) => (
                <Button
                  key={index}
                  activeClassName={classes.active}
                  className={clsx(classes.button, classes.subItem)}
                  component={RouterLink}
                  to={subHref}
                >
                  <span>{subTitle}</span>
                </Button>
              ))}
            </List>
          </Collapse>
        </Box>
      )}
    </ListItem>
  );
}

export default NavItem;
