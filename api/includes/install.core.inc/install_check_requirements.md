# install_check_requirements()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 1639–1758 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L1639-L1758)

## Signature

```php
function install_check_requirements($install_state)
```

## Documentation

```text
Checks installation requirements and reports any errors.
```

## Code

```php
function install_check_requirements($install_state) {
  $profile = $install_state['parameters']['profile'];

  // Check the profile requirements.
  $requirements = drupal_check_profile($profile);

  // If Drupal is not set up already, we need to create a settings file.
  if (!$install_state['settings_verified']) {
    $writable = FALSE;
    $conf_path = './' . conf_path(FALSE, TRUE);
    $settings_file = $conf_path . '/settings.php';
    $default_settings_file = './sites/default/default.settings.php';
    $file = $conf_path;
    $exists = FALSE;
    // Verify that the directory exists.
    if (drupal_verify_install_file($conf_path, FILE_EXIST, 'dir')) {
      // Check if a settings.php file already exists.
      $file = $settings_file;
      if (drupal_verify_install_file($settings_file, FILE_EXIST)) {
        // If it does, make sure it is writable.
        $writable = drupal_verify_install_file($settings_file, FILE_READABLE|FILE_WRITABLE);
        $exists = TRUE;
      }
    }

    // If default.settings.php does not exist, or is not readable, throw an
    // error.
    if (!drupal_verify_install_file($default_settings_file, FILE_EXIST|FILE_READABLE)) {
      $requirements['default settings file exists'] = array(
        'title'       => st('Default settings file'),
        'value'       => st('The default settings file does not exist.'),
        'severity'    => REQUIREMENT_ERROR,
        'description' => st('The @drupal installer requires that the %default-file file not be modified in any way from the original download.', array('@drupal' => drupal_install_profile_distribution_name(), '%default-file' => $default_settings_file)),
      );
    }
    // Otherwise, if settings.php does not exist yet, we can try to copy
    // default.settings.php to create it.
    elseif (!$exists) {
      $copied = drupal_verify_install_file($conf_path, FILE_EXIST|FILE_WRITABLE, 'dir') && @copy($default_settings_file, $settings_file);
      if ($copied) {
        // If the new settings file has the same owner as default.settings.php,
        // this means default.settings.php is owned by the webserver user.
        // This is an inherent security weakness because it allows a malicious
        // webserver process to append arbitrary PHP code and then execute it.
        // However, it is also a common configuration on shared hosting, and
        // there is nothing Drupal can do to prevent it. In this situation,
        // having settings.php also owned by the webserver does not introduce
        // any additional security risk, so we keep the file in place.
        if (fileowner($default_settings_file) === fileowner($settings_file)) {
          $writable = drupal_verify_install_file($settings_file, FILE_READABLE|FILE_WRITABLE);
          $exists = TRUE;
        }
        // If settings.php and default.settings.php have different owners, this
        // probably means the server is set up "securely" (with the webserver
        // running as its own user, distinct from the user who owns all the
        // Drupal PHP files), although with either a group or world writable
        // sites directory. Keeping settings.php owned by the webserver would
        // therefore introduce a security risk. It would also cause a usability
        // problem, since site owners who do not have root access to the file
        // system would be unable to edit their settings file later on. We
        // therefore must delete the file we just created and force the
        // administrator to log on to the server and create it manually.
        else {
          $deleted = @drupal_unlink($settings_file);
          // We expect deleting the file to be successful (since we just
          // created it ourselves above), but if it fails somehow, we set a
          // variable so we can display a one-time error message to the
          // administrator at the bottom of the requirements list. We also try
          // to make the file writable, to eliminate any conflicting error
          // messages in the requirements list.
          $exists = !$deleted;
          if ($exists) {
            $settings_file_ownership_error = TRUE;
            $writable = drupal_verify_install_file($settings_file, FILE_READABLE|FILE_WRITABLE);
          }
        }
      }
    }

    // If settings.php does not exist, throw an error.
    if (!$exists) {
      $requirements['settings file exists'] = array(
        'title'       => st('Settings file'),
        'value'       => st('The settings file does not exist.'),
        'severity'    => REQUIREMENT_ERROR,
        'description' => st('The @drupal installer requires that you create a settings file as part of the installation process. Copy the %default_file file to %file. More details about installing Drupal are available in <a href="@install_txt">INSTALL.txt</a>.', array('@drupal' => drupal_install_profile_distribution_name(), '%file' => $file, '%default_file' => $default_settings_file, '@install_txt' => base_path() . 'INSTALL.txt')),
      );
    }
    else {
      $requirements['settings file exists'] = array(
        'title'       => st('Settings file'),
        'value'       => st('The %file file exists.', array('%file' => $file)),
      );
      // If settings.php is not writable, throw an error.
      if (!$writable) {
        $requirements['settings file writable'] = array(
          'title'       => st('Settings file'),
          'value'       => st('The settings file is not writable.'),
          'severity'    => REQUIREMENT_ERROR,
          'description' => st('The @drupal installer requires write permissions to %file during the installation process. If you are unsure how to grant file permissions, consult the <a href="@handbook_url">online handbook</a>.', array('@drupal' => drupal_install_profile_distribution_name(), '%file' => $file, '@handbook_url' => 'http://drupal.org/server-permissions')),
        );
      }
      else {
        $requirements['settings file'] = array(
          'title'       => st('Settings file'),
          'value'       => st('The settings file is writable.'),
        );
      }
      if (!empty($settings_file_ownership_error)) {
        $requirements['settings file ownership'] = array(
          'title'       => st('Settings file'),
          'value'       => st('The settings file is owned by the web server.'),
          'severity'    => REQUIREMENT_ERROR,
          'description' => st('The @drupal installer failed to create a settings file with proper file ownership. Log on to your web server, remove the existing %file file, and create a new one by copying the %default_file file to %file. More details about installing Drupal are available in <a href="@install_txt">INSTALL.txt</a>. If you have problems with the file permissions on your server, consult the <a href="@handbook_url">online handbook</a>.', array('@drupal' => drupal_install_profile_distribution_name(), '%file' => $file, '%default_file' => $default_settings_file, '@install_txt' => base_path() . 'INSTALL.txt', '@handbook_url' => 'http://drupal.org/server-permissions')),
        );
      }
    }
  }
  return $requirements;
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
