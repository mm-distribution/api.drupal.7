# ThemeTableTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 173–179 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L173-L179)
- **Class:** [ThemeTableTestCase](../ThemeTableTestCase.md)
- **Module/theme:** batch_test

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
      'name' => 'Theme Table',
      'description' => 'Tests built-in theme functions.',
      'group' => 'Theme',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._
