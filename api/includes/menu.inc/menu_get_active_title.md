# menu_get_active_title()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 2641–2669 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L2641-L2669)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_get_active_title()
```

## Documentation

```text
Gets the title of the current page, as determined by the active trail.
```

## Code

```php
function menu_get_active_title() {
  $active_trail = menu_get_active_trail();
  $local_task_title = NULL;

  foreach (array_reverse($active_trail) as $item) {
    // Local task titles are displayed as tabs and therefore should not be
    // repeated as the page title. However, if the local task appears in a
    // top-level menu, it is no longer a "local task" anymore (the front page
    // of the site does not have tabs) so it is better to use the local task
    // title in that case than to fall back on the front page link in the
    // active trail (which is usually "Home" and would not make sense in this
    // context).
    if ((bool) ($item['type'] & MENU_IS_LOCAL_TASK)) {
      // A local task title is being skipped; track it in case it needs to be
      // used later.
      $local_task_title = $item['title'];
    }
    else {
      // This is not a local task, so use it for the page title (unless the
      // conditions described above are met).
      if (isset($local_task_title) && isset($item['href']) && $item['href'] == '<front>') {
        return $local_task_title;
      }
      else {
        return $item['title'];
      }
    }
  }
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
