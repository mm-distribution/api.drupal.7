# ShortcutSetsTestCase::testShortcutSetSwitchCreate()

- **Type:** Method
- **File:** [`modules/shortcut/shortcut.test`](../_file.md), lines 279–288 · [local source](../../../../../source/modules/shortcut/shortcut.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test#L279-L288)
- **Class:** [ShortcutSetsTestCase](../ShortcutSetsTestCase.md)
- **Module/theme:** shortcut

## Signature

```php
function testShortcutSetSwitchCreate()
```

## Documentation

```text
Tests switching a user's shortcut set and creating one at the same time.
```

## Code

```php
  function testShortcutSetSwitchCreate() {
    $edit = array(
      'set' => 'new',
      'new' => $this->randomName(10),
    );
    $this->drupalPost('user/' . $this->admin_user->uid . '/shortcuts', $edit, t('Change set'));
    $current_set = shortcut_current_displayed_set($this->admin_user);
    $this->assertNotEqual($current_set->set_name, $this->set->set_name, 'A shortcut set can be switched to at the same time as it is created.');
    $this->assertEqual($current_set->title, $edit['new'], 'The new set is correctly assigned to the user.');
  }
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.test](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test) · Licensed GPL-2.0-or-later (see LICENSE)._
