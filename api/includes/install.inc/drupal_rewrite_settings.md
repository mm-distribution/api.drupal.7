# drupal_rewrite_settings()

- **Type:** Function
- **File:** [`includes/install.inc`](_file.md), lines 590–667 · [local source](../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L590-L667)

## Signature

```php
function drupal_rewrite_settings($settings = array(), $prefix = '')
```

## Documentation

```text
Replaces values in settings.php with values in the submitted array.

@param $settings
  An array of settings that need to be updated.
```

## Code

```php
function drupal_rewrite_settings($settings = array(), $prefix = '') {
  $default_settings = 'sites/default/default.settings.php';
  drupal_static_reset('conf_path');
  $settings_file = conf_path(FALSE) . '/' . $prefix . 'settings.php';

  // Build list of setting names and insert the values into the global namespace.
  $keys = array();
  foreach ($settings as $setting => $data) {
    $GLOBALS[$setting] = $data['value'];
    $keys[] = $setting;
  }

  $buffer = NULL;
  $first = TRUE;
  if ($fp = fopen(DRUPAL_ROOT . '/' . $default_settings, 'r')) {
    // Step line by line through settings.php.
    while (!feof($fp)) {
      $line = fgets($fp);
      if ($first && substr($line, 0, 5) != '<?php') {
        $buffer = "<?php\n\n";
      }
      $first = FALSE;
      // Check for constants.
      if (substr($line, 0, 7) == 'define(') {
        preg_match('/define\(\s*[\'"]([A-Z_-]+)[\'"]\s*,(.*?)\);/', $line, $variable);
        if (in_array($variable[1], $keys)) {
          $setting = $settings[$variable[1]];
          $buffer .= str_replace($variable[2], " '" . $setting['value'] . "'", $line);
          unset($settings[$variable[1]]);
          unset($settings[$variable[2]]);
        }
        else {
          $buffer .= $line;
        }
      }
      // Check for variables.
      elseif (substr($line, 0, 1) == '$') {
        preg_match('/\$([^ ]*) /', $line, $variable);
        if (in_array($variable[1], $keys)) {
          // Write new value to settings.php in the following format:
          //    $'setting' = 'value'; // 'comment'
          $setting = $settings[$variable[1]];
          $buffer .= '$' . $variable[1] . " = " . var_export($setting['value'], TRUE) . ";" . (!empty($setting['comment']) ? ' // ' . $setting['comment'] . "\n" : "\n");
          unset($settings[$variable[1]]);
        }
        else {
          $buffer .= $line;
        }
      }
      else {
        $buffer .= $line;
      }
    }
    fclose($fp);

    // Add required settings that were missing from settings.php.
    foreach ($settings as $setting => $data) {
      if ($data['required']) {
        $buffer .= "\$$setting = " . var_export($data['value'], TRUE) . ";\n";
      }
    }

    $fp = fopen(DRUPAL_ROOT . '/' . $settings_file, 'w');
    if ($fp && fwrite($fp, $buffer) === FALSE) {
      throw new Exception(st('Failed to modify %settings. Verify the file permissions.', array('%settings' => $settings_file)));
    }
    else {
      // The existing settings.php file might have been included already. In
      // case an opcode cache is enabled, the rewritten contents of the file
      // will not be reflected in this process. Ensure to invalidate the file
      // in case an opcode cache is enabled.
      drupal_clear_opcode_cache(DRUPAL_ROOT . '/' . $settings_file);
    }
  }
  else {
    throw new Exception(st('Failed to open %settings. Verify the file permissions.', array('%settings' => $default_settings)));
  }
}
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
