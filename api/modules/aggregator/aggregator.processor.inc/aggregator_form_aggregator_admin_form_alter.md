# aggregator_form_aggregator_admin_form_alter()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.processor.inc`](_file.md), lines 73–127 · [local source](../../../../source/modules/aggregator/aggregator.processor.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.processor.inc#L73-L127)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_form_aggregator_admin_form_alter(&$form, $form_state)
```

## Documentation

```text
Implements hook_form_aggregator_admin_form_alter().

Form alter aggregator module's own form to keep processor functionality
separate from aggregator API functionality.
```

## Code

```php
function aggregator_form_aggregator_admin_form_alter(&$form, $form_state) {
  if (in_array('aggregator', variable_get('aggregator_processors', array('aggregator')))) {
    $info = module_invoke('aggregator', 'aggregator_process_info');
    $items = drupal_map_assoc(array(3, 5, 10, 15, 20, 25), '_aggregator_items');
    $period = drupal_map_assoc(array(3600, 10800, 21600, 32400, 43200, 86400, 172800, 259200, 604800, 1209600, 2419200, 4838400, 9676800), 'format_interval');
    $period[AGGREGATOR_CLEAR_NEVER] = t('Never');

    // Only wrap into a collapsible fieldset if there is a basic configuration.
    if (isset($form['basic_conf'])) {
      $form['modules']['aggregator'] = array(
        '#type' => 'fieldset',
        '#title' => t('Default processor settings'),
        '#description' => $info['description'],
        '#collapsible' => TRUE,
        '#collapsed' => !in_array('aggregator', variable_get('aggregator_processors', array('aggregator'))),
      );
    }
    else {
      $form['modules']['aggregator'] = array();
    }

    $form['modules']['aggregator']['aggregator_summary_items'] = array(
      '#type' => 'select',
      '#title' => t('Number of items shown in listing pages'),
      '#default_value' => variable_get('aggregator_summary_items', 3),
      '#empty_value' => 0,
      '#options' => $items,
    );

    $form['modules']['aggregator']['aggregator_clear'] = array(
      '#type' => 'select',
      '#title' => t('Discard items older than'),
      '#default_value' => variable_get('aggregator_clear', 9676800),
      '#options' => $period,
      '#description' => t('Requires a correctly configured <a href="@cron">cron maintenance task</a>.', array('@cron' => url('admin/reports/status'))),
    );

    $form['modules']['aggregator']['aggregator_category_selector'] = array(
      '#type' => 'radios',
      '#title' => t('Select categories using'),
      '#default_value' => variable_get('aggregator_category_selector', 'checkboxes'),
      '#options' => array('checkboxes' => t('checkboxes'),
      'select' => t('multiple selector')),
      '#description' => t('For a small number of categories, checkboxes are easier to use, while a multiple selector works well with large numbers of categories.'),
    );
    $form['modules']['aggregator']['aggregator_teaser_length'] = array(
      '#type' => 'select',
      '#title' => t('Length of trimmed description'),
      '#default_value' => variable_get('aggregator_teaser_length', 600),
      '#options' => drupal_map_assoc(array(0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000), '_aggregator_characters'),
      '#description' => t("The maximum number of characters used in the trimmed version of content.")
    );

  }
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.processor.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.processor.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
