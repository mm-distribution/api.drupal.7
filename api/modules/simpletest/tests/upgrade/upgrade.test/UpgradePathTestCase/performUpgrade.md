# UpgradePathTestCase::performUpgrade()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.test`](../_file.md), lines 214–293 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test#L214-L293)
- **Class:** [UpgradePathTestCase](../UpgradePathTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function performUpgrade($register_errors = TRUE)
```

## Documentation

```text
Perform the upgrade.

@param $register_errors
  Register the errors during the upgrade process as failures.
@return
  TRUE if the upgrade succeeded, FALSE otherwise.
```

## Code

```php
  protected function performUpgrade($register_errors = TRUE) {
    if (!$this->zlibInstalled) {
      $this->fail(t('Missing zlib requirement for upgrade tests.'));
      return FALSE;
    }

    $update_url = $GLOBALS['base_url'] . '/update.php';

    // Load the first update screen.
    $this->drupalGet($update_url, array('external' => TRUE));
    if (!$this->assertResponse(200)) {
      return FALSE;
    }

    // Continue.
    $this->drupalPost(NULL, array(), t('Continue'));
    if (!$this->assertResponse(200)) {
      return FALSE;
    }

    // The test should pass if there are no pending updates.
    $content = $this->drupalGetContent();
    if (strpos($content, t('No pending updates.')) !== FALSE) {
      $this->pass(t('No pending updates and therefore no upgrade process to test.'));
      $this->pendingUpdates = FALSE;
      return TRUE;
    }

    // Go!
    $this->drupalPost(NULL, array(), t('Apply pending updates'));
    if (!$this->assertResponse(200)) {
      return FALSE;
    }

    // Check for errors during the update process.
    foreach ($this->xpath('//li[@class=:class]', array(':class' => 'failure')) as $element) {
      $message = strip_tags($element->asXML());
      $this->upgradeErrors[] = $message;
      if ($register_errors) {
        $this->fail($message);
      }
    }

    if (!empty($this->upgradeErrors)) {
      // Upgrade failed, the installation might be in an inconsistent state,
      // don't process.
      return FALSE;
    }

    // Check if there still are pending updates.
    $this->drupalGet($update_url, array('external' => TRUE));
    $this->drupalPost(NULL, array(), t('Continue'));
    if (!$this->assertText(t('No pending updates.'), 'No pending updates at the end of the update process.')) {
      return FALSE;
    }

    // Upgrade succeed, rebuild the environment so that we can call the API
    // of the child site directly from this request.
    $this->upgradedSite = TRUE;

    // Reload module list. For modules that are enabled in the test database,
    // but not on the test client, we need to load the code here.
    $new_modules = array_diff(module_list(TRUE), $this->loadedModules);
    foreach ($new_modules as $module) {
      drupal_load('module', $module);
    }

    // Reload hook implementations
    module_implements('', FALSE, TRUE);

    // Rebuild caches.
    drupal_static_reset();
    drupal_flush_all_caches();

    // Reload global $conf array and permissions.
    $this->refreshVariables();
    $this->checkPermissions(array(), TRUE);

    return TRUE;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test) · Licensed GPL-2.0-or-later (see LICENSE)._
