# ShortcutTestCase::generateShortcutLink()

- **Type:** Method
- **File:** [`modules/shortcut/shortcut.test`](../_file.md), lines 67–74 · [local source](../../../../../source/modules/shortcut/shortcut.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test#L67-L74)
- **Class:** [ShortcutTestCase](../ShortcutTestCase.md)
- **Module/theme:** shortcut

## Signature

```php
function generateShortcutLink($path, $title = '')
```

## Documentation

```text
Creates a generic shortcut link.
```

## Code

```php
  function generateShortcutLink($path, $title = '') {
    $link = array(
      'link_path' => $path,
      'link_title' => !empty($title) ? $title : $this->randomName(10),
    );

    return $link;
  }
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.test](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test) · Licensed GPL-2.0-or-later (see LICENSE)._
