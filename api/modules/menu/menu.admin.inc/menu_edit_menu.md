# menu_edit_menu()

- **Type:** Function
- **File:** [`modules/menu/menu.admin.inc`](_file.md), lines 458–519 · [local source](../../../../source/modules/menu/menu.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc#L458-L519)
- **Module/theme:** menu

## Signature

```php
function menu_edit_menu($form, &$form_state, $type, $menu = array())
```

## Documentation

```text
Menu callback; Build the form that handles the adding/editing of a custom menu.
```

## Code

```php
function menu_edit_menu($form, &$form_state, $type, $menu = array()) {
  $system_menus = menu_list_system_menus();
  $menu += array(
    'menu_name' => '',
    'old_name' => !empty($menu['menu_name']) ? $menu['menu_name'] : '',
    'title' => '',
    'description' => '',
  );
  // Allow menu_edit_menu_submit() and other form submit handlers to determine
  // whether the menu already exists.
  $form['#insert'] = empty($menu['old_name']);
  $form['old_name'] = array(
    '#type' => 'value',
    '#value' => $menu['old_name'],
  );

  $form['title'] = array(
    '#type' => 'textfield',
    '#title' => t('Title'),
    '#default_value' => $menu['title'],
    '#required' => TRUE,
    // The title of a system menu cannot be altered.
    '#access' => !isset($system_menus[$menu['menu_name']]),
  );

  $form['menu_name'] = array(
    '#type' => 'machine_name',
    '#title' => t('Menu name'),
    '#default_value' => $menu['menu_name'],
    '#maxlength' => MENU_MAX_MENU_NAME_LENGTH_UI,
    '#description' => t('A unique name to construct the URL for the menu. It must only contain lowercase letters, numbers and hyphens.'),
    '#field_prefix' => empty($menu['old_name']) ? 'menu-' : '',
    '#machine_name' => array(
      'exists' => 'menu_edit_menu_name_exists',
      'source' => array('title'),
      'replace_pattern' => '[^a-z0-9-]+',
      'replace' => '-',
    ),
    // A menu's machine name cannot be changed.
    '#disabled' => !empty($menu['old_name']) || isset($system_menus[$menu['menu_name']]),
  );

  $form['description'] = array(
    '#type' => 'textarea',
    '#title' => t('Description'),
    '#default_value' => $menu['description'],
  );
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Save'),
  );
  // Only custom menus may be deleted.
  $form['actions']['delete'] = array(
    '#type' => 'submit',
    '#value' => t('Delete'),
    '#access' => $type == 'edit' && !isset($system_menus[$menu['menu_name']]),
    '#submit' => array('menu_custom_delete_submit'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/menu/menu.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
