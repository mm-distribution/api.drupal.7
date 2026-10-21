# UpdateTestContribCase::testUpdateShowDisabledThemes()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 519–575 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L519-L575)
- **Class:** [UpdateTestContribCase](../UpdateTestContribCase.md)
- **Module/theme:** update

## Signature

```php
function testUpdateShowDisabledThemes()
```

## Documentation

```text
Tests that disabled themes are only shown when desired.
```

## Code

```php
  function testUpdateShowDisabledThemes() {
    // Make sure all the update_test_* themes are disabled.
    db_update('system')
      ->fields(array('status' => 0))
      ->condition('type', 'theme')
      ->condition('name', 'update_test_%', 'LIKE')
      ->execute();

    // Define the initial state for core and the test contrib themes.
    $system_info = array(
      // We want core to be version 7.0.
      '#all' => array(
        'version' => '7.0',
      ),
      // The update_test_basetheme should be visible and up to date.
      'update_test_basetheme' => array(
        'project' => 'update_test_basetheme',
        'version' => '7.x-1.1',
        'hidden' => FALSE,
      ),
      // The update_test_subtheme should be visible and up to date.
      'update_test_subtheme' => array(
        'project' => 'update_test_subtheme',
        'version' => '7.x-1.0',
        'hidden' => FALSE,
      ),
    );
    // When there are contributed modules in the site's file system, the
    // total number of attempts made in the test may exceed the default value
    // of update_max_fetch_attempts. Therefore this variable is set very high
    // to avoid test failures in those cases.
    variable_set('update_max_fetch_attempts', 99999);
    variable_set('update_test_system_info', $system_info);
    $xml_mapping = array(
      'drupal' => '0',
      'update_test_subtheme' => '1_0',
      'update_test_basetheme' => '1_1-sec',
    );
    $base_theme_project_link = l(t('Update test base theme'), 'http://example.com/project/update_test_basetheme');
    $sub_theme_project_link = l(t('Update test subtheme'), 'http://example.com/project/update_test_subtheme');
    foreach (array(TRUE, FALSE) as $check_disabled) {
      variable_set('update_check_disabled', $check_disabled);
      $this->refreshUpdateStatus($xml_mapping);
      // In neither case should we see the "Themes" heading for enabled themes.
      $this->assertNoText(t('Themes'));
      if ($check_disabled) {
        $this->assertText(t('Disabled themes'));
        $this->assertRaw($base_theme_project_link, 'Link to the Update test base theme project appears.');
        $this->assertRaw($sub_theme_project_link, 'Link to the Update test subtheme project appears.');
      }
      else {
        $this->assertNoText(t('Disabled themes'));
        $this->assertNoRaw($base_theme_project_link, 'Link to the Update test base theme project does not appear.');
        $this->assertNoRaw($sub_theme_project_link, 'Link to the Update test subtheme project does not appear.');
      }
    }
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
