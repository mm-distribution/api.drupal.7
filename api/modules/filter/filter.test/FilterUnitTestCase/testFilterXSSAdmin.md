# FilterUnitTestCase::testFilterXSSAdmin()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 1262–1272 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L1262-L1272)
- **Class:** [FilterUnitTestCase](../FilterUnitTestCase.md)
- **Module/theme:** filter

## Signature

```php
function testFilterXSSAdmin()
```

## Documentation

```text
Tests the loose, admin HTML filter.
```

## Code

```php
  function testFilterXSSAdmin() {
    // DRUPAL-SA-2008-044
    $f = filter_xss_admin('<object />');
    $this->assertNoNormalized($f, 'object', 'Admin HTML filter -- should not allow object tag.');

    $f = filter_xss_admin('<script />');
    $this->assertNoNormalized($f, 'script', 'Admin HTML filter -- should not allow script tag.');

    $f = filter_xss_admin('<style /><iframe /><frame /><frameset /><meta /><link /><embed /><applet /><param /><layer />');
    $this->assertEqual($f, '', 'Admin HTML filter -- should never allow some tags.');
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
