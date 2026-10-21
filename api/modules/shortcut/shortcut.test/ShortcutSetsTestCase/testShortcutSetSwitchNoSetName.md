# ShortcutSetsTestCase::testShortcutSetSwitchNoSetName()

- **Type:** Method
- **File:** [`modules/shortcut/shortcut.test`](../_file.md), lines 293–299 · [local source](../../../../../source/modules/shortcut/shortcut.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test#L293-L299)
- **Class:** [ShortcutSetsTestCase](../ShortcutSetsTestCase.md)
- **Module/theme:** shortcut

## Signature

```php
function testShortcutSetSwitchNoSetName()
```

## Documentation

```text
Tests switching a user's shortcut set without providing a new set name.
```

## Code

```php
  function testShortcutSetSwitchNoSetName() {
    $edit = array('set' => 'new');
    $this->drupalPost('user/' . $this->admin_user->uid . '/shortcuts', $edit, t('Change set'));
    $this->assertText(t('The new set name is required.'));
    $current_set = shortcut_current_displayed_set($this->admin_user);
    $this->assertEqual($current_set->set_name, $this->set->set_name, 'Attempting to switch to a new shortcut set without providing a set name does not succeed.');
  }
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.test](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test) · Licensed GPL-2.0-or-later (see LICENSE)._
