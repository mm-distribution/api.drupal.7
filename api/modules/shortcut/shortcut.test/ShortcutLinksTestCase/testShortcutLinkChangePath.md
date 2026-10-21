# ShortcutLinksTestCase::testShortcutLinkChangePath()

- **Type:** Method
- **File:** [`modules/shortcut/shortcut.test`](../_file.md), lines 178–189 · [local source](../../../../../source/modules/shortcut/shortcut.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test#L178-L189)
- **Class:** [ShortcutLinksTestCase](../ShortcutLinksTestCase.md)
- **Module/theme:** shortcut

## Signature

```php
function testShortcutLinkChangePath()
```

## Documentation

```text
Tests that changing the path of a shortcut link works.
```

## Code

```php
  function testShortcutLinkChangePath() {
    $set = $this->set;

    // Tests changing a shortcut path.
    $new_link_path = 'admin/config';

    $this->drupalPost('admin/config/user-interface/shortcut/link/' . $set->links[0]['mlid'], array('shortcut_link[link_title]' => $set->links[0]['link_title'], 'shortcut_link[link_path]' => $new_link_path), t('Save'));
    $saved_set = shortcut_set_load($set->set_name);
    $paths = $this->getShortcutInformation($saved_set, 'link_path');
    $this->assertTrue(in_array($new_link_path, $paths), 'Shortcut path changed: ' . $new_link_path);
    $this->assertLinkByHref($new_link_path, 0, 'Shortcut with new path appears on the page.');
  }
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.test](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test) · Licensed GPL-2.0-or-later (see LICENSE)._
