# ShortcutLinksTestCase::testShortcutQuickLink()

- **Type:** Method
- **File:** [`modules/shortcut/shortcut.test`](../_file.md), lines 154–157 · [local source](../../../../../source/modules/shortcut/shortcut.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test#L154-L157)
- **Class:** [ShortcutLinksTestCase](../ShortcutLinksTestCase.md)
- **Module/theme:** shortcut

## Signature

```php
function testShortcutQuickLink()
```

## Documentation

```text
Tests that the "add to shortcut" link changes to "remove shortcut".
```

## Code

```php
  function testShortcutQuickLink() {
    $this->drupalGet($this->set->links[0]['link_path']);
    $this->assertRaw(t('Remove from %title shortcuts', array('%title' => $this->set->title)), '"Add to shortcuts" link properly switched to "Remove from shortcuts".');
  }
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.test](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test) · Licensed GPL-2.0-or-later (see LICENSE)._
