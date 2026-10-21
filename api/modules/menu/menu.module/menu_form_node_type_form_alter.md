# menu_form_node_type_form_alter()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 801–841 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L801-L841)
- **Module/theme:** menu
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function menu_form_node_type_form_alter(&$form, $form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().

Adds menu options to the node type form.
```

## Code

```php
function menu_form_node_type_form_alter(&$form, $form_state) {
  $menu_options = menu_get_menus();
  $type = $form['#node_type'];
  $form['menu'] = array(
    '#type' => 'fieldset',
    '#title' => t('Menu settings'),
    '#collapsible' => TRUE,
    '#collapsed' => TRUE,
    '#attached' => array(
      'js' => array(drupal_get_path('module', 'menu') . '/menu.admin.js'),
    ),
    '#group' => 'additional_settings',
  );
  $form['menu']['menu_options'] = array(
    '#type' => 'checkboxes',
    '#title' => t('Available menus'),
    '#default_value' => variable_get('menu_options_' . $type->type, array('main-menu')),
    '#options' => $menu_options,
    '#description' => t('The menus available to place links in for this content type.'),
  );
  // To avoid an 'illegal option' error after saving the form we have to load
  // all available menu items.
  // Otherwise it is not possible to dynamically add options to the list.
  // @todo Convert menu_parent_options() into a #process callback.
  $options = menu_parent_options(menu_get_menus(), array('mlid' => 0));
  $form['menu']['menu_parent'] = array(
    '#type' => 'select',
    '#title' => t('Default parent item'),
    '#default_value' => variable_get('menu_parent_' . $type->type, 'main-menu:0'),
    '#options' => $options,
    '#description' => t('Choose the menu item to be the default parent for a new link in the content authoring form.'),
    '#attributes' => array('class' => array('menu-title-select')),
  );

  // Call Drupal.menu_update_parent_list() to filter the list of
  // available default parent menu items based on the selected menus.
  drupal_add_js(
    '(function ($) { Drupal.menu_update_parent_list(); })(jQuery);',
    array('scope' => 'footer', 'type' => 'inline')
  );
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
