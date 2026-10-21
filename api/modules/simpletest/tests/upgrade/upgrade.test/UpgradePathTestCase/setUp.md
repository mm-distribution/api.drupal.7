# UpgradePathTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.test`](../_file.md), lines 87–165 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test#L87-L165)
- **Class:** [UpgradePathTestCase](../UpgradePathTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function setUp()
```

## Documentation

```text
Overrides DrupalWebTestCase::setUp() for upgrade testing.

@see DrupalWebTestCase::prepareDatabasePrefix()
@see DrupalWebTestCase::changeDatabasePrefix()
@see DrupalWebTestCase::prepareEnvironment()
```

## Code

```php
  protected function setUp() {
    // We are going to set a missing zlib requirement property for usage
    // during the performUpgrade() and tearDown() methods. Also set that the
    // tests failed.
    if (!$this->zlibInstalled) {
      parent::setUp();
      return;
    }

    global $user, $language, $conf;

    // Load the Update API.
    require_once DRUPAL_ROOT . '/includes/update.inc';

    // Reset flags.
    $this->upgradedSite = FALSE;
    $this->upgradeErrors = array();

    $this->loadedModules = module_list();

    // Create the database prefix for this test.
    $this->prepareDatabasePrefix();

    // Prepare the environment for running tests.
    $this->prepareEnvironment();
    if (!$this->setupEnvironment) {
      return FALSE;
    }

    // Reset all statics and variables to perform tests in a clean environment.
    $conf = array();
    drupal_static_reset();

    // Change the database prefix.
    // All static variables need to be reset before the database prefix is
    // changed, since DrupalCacheArray implementations attempt to
    // write back to persistent caches when they are destructed.
    $this->changeDatabasePrefix();
    if (!$this->setupDatabasePrefix) {
      return FALSE;
    }

    // Unregister the registry.
    // This is required to make sure that the database layer works properly.
    spl_autoload_unregister('drupal_autoload_class');
    spl_autoload_unregister('drupal_autoload_interface');

    // Load the database from the portable PHP dump.
    // The files may be gzipped.
    foreach ($this->databaseDumpFiles as $file) {
      if (substr($file, -3) == '.gz') {
        $file = "compress.zlib://$file";
      }
      require $file;
    }

    // Set path variables.
    $this->variable_set('file_public_path', $this->public_files_directory);
    $this->variable_set('file_private_path', $this->private_files_directory);
    $this->variable_set('file_temporary_path', $this->temp_files_directory);

    $this->pass('Finished loading the dump.');

    // Ensure that the session is not written to the new environment and replace
    // the global $user session with uid 1 from the new test site.
    drupal_save_session(FALSE);
    // Login as uid 1.
    $user = db_query('SELECT * FROM {users} WHERE uid = :uid', array(':uid' => 1))->fetchObject();

    // Generate and set a D6-compatible session cookie.
    $this->prepareD7Session();

    // Restore necessary variables.
    $this->variable_set('clean_url', $this->originalCleanUrl);
    $this->variable_set('site_mail', 'simpletest@example.com');

    drupal_set_time_limit($this->timeLimit);
    $this->setup = TRUE;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test) · Licensed GPL-2.0-or-later (see LICENSE)._
