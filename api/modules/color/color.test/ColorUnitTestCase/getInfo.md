# ColorUnitTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/color/color.test`](../_file.md), lines 145–151 · [local source](../../../../../source/modules/color/color.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.test#L145-L151)
- **Class:** [ColorUnitTestCase](../ColorUnitTestCase.md)
- **Module/theme:** color

## Signature

```php
public static function getInfo()
```

## Documentation

```text
{@inheritdoc}
```

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Color module unit tests',
      'description' => 'Test color.module functionality.',
      'group' => 'Color',
    );
  }
```

---
_Drupal 7.103 · [modules/color/color.test](https://github.com/drupal/drupal/blob/7.103/modules/color/color.test) · Licensed GPL-2.0-or-later (see LICENSE)._
