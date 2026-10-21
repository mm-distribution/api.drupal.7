# UpdateCoreTestCase::testDatestampMismatch()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 124–142 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L124-L142)
- **Class:** [UpdateCoreTestCase](../UpdateCoreTestCase.md)
- **Module/theme:** update

## Signature

```php
function testDatestampMismatch()
```

## Documentation

```text
Ensures proper results where there are date mismatches among modules.
```

## Code

```php
  function testDatestampMismatch() {
    $system_info = array(
      '#all' => array(
        // We need to think we're running a -dev snapshot to see dates.
        'version' => '7.0-dev',
        'datestamp' => time(),
      ),
      'block' => array(
        // This is 2001-09-09 01:46:40 GMT, so test for "2001-Sep-".
        'datestamp' => '1000000000',
      ),
    );
    variable_set('update_test_system_info', $system_info);
    $this->refreshUpdateStatus(array('drupal' => 'dev'));
    $this->assertNoText(t('2001-Sep-'));
    $this->assertText(t('Up to date'));
    $this->assertNoText(t('Update available'));
    $this->assertNoText(t('Security update required!'));
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
