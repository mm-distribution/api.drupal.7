# UpdateTestContribCase::testUpdateBrokenFetchURL()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 580–631 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L580-L631)
- **Class:** [UpdateTestContribCase](../UpdateTestContribCase.md)
- **Module/theme:** update

## Signature

```php
function testUpdateBrokenFetchURL()
```

## Documentation

```text
Makes sure that if we fetch from a broken URL, sane things happen.
```

## Code

```php
  function testUpdateBrokenFetchURL() {
    $system_info = array(
      '#all' => array(
        'version' => '7.0',
      ),
      'aaa_update_test' => array(
        'project' => 'aaa_update_test',
        'version' => '7.x-1.0',
        'hidden' => FALSE,
      ),
      'bbb_update_test' => array(
        'project' => 'bbb_update_test',
        'version' => '7.x-1.0',
        'hidden' => FALSE,
      ),
      'ccc_update_test' => array(
        'project' => 'ccc_update_test',
        'version' => '7.x-1.0',
        'hidden' => FALSE,
      ),
    );
    variable_set('update_test_system_info', $system_info);

    $xml_mapping = array(
      'drupal' => '0',
      'aaa_update_test' => '1_0',
      'bbb_update_test' => 'does-not-exist',
      'ccc_update_test' => '1_0',
    );
    $this->refreshUpdateStatus($xml_mapping);

    $this->assertText(t('Up to date'));
    // We're expecting the report to say most projects are up to date, so we
    // hope that 'Up to date' is not unique.
    $this->assertNoUniqueText(t('Up to date'));
    // It should say we failed to get data, not that we're missing an update.
    $this->assertNoText(t('Update available'));

    // We need to check that this string is found as part of a project row,
    // not just in the "Failed to get available update data for ..." message
    // at the top of the page.
    $this->assertRaw('<div class="version-status">' . t('Failed to get available update data'));

    // We should see the output messages from fetching manually.
    $this->assertUniqueText(t('Checked available update data for 3 projects.'));
    $this->assertUniqueText(t('Failed to get available update data for one project.'));

    // The other two should be listed as projects.
    $this->assertRaw(l(t('AAA Update test'), 'http://example.com/project/aaa_update_test'), 'Link to aaa_update_test project appears.');
    $this->assertNoRaw(l(t('BBB Update test'), 'http://example.com/project/bbb_update_test'), 'Link to bbb_update_test project does not appear.');
    $this->assertRaw(l(t('CCC Update test'), 'http://example.com/project/ccc_update_test'), 'Link to bbb_update_test project appears.');
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
