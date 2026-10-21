# UpdateTestContribCase::testNoReleasesAvailable()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 301–324 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L301-L324)
- **Class:** [UpdateTestContribCase](../UpdateTestContribCase.md)
- **Module/theme:** update

## Signature

```php
function testNoReleasesAvailable()
```

## Documentation

```text
Tests when there is no available release data for a contrib module.
```

## Code

```php
  function testNoReleasesAvailable() {
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
    $this->refreshUpdateStatus(array('drupal' => '0', 'aaa_update_test' => 'no-releases'));
    $this->drupalGet('admin/reports/updates');
    // Cannot use $this->standardTests() because we need to check for the
    // 'No available releases found' string.
    $this->assertRaw('<h3>' . t('Drupal core') . '</h3>');
    $this->assertRaw(l(t('Drupal'), 'http://example.com/project/drupal'));
    $this->assertText(t('Up to date'));
    $this->assertRaw('<h3>' . t('Modules') . '</h3>');
    $this->assertNoText(t('Update available'));
    $this->assertText(t('No available releases found'));
    $this->assertNoRaw(l(t('AAA Update test'), 'http://example.com/project/aaa_update_test'));
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
