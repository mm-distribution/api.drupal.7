# shortcut_link_add_inline()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.admin.inc`](_file.md), lines 769–788 · [local source](../../../../source/modules/shortcut/shortcut.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc#L769-L788)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_link_add_inline($shortcut_set)
```

## Documentation

```text
Menu page callback: creates a new link in the provided shortcut set.

After completion, redirects the user back to where they came from.

@param $shortcut_set
  Returned from shortcut_set_load().
```

## Code

```php
function shortcut_link_add_inline($shortcut_set) {
  if (isset($_REQUEST['token']) && drupal_valid_token($_REQUEST['token'], 'shortcut-add-link') && shortcut_valid_link($_GET['link'])) {
    $item = menu_get_item($_GET['link']);
    $title = ($item && $item['title']) ? $item['title'] : $_GET['name'];
    $link = array(
      'link_title' => $title,
      'link_path' => $_GET['link'],
    );
    shortcut_admin_add_link($link, $shortcut_set, shortcut_max_slots());
    if (shortcut_set_save($shortcut_set)) {
      drupal_set_message(t('Added a shortcut for %title.', array('%title' => $link['link_title'])));
    }
    else {
      drupal_set_message(t('Unable to add a shortcut for %title.', array('%title' => $link['link_title'])));
    }
    drupal_goto();
  }

  return MENU_ACCESS_DENIED;
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
