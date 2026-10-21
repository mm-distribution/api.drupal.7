# theme_system_modules_fieldset()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 2660–2696 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L2660-L2696)
- **Module/theme:** system
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_system_modules_fieldset($variables)
```

## Documentation

```text
Returns HTML for the modules form.

@param $variables
  An associative array containing:
  - form: A render element representing the form.

@ingroup themeable
```

## Code

```php
function theme_system_modules_fieldset($variables) {
  $form = $variables['form'];

  // Individual table headers.
  $rows = array();
  // Iterate through all the modules, which are
  // children of this fieldset.
  foreach (element_children($form) as $key) {
    // Stick it into $module for easier accessing.
    $module = $form[$key];
    $row = array();
    unset($module['enable']['#title']);
    $row[] = array('class' => array('checkbox'), 'data' => drupal_render($module['enable']));
    $label = '<label';
    if (isset($module['enable']['#id'])) {
      $label .= ' for="' . $module['enable']['#id'] . '"';
    }
    $row[] = $label . '><strong>' . drupal_render($module['name']) . '</strong></label>';
    $row[] = drupal_render($module['version']);
    // Add the description, along with any modules it requires.
    $description = drupal_render($module['description']);
    if ($module['#requires']) {
      $description .= '<div class="admin-requirements">' . t('Requires: !module-list', array('!module-list' => implode(', ', $module['#requires']))) . '</div>';
    }
    if ($module['#required_by']) {
      $description .= '<div class="admin-requirements">' . t('Required by: !module-list', array('!module-list' => implode(', ', $module['#required_by']))) . '</div>';
    }
    $row[] = array('data' => $description, 'class' => array('description'));
    // Display links (such as help or permissions) in their own columns.
    foreach (array('help', 'permissions', 'configure') as $link_type) {
      $row[] = array('data' => drupal_render($module['links'][$link_type]), 'class' => array($link_type));
    }
    $rows[] = $row;
  }

  return theme('table', array('header' => $form['#header'], 'rows' => $rows));
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
