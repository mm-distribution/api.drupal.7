# shortcut_preprocess_page()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 645–696 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L645-L696)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_preprocess_page(&$variables)
```

## Documentation

```text
Implements hook_preprocess_page().
```

## Code

```php
function shortcut_preprocess_page(&$variables) {
  // Only display the shortcut link if the user has the ability to edit
  // shortcuts and if the page's actual content is being shown (for example,
  // we do not want to display it on "access denied" or "page not found"
  // pages).
  if (shortcut_set_edit_access() && ($item = menu_get_item()) && $item['access']) {
    $link = $_GET['q'];
    $query_parameters = drupal_get_query_parameters();
    if (!empty($query_parameters)) {
     $link .= '?' . drupal_http_build_query($query_parameters);
    }
    $query = array(
     'link' => $link,
     'name' => drupal_get_title(),
    );
    $query += drupal_get_destination();

    $shortcut_set = shortcut_current_displayed_set();

    // Check if $link is already a shortcut and set $link_mode accordingly.
    foreach ($shortcut_set->links as $shortcut) {
      if ($link == $shortcut['link_path']) {
        $mlid = $shortcut['mlid'];
        break;
      }
    }
    $link_mode = isset($mlid) ? "remove" : "add";

    if ($link_mode == "add") {
      $query['token'] = drupal_get_token('shortcut-add-link');
      $link_text = shortcut_set_switch_access() ? t('Add to %shortcut_set shortcuts', array('%shortcut_set' => $shortcut_set->title)) : t('Add to shortcuts');
      $link_path = 'admin/config/user-interface/shortcut/' . $shortcut_set->set_name . '/add-link-inline';
    }
    else {
      $query['mlid'] = $mlid;
      $link_text = shortcut_set_switch_access() ? t('Remove from %shortcut_set shortcuts', array('%shortcut_set' => $shortcut_set->title)) : t('Remove from shortcuts');
      $link_path = 'admin/config/user-interface/shortcut/link/' . $mlid . '/delete';
    }

    if (theme_get_setting('shortcut_module_link')) {
      $variables['title_suffix']['add_or_remove_shortcut'] = array(
        '#attached' => array('css' => array(drupal_get_path('module', 'shortcut') . '/shortcut.css')),
        '#prefix' => '<div class="add-or-remove-shortcuts ' . $link_mode . '-shortcut">',
        '#type' => 'link',
        '#title' => '<span class="icon"></span><span class="text">' . $link_text . '</span>',
        '#href' => $link_path,
        '#options' => array('query' => $query, 'html' => TRUE),
        '#suffix' => '</div>',
      );
    }
  }
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
