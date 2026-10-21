# shortcut_set_reset_link_weights()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 425–431 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L425-L431)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_set_reset_link_weights(&$shortcut_set)
```

## Documentation

```text
Resets the link weights in a shortcut set to match their current order.

This function can be used, for example, when a new shortcut link is added to
the set. If the link is added to the end of the array and this function is
called, it will force that link to display at the end of the list.

@param object $shortcut_set
  An object representing a shortcut set. The link weights of the passed-in
  object will be reset as described above.
```

## Code

```php
function shortcut_set_reset_link_weights(&$shortcut_set) {
  $weight = -50;
  foreach ($shortcut_set->links as &$link) {
    $link['weight'] = $weight;
    $weight++;
  }
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
