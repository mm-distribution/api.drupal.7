# shortcut_admin_add_link()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.admin.inc`](_file.md), lines 566–591 · [local source](../../../../source/modules/shortcut/shortcut.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc#L566-L591)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_admin_add_link($shortcut_link, &$shortcut_set, $limit = NULL)
```

## Documentation

```text
Adds a link to the end of a shortcut set, keeping within a prescribed limit.

@param $link
  An array representing a shortcut link.
@param $shortcut_set
  An object representing the shortcut set which the link will be added to.
  The links in the shortcut set will be re-weighted so that the new link is
  at the end, and some existing links may be disabled (if the $limit
  parameter is provided).
@param $limit
  (optional) The maximum number of links that are allowed to be enabled for
  this shortcut set. If provided, existing links at the end of the list that
  exceed the limit will be automatically disabled. If not provided, no limit
  will be enforced.
```

## Code

```php
function shortcut_admin_add_link($shortcut_link, &$shortcut_set, $limit = NULL) {
  if (isset($limit)) {
    // Disable any existing links at the end of the list that would cause the
    // limit to be exceeded. Take into account whether or not the new link will
    // be enabled and count towards the total.
    $number_enabled = !empty($shortcut_link['hidden']) ? 0 : 1;
    foreach ($shortcut_set->links as &$link) {
      if (!$link['hidden']) {
        $number_enabled++;
        if ($number_enabled > $limit) {
          $link['hidden'] = 1;
        }
      }
    }
  }

  // Normalize the path in case it is an alias.
  $shortcut_link['link_path'] = drupal_get_normal_path($shortcut_link['link_path']);
  if (empty($shortcut_link['link_path'])) {
    $shortcut_link['link_path'] = '<front>';
  }

  // Add the link to the end of the list.
  $shortcut_set->links[] = $shortcut_link;
  shortcut_set_reset_link_weights($shortcut_set);
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
