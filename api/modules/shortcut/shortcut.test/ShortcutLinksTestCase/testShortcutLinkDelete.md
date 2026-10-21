# ShortcutLinksTestCase::testShortcutLinkDelete()

- **Type:** Method
- **File:** [`modules/shortcut/shortcut.test`](../_file.md), lines 194–201 · [local source](../../../../../source/modules/shortcut/shortcut.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test#L194-L201)
- **Class:** [ShortcutLinksTestCase](../ShortcutLinksTestCase.md)
- **Module/theme:** shortcut

## Signature

```php
function testShortcutLinkDelete()
```

## Documentation

```text
Tests deleting a shortcut link.
```

## Code

```php
  function testShortcutLinkDelete() {
    $set = $this->set;

    $this->drupalPost('admin/config/user-interface/shortcut/link/' . $set->links[0]['mlid'] . '/delete', array(), 'Delete');
    $saved_set = shortcut_set_load($set->set_name);
    $mlids = $this->getShortcutInformation($saved_set, 'mlid');
    $this->assertFalse(in_array($set->links[0]['mlid'], $mlids), 'Successfully deleted a shortcut.');
  }
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.test](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test) · Licensed GPL-2.0-or-later (see LICENSE)._
