# theme_update_manager_update_form()

- **Type:** Function
- **File:** [`modules/update/update.manager.inc`](_file.md), lines 276–282 · [local source](../../../../source/modules/update/update.manager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc#L276-L282)
- **Module/theme:** update
- **Topics:** [update_manager_update](../../../topics/update_manager_update.md), [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_update_manager_update_form($variables)
```

## Documentation

```text
Returns HTML for the first page in the process of updating projects.

@param $variables
  An associative array containing:
  - form: A render element representing the form.

@ingroup themeable
```

## Code

```php
function theme_update_manager_update_form($variables) {
  $form = $variables['form'];
  $last = variable_get('update_last_check', 0);
  $output = theme('update_last_check', array('last' => $last));
  $output .= drupal_render_children($form);
  return $output;
}
```

---
_Drupal 7.103 · [modules/update/update.manager.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
