# block_form_user_profile_form_alter()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 576–606 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L576-L606)
- **Module/theme:** block
- **Implements:** [hook_form_FORM_ID_alter()](../../system/system.api.php/hook_form_FORM_ID_alter.md)

## Signature

```php
function block_form_user_profile_form_alter(&$form, &$form_state)
```

## Documentation

```text
Implements hook_form_FORM_ID_alter() for user_profile_form().
```

## Code

```php
function block_form_user_profile_form_alter(&$form, &$form_state) {
  if ($form['#user_category'] == 'account') {
    $account = $form['#user'];
    $rids = array_keys($account->roles);
    $result = db_query("SELECT DISTINCT b.* FROM {block} b LEFT JOIN {block_role} r ON b.module = r.module AND b.delta = r.delta WHERE b.status = 1 AND b.custom <> 0 AND (r.rid IN (:rids) OR r.rid IS NULL) ORDER BY b.weight, b.module", array(':rids' => $rids));

    $blocks = array();
    foreach ($result as $block) {
      $data = module_invoke($block->module, 'block_info');
      if ($data[$block->delta]['info']) {
        $blocks[$block->module][$block->delta] = array(
          '#type' => 'checkbox',
          '#title' => check_plain($data[$block->delta]['info']),
          '#default_value' => isset($account->data['block'][$block->module][$block->delta]) ? $account->data['block'][$block->module][$block->delta] : ($block->custom == 1),
        );
      }
    }
    // Only display the fieldset if there are any personalizable blocks.
    if ($blocks) {
      $form['block'] = array(
        '#type' => 'fieldset',
        '#title' => t('Personalize blocks'),
        '#description' => t('Blocks consist of content or information that complements the main content of the page. Enable or disable optional blocks using the checkboxes below.'),
        '#weight' => 3,
        '#collapsible' => TRUE,
        '#tree' => TRUE,
      );
      $form['block'] += $blocks;
    }
  }
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
