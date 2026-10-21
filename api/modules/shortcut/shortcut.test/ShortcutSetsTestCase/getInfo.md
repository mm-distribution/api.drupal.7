# ShortcutSetsTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/shortcut/shortcut.test`](../_file.md), lines 232–238 · [local source](../../../../../source/modules/shortcut/shortcut.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test#L232-L238)
- **Class:** [ShortcutSetsTestCase](../ShortcutSetsTestCase.md)
- **Module/theme:** shortcut

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
      'name' => 'Shortcut set functionality',
      'description' => 'Create, view, edit, delete, and change shortcut sets.',
      'group' => 'Shortcut',
    );
  }
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.test](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test) · Licensed GPL-2.0-or-later (see LICENSE)._
