# DrupalWebTestCase::tearDown()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 1945–2028 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L1945-L2028)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function tearDown()
```

## Documentation

```text
Delete created files and temporary files directory, delete the tables created by setUp(),
and reset the database prefix.
```

## Code

```php
  protected function tearDown() {
    global $user, $language, $language_url, $theme, $theme_key, $theme_path;

    // In case a fatal error occurred that was not in the test process read the
    // log to pick up any fatal errors.
    simpletest_log_read($this->testId, $this->databasePrefix, get_class($this), TRUE);

    $emailCount = count(variable_get('drupal_test_email_collector', array()));
    if ($emailCount) {
      $message = format_plural($emailCount, '1 e-mail was sent during this test.', '@count e-mails were sent during this test.');
      $this->pass($message, t('E-mail'));
    }

    // Delete temporary files directory.
    file_unmanaged_delete_recursive($this->originalFileDirectory . '/simpletest/' . substr($this->databasePrefix, 10));

    // Remove all prefixed tables.
    $tables = db_find_tables_d8('%');
    if (empty($tables)) {
      $this->fail('Failed to find test tables to drop.');
    }
    foreach ($tables as $table) {
      if (db_drop_table($table)) {
        unset($tables[$table]);
      }
    }
    if (!empty($tables)) {
      $this->fail('Failed to drop all prefixed tables.');
    }

    // In PHP 8 some tests encounter problems when shutdown code tries to
    // access the database connection after it's been explicitly closed, for
    // example the destructor of DrupalCacheArray. We avoid this by not fully
    // destroying the test database connection.
    $close = \PHP_VERSION_ID < 80000;

    // Get back to the original connection.
    Database::removeConnection('default', $close);
    Database::renameConnection('simpletest_original_default', 'default');

    // Restore original shutdown callbacks array to prevent original
    // environment of calling handlers from test run.
    $callbacks = &drupal_register_shutdown_function();
    $callbacks = $this->originalShutdownCallbacks;

    // Return the user to the original one.
    $user = $this->originalUser;
    drupal_save_session(TRUE);

    // Ensure that internal logged in variable and cURL options are reset.
    $this->loggedInUser = FALSE;
    $this->additionalCurlOptions = array();

    // Reload module list and implementations to ensure that test module hooks
    // aren't called after tests.
    module_list(TRUE);
    module_implements('', FALSE, TRUE);

    // Reset the Field API.
    field_cache_clear();

    // Rebuild caches.
    $this->refreshVariables();

    // Reset public files directory.
    $GLOBALS['conf']['file_public_path'] = $this->originalFileDirectory;

    // Reset language.
    $language = $this->originalLanguage;
    $language_url = $this->originalLanguageUrl;
    if ($this->originalLanguageDefault) {
      $GLOBALS['conf']['language_default'] = $this->originalLanguageDefault;
    }

    // Reset theme.
    $theme = $this->originalTheme;
    $theme_key = $this->originalThemeKey;
    $theme_path = $this->originalThemePath;

    // Close the CURL handler and reset the cookies array so test classes
    // containing multiple tests are not polluted.
    $this->curlClose();
    $this->cookies = array();
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
