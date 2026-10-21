# DrupalWebTestCase::prepareEnvironment()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 1471–1527 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L1471-L1527)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function prepareEnvironment()
```

## Documentation

```text
Prepares the current environment for running the test.

Backups various current environment variables and resets them, so they do
not interfere with the Drupal site installation in which tests are executed
and can be restored in tearDown().

Also sets up new resources for the testing environment, such as the public
filesystem and configuration directories.

@see DrupalWebTestCase::setUp()
@see DrupalWebTestCase::tearDown()
```

## Code

```php
  protected function prepareEnvironment() {
    global $user, $language, $language_url, $conf, $theme, $theme_key, $theme_path;

    // Store necessary current values before switching to prefixed database.
    $this->originalLanguage = $language;
    $this->originalLanguageUrl = $language_url;
    $this->originalLanguageDefault = variable_get('language_default');
    $this->originalFileDirectory = variable_get('file_public_path', conf_path() . '/files');
    $this->verboseDirectoryUrl = file_create_url($this->originalFileDirectory . '/simpletest/verbose');
    $this->originalProfile = drupal_get_profile();
    $this->originalCleanUrl = variable_get('clean_url', 0);
    $this->originalUser = $user;

    // Set to English to prevent exceptions from utf8_truncate() from t()
    // during install if the current language is not 'en'.
    // The following array/object conversion is copied from language_default().
    $language_url = $language = (object) array('language' => 'en', 'name' => 'English', 'native' => 'English', 'direction' => 0, 'enabled' => 1, 'plurals' => 0, 'formula' => '', 'domain' => '', 'prefix' => '', 'weight' => 0, 'javascript' => '');

    // Reset the theme globals.
    $this->originalTheme = $theme;
    $this->originalThemeKey = $theme_key;
    $this->originalThemePath = $theme_path;
    $theme = $theme_key = $theme_path = NULL;

    // Save and clean the shutdown callbacks array because it is static cached
    // and will be changed by the test run. Otherwise it will contain callbacks
    // from both environments and the testing environment will try to call the
    // handlers defined by the original one.
    $callbacks = &drupal_register_shutdown_function();
    $this->originalShutdownCallbacks = $callbacks;
    $callbacks = array();

    // Create test directory ahead of installation so fatal errors and debug
    // information can be logged during installation process.
    // Use temporary files directory with the same prefix as the database.
    $this->public_files_directory = $this->originalFileDirectory . '/simpletest/' . substr($this->databasePrefix, 10);
    $this->private_files_directory = $this->public_files_directory . '/private';
    $this->temp_files_directory = $this->private_files_directory . '/temp';

    // Create the directories
    file_prepare_directory($this->public_files_directory, FILE_CREATE_DIRECTORY | FILE_MODIFY_PERMISSIONS);
    file_prepare_directory($this->private_files_directory, FILE_CREATE_DIRECTORY);
    file_prepare_directory($this->temp_files_directory, FILE_CREATE_DIRECTORY);
    $this->generatedTestFiles = FALSE;

    // Log fatal errors.
    ini_set('log_errors', 1);
    ini_set('error_log', $this->public_files_directory . '/error.log');

    // Set the test information for use in other parts of Drupal.
    $test_info = &$GLOBALS['drupal_test_info'];
    $test_info['test_run_id'] = $this->databasePrefix;
    $test_info['in_child_site'] = FALSE;

    // Indicate the environment was set up correctly.
    $this->setupEnvironment = TRUE;
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
