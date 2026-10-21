# SystemArchiverTest::testArchiverOutOfPath()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 3266–3269 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L3266-L3269)
- **Class:** [SystemArchiverTest](../SystemArchiverTest.md)
- **Module/theme:** system

## Signature

```php
public function testArchiverOutOfPath()
```

## Documentation

```text
Tests out-of-path extraction protection.
```

## Code

```php
  public function testArchiverOutOfPath() {
    $this->_testArchiverOutOfPath('system_test_archive_rel.tar', 'Relative out-of-path extraction caught');
    $this->_testArchiverOutOfPath('system_test_archive_abs.tgz', 'Absolute out-of-path extraction caught');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
