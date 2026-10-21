# FilterFormatAccessTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 473–479 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L473-L479)
- **Class:** [FilterFormatAccessTestCase](../FilterFormatAccessTestCase.md)
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
      'name' => 'Filter format access',
      'description' => 'Tests access to text formats.',
      'group' => 'Filter',
    );
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
