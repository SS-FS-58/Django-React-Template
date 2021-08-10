import * as React from 'react';
import { useDispatch } from 'react-redux';
// import { useHistory } from 'react-router-dom';
import {
  Box,
  Button,
  Card,
  CardActions,
  CardContent,
  Container,
  Divider,
  Typography,
  Switch,
  FormControlLabel,
} from '@material-ui/core';
import { useFormik } from 'formik';

// import { InputField } from 'src/components';
import { basicInfo } from 'src/store/actions/business';

import validationSchema from './schema';

function Notification() {
  // const history = useHistory();
  const dispatch = useDispatch();

  const handleSubmit = async (values) => {
    await dispatch(
      basicInfo(values),
    );
  };
  const [checked, setChecked] = React.useState();
  const handleChange = (event) => {
    setChecked(event.target.checked);
  };

  const formik = useFormik({
    initialValues: {
      checked: true,
    },
    validationSchema,
    onSubmit: handleSubmit,
  });

  return (
    <Container maxWidth="lg">
      <form onSubmit={formik.handleSubmit}>
        <Typography variant="h4">Notificaiton</Typography>
        <Divider />
        <Card elevation={1}>
          <CardContent>
            <Typography variant="h6" style={{ marginBottom: 16 }}>Notificaiton</Typography>
            <FormControlLabel
              label=" Notification for user settings "
              labelPlacement="start"
              control={<Switch checked={checked} onChange={handleChange} color="primary" />}
            />
          </CardContent>
          <CardActions>
            <Box display="flex" justifyContent="flex-end" width="100%" marginBottom="16px">
              <Button type="submit" color="primary" variant="contained">
                Update
              </Button>
            </Box>
          </CardActions>
        </Card>
      </form>
    </Container>
  );
}

export default Notification;
