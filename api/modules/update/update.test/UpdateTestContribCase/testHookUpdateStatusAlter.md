# UpdateTestContribCase::testHookUpdateStatusAlter()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 641–691 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L641-L691)
- **Class:** [UpdateTestContribCase](../UpdateTestContribCase.md)
- **Module/theme:** update

## Signature

```php
function testHookUpdateStatusAlter()
```

## Documentation

```text
Checks that hook_update_status_alter() works to change a status.

We provide the same external data as if aaa_update_test 7.x-1.0 were
installed and that was the latest release. Then we use
hook_update_status_alter() to try to mark this as missing a security
update, then assert if we see the appropriate warnings on the right pages.
```

## Code

```php
  function testHookUpdateStatusAlter() {
    variable_set('allow_authorize_operations', TRUE);
    $update_admin_user = $this->drupalCreateUser(array('administer site configuration', 'administer software updates'));
    $this->drupalLogin($update_admin_user);

    $system_info = array(
      '#all' => array(
        'version' => '7.0',
      ),
      'aaa_update_test' => array(
        'project' => 'aaa_update_test',
        'version' => '7.x-1.0',
        'hidden' => FALSE,
      ),
    );
    variable_set('update_test_system_info', $system_info);
    $update_status = array(
      'aaa_update_test' => array(
        'status' => UPDATE_NOT_SECURE,
      ),
    );
    variable_set('update_test_update_status', $update_status);
    $this->refreshUpdateStatus(
      array(
        'drupal' => '0',
        'aaa_update_test' => '1_0',
      )
    );
    $this->drupalGet('admin/reports/updates');
    $this->assertRaw('<h3>' . t('Modules') . '</h3>');
    $this->assertText(t('Security update required!'));
    $this->assertRaw(l(t('AAA Update test'), 'http://example.com/project/aaa_update_test'), 'Link to aaa_update_test project appears.');

    // Visit the reports page again without the altering and make sure the
    // status is back to normal.
    variable_set('update_test_update_status', array());
    $this->drupalGet('admin/reports/updates');
    $this->assertRaw('<h3>' . t('Modules') . '</h3>');
    $this->assertNoText(t('Security update required!'));
    $this->assertRaw(l(t('AAA Update test'), 'http://example.com/project/aaa_update_test'), 'Link to aaa_update_test project appears.');

    // Turn the altering back on and visit the Update manager UI.
    variable_set('update_test_update_status', $update_status);
    $this->drupalGet('admin/modules/update');
    $this->assertText(t('Security update'));

    // Turn the altering back off and visit the Update manager UI.
    variable_set('update_test_update_status', array());
    $this->drupalGet('admin/modules/update');
    $this->assertNoText(t('Security update'));
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
