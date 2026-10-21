# ShortcutSetsTestCase::testShortcutSetRenameAlreadyExists()

- **Type:** Method
- **File:** [`modules/shortcut/shortcut.test`](../_file.md), lines 331–338 · [local source](../../../../../source/modules/shortcut/shortcut.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test#L331-L338)
- **Class:** [ShortcutSetsTestCase](../ShortcutSetsTestCase.md)
- **Module/theme:** shortcut

## Signature

```php
function testShortcutSetRenameAlreadyExists()
```

## Documentation

```text
Tests renaming a shortcut set to the same name as another set.
```

## Code

```php
  function testShortcutSetRenameAlreadyExists() {
    $set = $this->generateShortcutSet($this->randomName(10));
    $existing_title = $this->set->title;
    $this->drupalPost('admin/config/user-interface/shortcut/' . $set->set_name . '/edit', array('title' => $existing_title), t('Save'));
    $this->assertRaw(t('The shortcut set %name already exists. Choose another name.', array('%name' => $existing_title)));
    $set = shortcut_set_load($set->set_name);
    $this->assertNotEqual($set->title, $existing_title, format_string('The shortcut set %title cannot be renamed to %new-title because a shortcut set with that title already exists.', array('%title' => $set->title, '%new-title' => $existing_title)));
  }
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.test](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test) · Licensed GPL-2.0-or-later (see LICENSE)._
