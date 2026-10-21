# ShortcutSetsTestCase::testShortcutSetAssign()

- **Type:** Method
- **File:** [`modules/shortcut/shortcut.test`](../_file.md), lines 268–274 · [local source](../../../../../source/modules/shortcut/shortcut.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test#L268-L274)
- **Class:** [ShortcutSetsTestCase](../ShortcutSetsTestCase.md)
- **Module/theme:** shortcut

## Signature

```php
function testShortcutSetAssign()
```

## Documentation

```text
Tests switching another user's shortcut set.
```

## Code

```php
  function testShortcutSetAssign() {
    $new_set = $this->generateShortcutSet($this->randomName(10));

    shortcut_set_assign_user($new_set, $this->shortcut_user);
    $current_set = shortcut_current_displayed_set($this->shortcut_user);
    $this->assertTrue($new_set->set_name == $current_set->set_name, "Successfully switched another user's shortcut set.");
  }
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.test](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test) · Licensed GPL-2.0-or-later (see LICENSE)._
