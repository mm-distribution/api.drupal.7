# shortcut_toolbar_pre_render()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 712–735 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L712-L735)
- **Module/theme:** shortcut

## Signature

```php
function shortcut_toolbar_pre_render($toolbar)
```

## Documentation

```text
Pre-render function for adding shortcuts to the toolbar drawer.
```

## Code

```php
function shortcut_toolbar_pre_render($toolbar) {
  $links = shortcut_renderable_links();
  $links['#attached'] = array('css' => array(drupal_get_path('module', 'shortcut') . '/shortcut.css'));
  $links['#prefix'] = '<div class="toolbar-shortcuts">';
  $links['#suffix'] = '</div>';
  $shortcut_set = shortcut_current_displayed_set();
  $configure_link = NULL;
  if (shortcut_set_edit_access($shortcut_set)) {
    $configure_link = array(
      '#type' => 'link',
      '#title' => t('Edit shortcuts'),
      '#href' => 'admin/config/user-interface/shortcut/' . $shortcut_set->set_name,
      '#options' => array('attributes' => array('id' => 'edit-shortcuts')),
    );
  }

  $drawer = array(
    'shortcuts' => $links,
    'configure' => $configure_link,
  );

  $toolbar['toolbar_drawer'][] = $drawer;
  return $toolbar;
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
