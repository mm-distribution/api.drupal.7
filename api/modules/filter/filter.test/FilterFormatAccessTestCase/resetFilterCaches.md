# FilterFormatAccessTestCase::resetFilterCaches()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 732–735 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L732-L735)
- **Class:** [FilterFormatAccessTestCase](../FilterFormatAccessTestCase.md)
- **Module/theme:** filter

## Signature

```php
protected function resetFilterCaches()
```

## Documentation

```text
Rebuilds text format and permission caches in the thread running the tests.
```

## Code

```php
  protected function resetFilterCaches() {
    filter_formats_reset();
    $this->checkPermissions(array(), TRUE);
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
