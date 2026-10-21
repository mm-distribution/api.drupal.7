# ShortcutSetsTestCase::testShortcutSetDelete()

- **Type:** Method
- **File:** [`modules/shortcut/shortcut.test`](../_file.md), lines 356–362 · [local source](../../../../../source/modules/shortcut/shortcut.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test#L356-L362)
- **Class:** [ShortcutSetsTestCase](../ShortcutSetsTestCase.md)
- **Module/theme:** shortcut

## Signature

```php
function testShortcutSetDelete()
```

## Documentation

```text
Tests deleting a shortcut set.
```

## Code

```php
  function testShortcutSetDelete() {
    $new_set = $this->generateShortcutSet($this->randomName(10));

    $this->drupalPost('admin/config/user-interface/shortcut/' . $new_set->set_name . '/delete', array(), t('Delete'));
    $sets = shortcut_sets();
    $this->assertFalse(isset($sets[$new_set->set_name]), 'Successfully deleted a shortcut set.');
  }
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.test](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test) · Licensed GPL-2.0-or-later (see LICENSE)._
