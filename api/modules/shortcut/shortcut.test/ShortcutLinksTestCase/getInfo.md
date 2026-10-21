# ShortcutLinksTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/shortcut/shortcut.test`](../_file.md), lines 104–110 · [local source](../../../../../source/modules/shortcut/shortcut.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test#L104-L110)
- **Class:** [ShortcutLinksTestCase](../ShortcutLinksTestCase.md)
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
      'name' => 'Shortcut link functionality',
      'description' => 'Create, view, edit, delete, and change shortcut links.',
      'group' => 'Shortcut',
    );
  }
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.test](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test) · Licensed GPL-2.0-or-later (see LICENSE)._
