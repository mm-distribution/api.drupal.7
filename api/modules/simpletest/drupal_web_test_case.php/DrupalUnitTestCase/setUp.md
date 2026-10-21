# DrupalUnitTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 773–823 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L773-L823)
- **Class:** [DrupalUnitTestCase](../DrupalUnitTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function setUp()
```

## Documentation

```text
Sets up unit test environment.

Unlike DrupalWebTestCase::setUp(), DrupalUnitTestCase::setUp() does not
install modules because tests are performed without accessing the database.
Any required files must be explicitly included by the child class setUp()
method.
```

## Code

```php
  protected function setUp() {
    global $conf, $language;

    // Store necessary current values before switching to the test environment.
    $this->originalFileDirectory = variable_get('file_public_path', conf_path() . '/files');
    $this->verboseDirectoryUrl = file_create_url($this->originalFileDirectory . '/simpletest/verbose');

    // Set up English language.
    $this->originalLanguage = $language;
    $this->originalLanguageDefault = variable_get('language_default');
    unset($conf['language_default']);
    $language = language_default();

    // Reset all statics so that test is performed with a clean environment.
    drupal_static_reset();

    // Generate temporary prefixed database to ensure that tests have a clean starting point.
    $this->databasePrefix = Database::getConnection()->prefixTables('{simpletest' . mt_rand(1000, 1000000) . '}');

    // Create test directory.
    $public_files_directory = $this->originalFileDirectory . '/simpletest/' . substr($this->databasePrefix, 10);
    file_prepare_directory($public_files_directory, FILE_CREATE_DIRECTORY | FILE_MODIFY_PERMISSIONS);
    $conf['file_public_path'] = $public_files_directory;

    // Clone the current connection and replace the current prefix.
    $connection_info = Database::getConnectionInfo('default');
    Database::renameConnection('default', 'simpletest_original_default');
    foreach ($connection_info as $target => $value) {
      $connection_info[$target]['prefix'] = array(
        'default' => $value['prefix']['default'] . $this->databasePrefix,
      );
    }
    Database::addConnectionInfo('default', 'default', $connection_info['default']);

    // Set user agent to be consistent with web test case.
    $_SERVER['HTTP_USER_AGENT'] = $this->databasePrefix;

    // If locale is enabled then t() will try to access the database and
    // subsequently will fail as the database is not accessible.
    $module_list = module_list();
    if (isset($module_list['locale'])) {
      // Transform the list into the format expected as input to module_list().
      foreach ($module_list as &$module) {
        $module = array('filename' => drupal_get_filename('module', $module));
      }
      $this->originalModuleList = $module_list;
      unset($module_list['locale']);
      module_list(TRUE, FALSE, FALSE, $module_list);
    }
    $this->setup = TRUE;
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
