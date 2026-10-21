# ThemeHookInitTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 408–414 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L408-L414)
- **Class:** [ThemeHookInitTestCase](../ThemeHookInitTestCase.md)
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
      'name' => 'Theme initialization in hook_init()',
      'description' => 'Tests that the theme system can be correctly initialized in hook_init().',
      'group' => 'Theme',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._
