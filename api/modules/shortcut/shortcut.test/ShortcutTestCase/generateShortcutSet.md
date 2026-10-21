# ShortcutTestCase::generateShortcutSet()

- **Type:** Method
- **File:** [`modules/shortcut/shortcut.test`](../_file.md), lines 51–62 · [local source](../../../../../source/modules/shortcut/shortcut.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test#L51-L62)
- **Class:** [ShortcutTestCase](../ShortcutTestCase.md)
- **Module/theme:** shortcut

## Signature

```php
function generateShortcutSet($title = '', $default_links = TRUE)
```

## Documentation

```text
Creates a generic shortcut set.
```

## Code

```php
  function generateShortcutSet($title = '', $default_links = TRUE) {
    $set = new stdClass();
    $set->title = empty($title) ? $this->randomName(10) : $title;
    if ($default_links) {
      $set->links = array();
      $set->links[] = $this->generateShortcutLink('node/add');
      $set->links[] = $this->generateShortcutLink('admin/content');
    }
    shortcut_set_save($set);

    return $set;
  }
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.test](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test) · Licensed GPL-2.0-or-later (see LICENSE)._
