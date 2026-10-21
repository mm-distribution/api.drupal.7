# HelpTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/help/help.test`](../_file.md), lines 27–33 · [local source](../../../../../source/modules/help/help.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/help/help.test#L27-L33)
- **Class:** [HelpTestCase](../HelpTestCase.md)
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
      'name' => 'Help functionality',
      'description' => 'Verify help display and user access to help based on permissions.',
      'group' => 'Help',
    );
  }
```

---
_Drupal 7.103 · [modules/help/help.test](https://github.com/drupal/drupal/blob/7.103/modules/help/help.test) · Licensed GPL-2.0-or-later (see LICENSE)._
