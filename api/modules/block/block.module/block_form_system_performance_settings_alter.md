# block_form_system_performance_settings_alter()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 1076–1086 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L1076-L1086)
- **Module/theme:** block
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function block_form_system_performance_settings_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter().
```

## Code

```php
function block_form_system_performance_settings_alter(&$form, &$form_state) {
  $disabled = (!variable_get('block_cache_bypass_node_grants', FALSE) && count(module_implements('node_grants')));
  $form['caching']['block_cache'] = array(
    '#type' => 'checkbox',
    '#title' => t('Cache blocks'),
    '#default_value' => variable_get('block_cache', FALSE),
    '#disabled' => $disabled,
    '#description' => $disabled ? t('Block caching is inactive because you have enabled modules defining content access restrictions.') : NULL,
    '#weight' => -1,
  );
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
