# menu_form_node_form_alter()

- **Type:** Function
- **File:** [`modules/menu/menu.module`](_file.md), lines 683–781 · [local source](../../../../source/modules/menu/menu.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module#L683-L781)
- **Module/theme:** menu
- **Implements:** [hook_form_BASE_FORM_ID_alter()](../../system/system.api.php/hook_form_BASE_FORM_ID_alter.md)

## Signature

```php
function menu_form_node_form_alter(&$form, $form_state)
```

## Documentation

```text
Implements hook_form_BASE_FORM_ID_alter().

Adds menu item fields to the node form.

@see menu_node_submit()
```

## Code

```php
function menu_form_node_form_alter(&$form, $form_state) {
  // Generate a list of possible parents (not including this link or descendants).
  // @todo This must be handled in a #process handler.
  $link = $form['#node']->menu;
  $type = $form['#node']->type;
  // menu_parent_options() is goofy and can actually handle either a menu link
  // or a node type both as second argument. Pick based on whether there is
  // a link already (menu_node_prepare() sets mlid default to 0).
  $options = menu_parent_options(menu_get_menus(), $link['mlid'] ? $link : $type, $type);
  // If no possible parent menu items were found, there is nothing to display.
  if (empty($options)) {
    return;
  }

  $form['menu'] = array(
    '#type' => 'fieldset',
    '#title' => t('Menu settings'),
    '#access' => user_access('administer menu'),
    '#collapsible' => TRUE,
    '#collapsed' => !$link['link_title'],
    '#group' => 'additional_settings',
    '#attached' => array(
      'js' => array(drupal_get_path('module', 'menu') . '/menu.js'),
    ),
    '#tree' => TRUE,
    '#weight' => -2,
    '#attributes' => array('class' => array('menu-link-form')),
  );
  $form['menu']['enabled'] = array(
    '#type' => 'checkbox',
    '#title' => t('Provide a menu link'),
    '#default_value' => (int) (bool) $link['mlid'],
  );
  $form['menu']['link'] = array(
    '#type' => 'container',
    '#parents' => array('menu'),
    '#states' => array(
      'invisible' => array(
        'input[name="menu[enabled]"]' => array('checked' => FALSE),
      ),
    ),
  );

  // Populate the element with the link data.
  foreach (array('mlid', 'module', 'hidden', 'has_children', 'customized', 'options', 'expanded', 'hidden', 'parent_depth_limit') as $key) {
    $form['menu']['link'][$key] = array('#type' => 'value', '#value' => $link[$key]);
  }

  $form['menu']['link']['link_title'] = array(
    '#type' => 'textfield',
    '#title' => t('Menu link title'),
    '#maxlength' => 255,
    '#default_value' => $link['link_title'],
  );

  $form['menu']['link']['description'] = array(
    '#type' => 'textarea',
    '#title' => t('Description'),
    '#default_value' => isset($link['options']['attributes']['title']) ? $link['options']['attributes']['title'] : '',
    '#rows' => 1,
    '#description' => t('Shown when hovering over the menu link.'),
  );

  $default = ($link['mlid'] ? $link['menu_name'] . ':' . $link['plid'] : variable_get('menu_parent_' . $type, 'main-menu:0'));
  // If the current parent menu item is not present in options, use the first
  // available option as default value.
  // @todo User should not be allowed to access menu link settings in such a
  // case.
  if (!isset($options[$default])) {
    $array = array_keys($options);
    $default = reset($array);
  }
  $form['menu']['link']['parent'] = array(
    '#type' => 'select',
    '#title' => t('Parent item'),
    '#default_value' => $default,
    '#options' => $options,
    '#attributes' => array('class' => array('menu-parent-select')),
  );
  // Get number of items in all possible parent menus so the weight selector is
  // sized appropriately.
  $menu_names = array_keys(menu_get_menus());
  $menu_options = array();
  foreach ($menu_names as $menu_name) {
    if (isset($options[$menu_name . ':0'])) {
      $menu_options[] = $menu_name;
    }
  }
  // Make sure that we always have values in menu_options.
  $menu_options = !empty($menu_options) ? $menu_options : $menu_names;

  $form['menu']['link']['weight'] = array(
    '#type' => 'weight',
    '#title' => t('Weight'),
    '#delta' => _menu_get_menu_weight_delta($menu_options),
    '#default_value' => $link['weight'],
    '#description' => t('Menu links with smaller weights are displayed before links with larger weights.'),
  );
}
```

---
_Drupal 7.103 · [modules/menu/menu.module](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.module) · Licensed GPL-2.0-or-later (see LICENSE)._
