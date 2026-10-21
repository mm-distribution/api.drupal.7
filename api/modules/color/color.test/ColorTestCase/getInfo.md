# ColorTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/color/color.test`](../_file.md), lines 16–22 · [local source](../../../../../source/modules/color/color.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.test#L16-L22)
- **Class:** [ColorTestCase](../ColorTestCase.md)
- **Module/theme:** color

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
      'name' => 'Color functionality',
      'description' => 'Modify the Bartik and Garland theme colors and make sure the changes are reflected on the frontend',
      'group' => 'Color',
    );
  }
```

---
_Drupal 7.103 · [modules/color/color.test](https://github.com/drupal/drupal/blob/7.103/modules/color/color.test) · Licensed GPL-2.0-or-later (see LICENSE)._
