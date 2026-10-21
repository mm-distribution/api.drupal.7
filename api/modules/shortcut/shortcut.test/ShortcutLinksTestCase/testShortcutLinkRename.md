# ShortcutLinksTestCase::testShortcutLinkRename()

- **Type:** Method
- **File:** [`modules/shortcut/shortcut.test`](../_file.md), lines 162–173 · [local source](../../../../../source/modules/shortcut/shortcut.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test#L162-L173)
- **Class:** [ShortcutLinksTestCase](../ShortcutLinksTestCase.md)
- **Module/theme:** shortcut

## Signature

```php
function testShortcutLinkRename()
```

## Documentation

```text
Tests that shortcut links can be renamed.
```

## Code

```php
  function testShortcutLinkRename() {
    $set = $this->set;

    // Attempt to rename shortcut link.
    $new_link_name = $this->randomName(10);

    $this->drupalPost('admin/config/user-interface/shortcut/link/' . $set->links[0]['mlid'], array('shortcut_link[link_title]' => $new_link_name, 'shortcut_link[link_path]' => $set->links[0]['link_path']), t('Save'));
    $saved_set = shortcut_set_load($set->set_name);
    $titles = $this->getShortcutInformation($saved_set, 'link_title');
    $this->assertTrue(in_array($new_link_name, $titles), 'Shortcut renamed: ' . $new_link_name);
    $this->assertLink($new_link_name, 0, 'Renamed shortcut link appears on the page.');
  }
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.test](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test) · Licensed GPL-2.0-or-later (see LICENSE)._
