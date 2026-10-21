# UpdateTestContribCase::testUpdateContribBasic()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 329–352 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L329-L352)
- **Class:** [UpdateTestContribCase](../UpdateTestContribCase.md)
- **Module/theme:** update

## Signature

```php
function testUpdateContribBasic()
```

## Documentation

```text
Tests the basic functionality of a contrib module on the status report.
```

## Code

```php
  function testUpdateContribBasic() {
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
    $this->refreshUpdateStatus(
      array(
        'drupal' => '0',
        'aaa_update_test' => '1_0',
      )
    );
    $this->standardTests();
    $this->assertText(t('Up to date'));
    $this->assertRaw('<h3>' . t('Modules') . '</h3>');
    $this->assertNoText(t('Update available'));
    $this->assertRaw(l(t('AAA Update test'), 'http://example.com/project/aaa_update_test'), 'Link to aaa_update_test project appears.');
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
