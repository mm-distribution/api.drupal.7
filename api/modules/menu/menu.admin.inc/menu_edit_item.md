# menu_edit_item()

- **Type:** Function
- **File:** [`modules/menu/menu.admin.inc`](_file.md), lines 266–389 · [local source](../../../../source/modules/menu/menu.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc#L266-L389)
- **Module/theme:** menu

## Signature

```php
function menu_edit_item($form, &$form_state, $type, $item, $menu)
```

## Documentation

```text
Menu callback; Build the menu link editing form.
```

## Code

```php
function menu_edit_item($form, &$form_state, $type, $item, $menu) {
  if ($type == 'add' || empty($item)) {
    // This is an add form, initialize the menu link.
    $item = array('link_title' => '', 'mlid' => 0, 'plid' => 0, 'menu_name' => $menu['menu_name'], 'weight' => 0, 'link_path' => '', 'options' => array(), 'module' => 'menu', 'expanded' => 0, 'hidden' => 0, 'has_children' => 0);
  }
  else {
    // Get the human-readable menu title from the given menu name.
    $titles = menu_get_menus();
    $current_title = $titles[$item['menu_name']];

    // Get the current breadcrumb and add a link to that menu's overview page.
    $breadcrumb = menu_get_active_breadcrumb();
    $breadcrumb[] = l($current_title, 'admin/structure/menu/manage/' . $item['menu_name']);
    drupal_set_breadcrumb($breadcrumb);
  }
  $form['actions'] = array('#type' => 'actions');
  $form['link_title'] = array(
    '#type' => 'textfield',
    '#title' => t('Menu link title'),
    '#maxlength' => 255,
    '#default_value' => $item['link_title'],
    '#description' => t('The text to be used for this link in the menu.'),
    '#required' => TRUE,
  );
  foreach (array('link_path', 'mlid', 'module', 'has_children', 'options') as $key) {
    $form[$key] = array('#type' => 'value', '#value' => $item[$key]);
  }
  // Any item created or edited via this interface is considered "customized".
  $form['customized'] = array('#type' => 'value', '#value' => 1);
  $form['original_item'] = array('#type' => 'value', '#value' => $item);

  $path = $item['link_path'];
  if (isset($item['options']['query'])) {
    $path .= '?' . drupal_http_build_query($item['options']['query']);
  }
  if (isset($item['options']['fragment'])) {
    $path .= '#' . $item['options']['fragment'];
  }
  if ($item['module'] == 'menu') {
    $form['link_path'] = array(
      '#type' => 'textfield',
      '#title' => t('Path'),
      '#maxlength' => 255,
      '#default_value' => $path,
      '#description' => t('The path for this menu link. This can be an internal path such as %add-node or an external URL such as %example. Enter %front to link to the front page.', array('%front' => '<front>', '%add-node' => 'node/add', '%example' => 'http://example.com')),
      '#required' => TRUE,
    );
    $form['actions']['delete'] = array(
      '#type' => 'submit',
      '#value' => t('Delete'),
      '#access' => $item['mlid'],
      '#submit' => array('menu_item_delete_submit'),
      '#weight' => 10,
    );
  }
  else {
    $form['_path'] = array(
      '#type' => 'item',
      '#title' => t('Path'),
      '#description' => l($item['link_title'], $item['href'], $item['options']),
    );
  }
  $form['description'] = array(
    '#type' => 'textarea',
    '#title' => t('Description'),
    '#default_value' => isset($item['options']['attributes']['title']) ? $item['options']['attributes']['title'] : '',
    '#rows' => 1,
    '#description' => t('Shown when hovering over the menu link.'),
  );
  $form['enabled'] = array(
    '#type' => 'checkbox',
    '#title' => t('Enabled'),
    '#default_value' => !$item['hidden'],
    '#description' => t('Menu links that are not enabled will not be listed in any menu.'),
  );
  $form['expanded'] = array(
    '#type' => 'checkbox',
    '#title' => t('Show as expanded'),
    '#default_value' => $item['expanded'],
    '#description' => t('If selected and this menu link has children, the menu will always appear expanded.'),
  );

  // Generate a list of possible parents (not including this link or descendants).
  if ($type == 'add') {
    $options = menu_parent_options(array($menu['menu_name'] => t($menu['title'])), $item);
  }
  else {
    $options = menu_parent_options(menu_get_menus(), $item);
  }
  $default = $item['menu_name'] . ':' . $item['plid'];
  if (!isset($options[$default])) {
    $default = $item['menu_name'] . ':0';
  }
  $form['parent'] = array(
    '#type' => 'select',
    '#title' => t('Parent link'),
    '#default_value' => $default,
    '#options' => $options,
    '#description' => t('The maximum depth for a link and all its children is fixed at !maxdepth. Some menu links may not be available as parents if selecting them would exceed this limit.', array('!maxdepth' => MENU_MAX_DEPTH)),
    '#attributes' => array('class' => array('menu-title-select')),
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

  $form['weight'] = array(
    '#type' => 'weight',
    '#title' => t('Weight'),
    '#delta' => _menu_get_menu_weight_delta($menu_options),
    '#default_value' => $item['weight'],
    '#description' => t('Optional. In the menu, the heavier links will sink and the lighter links will be positioned nearer the top.'),
  );
  $form['actions']['submit'] = array('#type' => 'submit', '#value' => t('Save'));

  return $form;
}
```

---
_Drupal 7.103 · [modules/menu/menu.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
