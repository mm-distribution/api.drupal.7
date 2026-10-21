# aggregator_admin_form()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.admin.inc`](_file.md), lines 421–524 · [local source](../../../../source/modules/aggregator/aggregator.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc#L421-L524)
- **Module/theme:** aggregator
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function aggregator_admin_form($form, $form_state)
```

## Documentation

```text
Form constructor for the aggregator system settings.

@see aggregator_admin_form_submit()
@ingroup forms
```

## Code

```php
function aggregator_admin_form($form, $form_state) {
  // Global aggregator settings.
  $form['aggregator_allowed_html_tags'] = array(
    '#type' => 'textfield',
    '#title' => t('Allowed HTML tags'),
    '#size' => 80,
    '#maxlength' => 255,
    '#default_value' => variable_get('aggregator_allowed_html_tags', '<a> <b> <br> <dd> <dl> <dt> <em> <i> <li> <ol> <p> <strong> <u> <ul>'),
    '#description' => t('A space-separated list of HTML tags allowed in the content of feed items. Disallowed tags are stripped from the content.'),
  );

  // Make sure configuration is sane.
  aggregator_sanitize_configuration();

  // Get all available fetchers.
  $fetchers = module_implements('aggregator_fetch');
  foreach ($fetchers as $k => $module) {
    if ($info = module_invoke($module, 'aggregator_fetch_info')) {
      $label = $info['title'] . ' <span class="description">' . $info['description'] . '</span>';
    }
    else {
      $label = $module;
    }
    unset($fetchers[$k]);
    $fetchers[$module] = $label;
  }

  // Get all available parsers.
  $parsers = module_implements('aggregator_parse');
  foreach ($parsers as $k => $module) {
    if ($info = module_invoke($module, 'aggregator_parse_info')) {
      $label = $info['title'] . ' <span class="description">' . $info['description'] . '</span>';
    }
    else {
      $label = $module;
    }
    unset($parsers[$k]);
    $parsers[$module] = $label;
  }

  // Get all available processors.
  $processors = module_implements('aggregator_process');
  foreach ($processors as $k => $module) {
    if ($info = module_invoke($module, 'aggregator_process_info')) {
      $label = $info['title'] . ' <span class="description">' . $info['description'] . '</span>';
    }
    else {
      $label = $module;
    }
    unset($processors[$k]);
    $processors[$module] = $label;
  }

  // Only show basic configuration if there are actually options.
  $basic_conf = array();
  if (count($fetchers) > 1) {
    $basic_conf['aggregator_fetcher'] = array(
      '#type' => 'radios',
      '#title' => t('Fetcher'),
      '#description' => t('Fetchers download data from an external source. Choose a fetcher suitable for the external source you would like to download from.'),
      '#options' => $fetchers,
      '#default_value' => variable_get('aggregator_fetcher', 'aggregator'),
    );
  }
  if (count($parsers) > 1) {
    $basic_conf['aggregator_parser'] = array(
      '#type' => 'radios',
      '#title' => t('Parser'),
      '#description' => t('Parsers transform downloaded data into standard structures. Choose a parser suitable for the type of feeds you would like to aggregate.'),
      '#options' => $parsers,
      '#default_value' => variable_get('aggregator_parser', 'aggregator'),
    );
  }
  if (count($processors) > 1) {
    $basic_conf['aggregator_processors'] = array(
      '#type' => 'checkboxes',
      '#title' => t('Processors'),
      '#description' => t('Processors act on parsed feed data, for example they store feed items. Choose the processors suitable for your task.'),
      '#options' => $processors,
      '#default_value' => variable_get('aggregator_processors', array('aggregator')),
    );
  }
  if (count($basic_conf)) {
    $form['basic_conf'] = array(
      '#type' => 'fieldset',
      '#title' => t('Basic configuration'),
      '#description' => t('For most aggregation tasks, the default settings are fine.'),
      '#collapsible' => TRUE,
      '#collapsed' => FALSE,
      );
    $form['basic_conf'] += $basic_conf;
  }

  // Implementing modules will expect an array at $form['modules'].
  $form['modules'] = array();

  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Save configuration'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
