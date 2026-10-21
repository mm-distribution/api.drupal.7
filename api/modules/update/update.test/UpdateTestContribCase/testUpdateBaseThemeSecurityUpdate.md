# UpdateTestContribCase::testUpdateBaseThemeSecurityUpdate()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 429–465 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L429-L465)
- **Class:** [UpdateTestContribCase](../UpdateTestContribCase.md)
- **Module/theme:** update

## Signature

```php
function testUpdateBaseThemeSecurityUpdate()
```

## Documentation

```text
Tests that subthemes are notified about security updates for base themes.
```

## Code

```php
  function testUpdateBaseThemeSecurityUpdate() {
    // Only enable the subtheme, not the base theme.
    db_update('system')
      ->fields(array('status' => 1))
      ->condition('type', 'theme')
      ->condition('name', 'update_test_subtheme')
      ->execute();

    // Define the initial state for core and the subtheme.
    $system_info = array(
      // We want core to be version 7.0.
      '#all' => array(
        'version' => '7.0',
      ),
      // Show the update_test_basetheme
      'update_test_basetheme' => array(
        'project' => 'update_test_basetheme',
        'version' => '7.x-1.0',
        'hidden' => FALSE,
      ),
      // Show the update_test_subtheme
      'update_test_subtheme' => array(
        'project' => 'update_test_subtheme',
        'version' => '7.x-1.0',
        'hidden' => FALSE,
      ),
    );
    variable_set('update_test_system_info', $system_info);
    $xml_mapping = array(
      'drupal' => '0',
      'update_test_subtheme' => '1_0',
      'update_test_basetheme' => '1_1-sec',
    );
    $this->refreshUpdateStatus($xml_mapping);
    $this->assertText(t('Security update required!'));
    $this->assertRaw(l(t('Update test base theme'), 'http://example.com/project/update_test_basetheme'), 'Link to the Update test base theme project appears.');
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
