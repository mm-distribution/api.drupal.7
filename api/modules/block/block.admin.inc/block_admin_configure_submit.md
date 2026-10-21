# block_admin_configure_submit()

- **Type:** Function
- **File:** [`modules/block/block.admin.inc`](_file.md), lines 466–518 · [local source](../../../../source/modules/block/block.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.admin.inc#L466-L518)
- **Module/theme:** block

## Signature

```php
function block_admin_configure_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for block_admin_configure().

@see block_admin_configure()
@see block_admin_configure_validate()
```

## Code

```php
function block_admin_configure_submit($form, &$form_state) {
  if (!form_get_errors()) {
    $transaction = db_transaction();
    try {
      db_update('block')
        ->fields(array(
          'visibility' => (int) $form_state['values']['visibility'],
          'pages' => trim($form_state['values']['pages']),
          'custom' => (int) $form_state['values']['custom'],
          'title' => $form_state['values']['title'],
        ))
        ->condition('module', $form_state['values']['module'])
        ->condition('delta', $form_state['values']['delta'])
        ->execute();

      db_delete('block_role')
        ->condition('module', $form_state['values']['module'])
        ->condition('delta', $form_state['values']['delta'])
        ->execute();
      $query = db_insert('block_role')->fields(array('rid', 'module', 'delta'));
      foreach (array_filter($form_state['values']['roles']) as $rid) {
        $query->values(array(
          'rid' => $rid,
          'module' => $form_state['values']['module'],
          'delta' => $form_state['values']['delta'],
        ));
      }
      $query->execute();

      // Store regions per theme for this block
      foreach ($form_state['values']['regions'] as $theme => $region) {
        db_merge('block')
          ->key(array('theme' => $theme, 'delta' => $form_state['values']['delta'], 'module' => $form_state['values']['module']))
          ->fields(array(
            'region' => ($region == BLOCK_REGION_NONE ? '' : $region),
            'pages' => trim($form_state['values']['pages']),
            'status' => (int) ($region != BLOCK_REGION_NONE),
          ))
          ->execute();
      }

      module_invoke($form_state['values']['module'], 'block_save', $form_state['values']['delta'], $form_state['values']);
    }
    catch (Exception $e) {
      $transaction->rollback();
      watchdog_exception('block', $e);
      throw $e;
    }
    drupal_set_message(t('The block configuration has been saved.'));
    cache_clear_all();
    $form_state['redirect'] = 'admin/structure/block';
  }
}
```

---
_Drupal 7.103 · [modules/block/block.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/block/block.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
