# FilterSecurityTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 839–845 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L839-L845)
- **Class:** [FilterSecurityTestCase](../FilterSecurityTestCase.md)
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
      'name' => 'Security',
      'description' => 'Test the behavior of check_markup() when a filter or text format vanishes.',
      'group' => 'Filter',
    );
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
