# UpdateCoreTestCase::testNoUpdatesAvailable()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 82–89 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L82-L89)
- **Class:** [UpdateCoreTestCase](../UpdateCoreTestCase.md)
- **Module/theme:** update

## Signature

```php
function testNoUpdatesAvailable()
```

## Documentation

```text
Tests the Update Manager module when no updates are available.
```

## Code

```php
  function testNoUpdatesAvailable() {
    $this->setSystemInfo7_0();
    $this->refreshUpdateStatus(array('drupal' => '0'));
    $this->standardTests();
    $this->assertText(t('Up to date'));
    $this->assertNoText(t('Update available'));
    $this->assertNoText(t('Security update required!'));
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
