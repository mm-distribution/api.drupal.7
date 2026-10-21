# ShortcutSetsTestCase::testShortcutSetRename()

- **Type:** Method
- **File:** [`modules/shortcut/shortcut.test`](../_file.md), lines 319–326 · [local source](../../../../../source/modules/shortcut/shortcut.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test#L319-L326)
- **Class:** [ShortcutSetsTestCase](../ShortcutSetsTestCase.md)
- **Module/theme:** shortcut

## Signature

```php
function testShortcutSetRename()
```

## Documentation

```text
Tests renaming a shortcut set.
```

## Code

```php
  function testShortcutSetRename() {
    $set = $this->set;
    
    $new_title = $this->randomName(10);
    $this->drupalPost('admin/config/user-interface/shortcut/' . $set->set_name . '/edit', array('title' => $new_title), t('Save'));
    $set = shortcut_set_load($set->set_name);
    $this->assertTrue($set->title == $new_title, 'Shortcut set has been successfully renamed.');
  }
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.test](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test) · Licensed GPL-2.0-or-later (see LICENSE)._
