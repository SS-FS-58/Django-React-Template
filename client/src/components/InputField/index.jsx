import * as React from 'react';
import {
  Box,
  FormControl,
  FormHelperText,
  InputLabel,
  MenuItem,
  Select,
  TextField,
  Button,
} from '@material-ui/core';

import useStyles from './style';

function InputField({
  formik,
  className,
  type = 'text',
  variant = 'outlined',
  name,
  label,
  hideError = false,
  width = '100%',
  options = [],
  onChange,
  onBlur,
  ...rest
}) {
  const classes = useStyles();

  const isError = !!formik.touched[name] && !!formik.errors[name];

  const handleChange = (event) => {
    formik.handleChange(event);
    if (onChange) {
      onChange(event);
    }
  };

  const handleBlur = (event) => {
    formik.handleBlur(event);
    if (onBlur) {
      onBlur(event);
    }
  };

  const handleFile = (event) => {
    formik.setFieldValue(name, event.target.files[0]);
  };

  const renderComponent = () => {
    if (type === 'select') {
      return (
        <FormControl variant="outlined" error={isError} style={{ width }}>
          {label && <InputLabel>{label}</InputLabel>}
          <Select
            {...formik.getFieldProps(name)}
            label={label}
            onChange={handleChange}
            onBlur={handleBlur}
            {...rest}
          >
            {options.map((option) => (
              <MenuItem value={option.value}>
                {option.label}
              </MenuItem>
            ))}
          </Select>
          {!hideError && isError && (
            <FormHelperText>{formik.errors[name]}</FormHelperText>
          )}
        </FormControl>
      );
    }
    if (type === 'file') {
      return (
        <FormControl error={isError} style={{ width }}>
          <Button
            variant={variant}
            component="label"
            dense="true"
            fullWidth
          >
            {label}
            <input
              {...formik.getFieldProps(name)}
              type="file"
              value={formik.values[name] ? formik.values[name].path : null}
              onChange={handleFile}
              onBlur={handleBlur}
              {...rest}
              hidden
            />
          </Button>
          <FormHelperText error={isError}>{!hideError && isError ? formik.errors[name] : ''}</FormHelperText>
        </FormControl>
      );
    }
    return (
      <TextField
        className={classes.input}
        type={type}
        label={label}
        variant={variant}
        {...formik.getFieldProps(name)}
        helperText={!hideError && isError ? formik.errors[name] : ''}
        error={isError}
        onChange={handleChange}
        onBlur={handleBlur}
        dense="true"
        {...rest}
        style={{ width }}
      />
    );
  };

  return (
    <Box className={className} width={width}>
      {renderComponent()}
    </Box>
  );
}

export default InputField;
