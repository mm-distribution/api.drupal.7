# ShortcutSetsTestCase::testShortcutSetDeleteDefault()

- **Type:** Method
- **File:** [`modules/shortcut/shortcut.test`](../_file.md), lines 367–370 · [local source](../../../../../source/modules/shortcut/shortcut.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test#L367-L370)
- **Class:** [ShortcutSetsTestCase](../ShortcutSetsTestCase.md)
- **Module/theme:** shortcut

## Signature

```php
function testShortcutSetDeleteDefault()
```

## Documentation

```text
Tests deleting the default shortcut set.
```

## Code

```php
  function testShortcutSetDeleteDefault() {
    $this->drupalGet('admin/config/user-interface/shortcut/' . SHORTCUT_DEFAULT_SET_NAME . '/delete');
    $this->assertResponse(403);
  }
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.test](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test) · Licensed GPL-2.0-or-later (see LICENSE)._
