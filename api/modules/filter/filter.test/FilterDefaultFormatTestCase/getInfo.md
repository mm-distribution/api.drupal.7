# FilterDefaultFormatTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 742–748 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L742-L748)
- **Class:** [FilterDefaultFormatTestCase](../FilterDefaultFormatTestCase.md)
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
      'name' => 'Default text format functionality',
      'description' => 'Test the default text formats for different users.',
      'group' => 'Filter',
    );
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
