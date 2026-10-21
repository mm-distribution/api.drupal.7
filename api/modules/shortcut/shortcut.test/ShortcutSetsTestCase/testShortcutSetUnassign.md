# ShortcutSetsTestCase::testShortcutSetUnassign()

- **Type:** Method
- **File:** [`modules/shortcut/shortcut.test`](../_file.md), lines 343–351 · [local source](../../../../../source/modules/shortcut/shortcut.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test#L343-L351)
- **Class:** [ShortcutSetsTestCase](../ShortcutSetsTestCase.md)
- **Module/theme:** shortcut

## Signature

```php
function testShortcutSetUnassign()
```

## Documentation

```text
Tests unassigning a shortcut set.
```

## Code

```php
  function testShortcutSetUnassign() {
    $new_set = $this->generateShortcutSet($this->randomName(10));

    shortcut_set_assign_user($new_set, $this->shortcut_user);
    shortcut_set_unassign_user($this->shortcut_user);
    $current_set = shortcut_current_displayed_set($this->shortcut_user);
    $default_set = shortcut_default_set($this->shortcut_user);
    $this->assertTrue($current_set->set_name == $default_set->set_name, "Successfully unassigned another user's shortcut set.");
  }
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.test](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test) · Licensed GPL-2.0-or-later (see LICENSE)._
