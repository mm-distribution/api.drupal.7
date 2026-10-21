# UpdateTestContribCase::testUpdateAdminThemeSecurityUpdate()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 470–514 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L470-L514)
- **Class:** [UpdateTestContribCase](../UpdateTestContribCase.md)
- **Module/theme:** update

## Signature

```php
function testUpdateAdminThemeSecurityUpdate()
```

## Documentation

```text
Tests that the admin theme is always notified about security updates.
```

## Code

```php
  function testUpdateAdminThemeSecurityUpdate() {
    // Disable the admin theme.
    db_update('system')
      ->fields(array('status' => 0))
      ->condition('type', 'theme')
      ->condition('name', 'update_test_%', 'LIKE')
      ->execute();

    variable_set('admin_theme', 'update_test_admintheme');

    // Define the initial state for core and the themes.
    $system_info = array(
      '#all' => array(
        'version' => '7.0',
      ),
      'update_test_admintheme' => array(
        'project' => 'update_test_admintheme',
        'version' => '7.x-1.0',
        'hidden' => FALSE,
      ),
      'update_test_basetheme' => array(
        'project' => 'update_test_basetheme',
        'version' => '7.x-1.1',
        'hidden' => FALSE,
      ),
      'update_test_subtheme' => array(
        'project' => 'update_test_subtheme',
        'version' => '7.x-1.0',
        'hidden' => FALSE,
      ),
    );
    variable_set('update_test_system_info', $system_info);
    variable_set('update_check_disabled', FALSE);
    $xml_mapping = array(
      // This is enough because we don't check the update status of the admin
      // theme. We want to check that the admin theme is included in the list.
      'drupal' => '0',
    );
    $this->refreshUpdateStatus($xml_mapping);
    // The admin theme is displayed even if it's disabled.
    $this->assertText('update_test_admintheme', "The admin theme is checked for update even if it's disabled");
    // The other disabled themes are not displayed.
    $this->assertNoText('update_test_basetheme', 'Disabled theme is not checked for update in the list.');
    $this->assertNoText('update_test_subtheme', 'Disabled theme is not checked for update in the list.');
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
