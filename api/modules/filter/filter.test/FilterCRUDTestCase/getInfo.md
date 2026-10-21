# FilterCRUDTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 12–18 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L12-L18)
- **Class:** [FilterCRUDTestCase](../FilterCRUDTestCase.md)
- **Module/theme:** filter

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Filter CRUD operations',
      'description' => 'Test creation, loading, updating, deleting of text formats and filters.',
      'group' => 'Filter',
    );
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
