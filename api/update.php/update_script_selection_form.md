# update_script_selection_form()

- **Type:** Function
- **File:** [`update.php`](_file.md), lines 46–144 · [local source](../../source/update.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/update.php#L46-L144)

## Signature

```php
function update_script_selection_form($form, &$form_state)
```

## Documentation

```text
Form constructor for the list of available database module updates.
```

## Code

```php
function update_script_selection_form($form, &$form_state) {
  $count = 0;
  $incompatible_count = 0;
  $form['start'] = array(
    '#tree' => TRUE,
    '#type' => 'fieldset',
    '#collapsed' => TRUE,
    '#collapsible' => TRUE,
  );

  // Ensure system.module's updates appear first.
  $form['start']['system'] = array();

  $updates = update_get_update_list();
  $starting_updates = array();
  $incompatible_updates_exist = FALSE;
  foreach ($updates as $module => $update) {
    if (!isset($update['start'])) {
      $form['start'][$module] = array(
        '#type' => 'item',
        '#title' => $module . ' module',
        '#markup'  => $update['warning'],
        '#prefix' => '<div class="messages warning">',
        '#suffix' => '</div>',
      );
      $incompatible_updates_exist = TRUE;
      continue;
    }
    if (!empty($update['pending'])) {
      $starting_updates[$module] = $update['start'];
      $form['start'][$module] = array(
        '#type' => 'hidden',
        '#value' => $update['start'],
      );
      $form['start'][$module . '_updates'] = array(
        '#theme' => 'item_list',
        '#items' => $update['pending'],
        '#title' => $module . ' module',
      );
    }
    if (isset($update['pending'])) {
      $count = $count + count($update['pending']);
    }
  }

  // Find and label any incompatible updates.
  foreach (update_resolve_dependencies($starting_updates) as $function => $data) {
    if (!$data['allowed']) {
      $incompatible_updates_exist = TRUE;
      $incompatible_count++;
      $module_update_key = $data['module'] . '_updates';
      if (isset($form['start'][$module_update_key]['#items'][$data['number']])) {
        $text = $data['missing_dependencies'] ? 'This update will been skipped due to the following missing dependencies: <em>' . implode(', ', $data['missing_dependencies']) . '</em>' : "This update will be skipped due to an error in the module's code.";
        $form['start'][$module_update_key]['#items'][$data['number']] .= '<div class="messages warning">' . $text . '</div>';
      }
      // Move the module containing this update to the top of the list.
      $form['start'] = array($module_update_key => $form['start'][$module_update_key]) + $form['start'];
    }
  }

  // Warn the user if any updates were incompatible.
  if ($incompatible_updates_exist) {
    drupal_set_message('Some of the pending updates cannot be applied because their dependencies were not met.', 'warning');
  }

  if (empty($count)) {
    drupal_set_message(t('No pending updates.'));
    unset($form);
    $form['links'] = array(
      '#markup' => theme('item_list', array('items' => update_helpful_links())),
    );

    // No updates to run, so caches won't get flushed later.  Clear them now.
    drupal_flush_all_caches();
  }
  else {
    $form['help'] = array(
      '#markup' => '<p>The version of Drupal you are updating from has been automatically detected.</p>',
      '#weight' => -5,
    );
    if ($incompatible_count) {
      $form['start']['#title'] = format_plural(
        $count,
        '1 pending update (@number_applied to be applied, @number_incompatible skipped)',
        '@count pending updates (@number_applied to be applied, @number_incompatible skipped)',
        array('@number_applied' => $count - $incompatible_count, '@number_incompatible' => $incompatible_count)
      );
    }
    else {
      $form['start']['#title'] = format_plural($count, '1 pending update', '@count pending updates');
    }
    $form['actions'] = array('#type' => 'actions');
    $form['actions']['submit'] = array(
      '#type' => 'submit',
      '#value' => 'Apply pending updates',
    );
  }
  return $form;
}
```

---
_Drupal 7.103 · [update.php](https://github.com/drupal/drupal/blob/7.103/update.php) · Licensed GPL-2.0-or-later (see LICENSE)._
