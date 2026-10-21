# menu_delete_menu_confirm()

- **Type:** Function
- **File:** [`modules/menu/menu.admin.inc`](_file.md), lines 543–552 · [local source](../../../../source/modules/menu/menu.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc#L543-L552)
- **Module/theme:** menu

## Signature

```php
function menu_delete_menu_confirm($form, &$form_state, $menu)
```

## Documentation

```text
Build a confirm form for deletion of a custom menu.
```

## Code

```php
function menu_delete_menu_confirm($form, &$form_state, $menu) {
  $form['#menu'] = $menu;
  $caption = '';
  $num_links = db_query("SELECT COUNT(*) FROM {menu_links} WHERE menu_name = :menu", array(':menu' => $menu['menu_name']))->fetchField();
  if ($num_links) {
    $caption .= '<p>' . format_plural($num_links, '<strong>Warning:</strong> There is currently 1 menu link in %title. It will be deleted (system-defined items will be reset).', '<strong>Warning:</strong> There are currently @count menu links in %title. They will be deleted (system-defined links will be reset).', array('%title' => $menu['title'])) . '</p>';
  }
  $caption .= '<p>' . t('This action cannot be undone.') . '</p>';
  return confirm_form($form, t('Are you sure you want to delete the custom menu %title?', array('%title' => $menu['title'])), 'admin/structure/menu/manage/' . $menu['menu_name'], $caption, t('Delete'));
}
```

---
_Drupal 7.103 · [modules/menu/menu.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
