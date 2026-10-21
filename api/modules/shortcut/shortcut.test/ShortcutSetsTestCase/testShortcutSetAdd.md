# ShortcutSetsTestCase::testShortcutSetAdd()

- **Type:** Method
- **File:** [`modules/shortcut/shortcut.test`](../_file.md), lines 243–249 · [local source](../../../../../source/modules/shortcut/shortcut.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test#L243-L249)
- **Class:** [ShortcutSetsTestCase](../ShortcutSetsTestCase.md)
- **Module/theme:** shortcut

## Signature

```php
function testShortcutSetAdd()
```

## Documentation

```text
Tests creating a shortcut set.
```

## Code

```php
  function testShortcutSetAdd() {
    $new_set = $this->generateShortcutSet($this->randomName(10));
    $sets = shortcut_sets();
    $this->assertTrue(isset($sets[$new_set->set_name]), 'Successfully created a shortcut set.');
    $this->drupalGet('user/' . $this->admin_user->uid . '/shortcuts');
    $this->assertText($new_set->title, 'Generated shortcut set was listed as a choice on the user account page.');
  }
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.test](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test) · Licensed GPL-2.0-or-later (see LICENSE)._
