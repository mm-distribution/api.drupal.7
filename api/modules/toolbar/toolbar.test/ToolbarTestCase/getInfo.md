# ToolbarTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/toolbar/toolbar.test`](../_file.md), lines 7–13 · [local source](../../../../../source/modules/toolbar/toolbar.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.test#L7-L13)
- **Class:** [ToolbarTestCase](../ToolbarTestCase.md)
- **Module/theme:** toolbar

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
      'name' => 'Toolbar',
      'description' => 'Test toolbar functionality.',
      'group' => 'Toolbar (core)',
    );
  }
```

---
_Drupal 7.103 · [modules/toolbar/toolbar.test](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.test) · Licensed GPL-2.0-or-later (see LICENSE)._
