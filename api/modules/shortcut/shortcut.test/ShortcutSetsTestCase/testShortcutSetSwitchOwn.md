# ShortcutSetsTestCase::testShortcutSetSwitchOwn()

- **Type:** Method
- **File:** [`modules/shortcut/shortcut.test`](../_file.md), lines 254–263 · [local source](../../../../../source/modules/shortcut/shortcut.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test#L254-L263)
- **Class:** [ShortcutSetsTestCase](../ShortcutSetsTestCase.md)
- **Module/theme:** shortcut

## Signature

```php
function testShortcutSetSwitchOwn()
```

## Documentation

```text
Tests switching a user's own shortcut set.
```

## Code

```php
  function testShortcutSetSwitchOwn() {
    $new_set = $this->generateShortcutSet($this->randomName(10));

    // Attempt to switch the default shortcut set to the newly created shortcut
    // set.
    $this->drupalPost('user/' . $this->admin_user->uid . '/shortcuts', array('set' => $new_set->set_name), t('Change set'));
    $this->assertResponse(200);
    $current_set = shortcut_current_displayed_set($this->admin_user);
    $this->assertTrue($new_set->set_name == $current_set->set_name, 'Successfully switched own shortcut set.');
  }
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.test](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test) · Licensed GPL-2.0-or-later (see LICENSE)._
