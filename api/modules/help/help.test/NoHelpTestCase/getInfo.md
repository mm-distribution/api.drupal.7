# NoHelpTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/help/help.test`](../_file.md), lines 119–125 · [local source](../../../../../source/modules/help/help.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/help/help.test#L119-L125)
- **Class:** [NoHelpTestCase](../NoHelpTestCase.md)
- **Module/theme:** help

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
      'name' => 'No help',
      'description' => 'Verify no help is displayed for modules not providing any help.',
      'group' => 'Help',
    );
  }
```

---
_Drupal 7.103 · [modules/help/help.test](https://github.com/drupal/drupal/blob/7.103/modules/help/help.test) · Licensed GPL-2.0-or-later (see LICENSE)._
