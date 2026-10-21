# ShortcutTestCase::getShortcutInformation()

- **Type:** Method
- **File:** [`modules/shortcut/shortcut.test`](../_file.md), lines 90–96 · [local source](../../../../../source/modules/shortcut/shortcut.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test#L90-L96)
- **Class:** [ShortcutTestCase](../ShortcutTestCase.md)
- **Module/theme:** shortcut

## Signature

```php
function getShortcutInformation($set, $key)
```

## Documentation

```text
Extracts information from shortcut set links.

@param object $set
  The shortcut set object to extract information from.
@param string $key
  The array key indicating what information to extract from each link:
   - 'link_path': Extract link paths.
   - 'link_title': Extract link titles.
   - 'mlid': Extract the menu link item ID numbers.

@return array
  Array of the requested information from each link.
```

## Code

```php
  function getShortcutInformation($set, $key) {
    $info = array();
    foreach ($set->links as $link) {
      $info[] = $link[$key];
    }
    return $info;
  }
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.test](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.test) · Licensed GPL-2.0-or-later (see LICENSE)._
