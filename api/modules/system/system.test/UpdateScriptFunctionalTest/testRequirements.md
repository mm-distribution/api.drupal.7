# UpdateScriptFunctionalTest::testRequirements()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2573–2626 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2573-L2626)
- **Class:** [UpdateScriptFunctionalTest](../UpdateScriptFunctionalTest.md)
- **Module/theme:** system

## Signature

```php
function testRequirements()
```

## Documentation

```text
Tests that requirements warnings and errors are correctly displayed.
```

## Code

```php
  function testRequirements() {
    $this->drupalLogin($this->update_user);

    // If there are no requirements warnings or errors, we expect to be able to
    // go through the update process uninterrupted.
    $this->drupalGet($this->update_url, array('external' => TRUE));
    $this->drupalPost(NULL, array(), t('Continue'));
    $this->assertText(t('No pending updates.'), 'End of update process was reached.');
    // Confirm that all caches were cleared.
    $this->assertText(t('hook_flush_caches() invoked for update_script_test.module.'), 'Caches were cleared when there were no requirements warnings or errors.');

    // If there is a requirements warning, we expect it to be initially
    // displayed, but clicking the link to proceed should allow us to go
    // through the rest of the update process uninterrupted.

    // First, run this test with pending updates to make sure they can be run
    // successfully.
    variable_set('update_script_test_requirement_type', REQUIREMENT_WARNING);
    drupal_set_installed_schema_version('update_script_test', drupal_get_installed_schema_version('update_script_test') - 1);
    $this->drupalGet($this->update_url, array('external' => TRUE));
    $this->assertText('This is a requirements warning provided by the update_script_test module.');
    $this->clickLink('try again');
    $this->assertNoText('This is a requirements warning provided by the update_script_test module.');
    $this->drupalPost(NULL, array(), t('Continue'));
    $this->drupalPost(NULL, array(), t('Apply pending updates'));
    $this->assertText(t('The update_script_test_update_7000() update was executed successfully.'), 'End of update process was reached.');
    // Confirm that all caches were cleared.
    $this->assertText(t('hook_flush_caches() invoked for update_script_test.module.'), 'Caches were cleared after resolving a requirements warning and applying updates.');

    // Now try again without pending updates to make sure that works too.
    $this->drupalGet($this->update_url, array('external' => TRUE));
    $this->assertText('This is a requirements warning provided by the update_script_test module.');
    $this->clickLink('try again');
    $this->assertNoText('This is a requirements warning provided by the update_script_test module.');
    $this->drupalPost(NULL, array(), t('Continue'));
    $this->assertText(t('No pending updates.'), 'End of update process was reached.');
    // Confirm that all caches were cleared.
    $this->assertText(t('hook_flush_caches() invoked for update_script_test.module.'), 'Caches were cleared after applying updates and re-running the script.');

    // If there is a requirements error, it should be displayed even after
    // clicking the link to proceed (since the problem that triggered the error
    // has not been fixed).
    variable_set('update_script_test_requirement_type', REQUIREMENT_ERROR);
    $this->drupalGet($this->update_url, array('external' => TRUE));
    $this->assertText('This is a requirements error provided by the update_script_test module.');
    $this->clickLink('try again');
    $this->assertText('This is a requirements error provided by the update_script_test module.');

    // Check if the optional 'value' key displays without a notice.
    variable_set('update_script_test_requirement_type', REQUIREMENT_INFO);
    $this->drupalGet($this->update_url, array('external' => TRUE));
    $this->assertText('This is a requirements info provided by the update_script_test module.');
    $this->assertNoText('Notice: Undefined index: value in theme_status_report()');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
