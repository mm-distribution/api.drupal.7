# system_cron_settings()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 1619–1656 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L1619-L1656)
- **Module/theme:** system
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function system_cron_settings()
```

## Documentation

```text
Form builder; Cron form.

@see system_settings_form()
@ingroup forms
```

## Code

```php
function system_cron_settings() {
  global $base_url;
  $form['description'] = array(
    '#markup' => '<p>' . t('Cron takes care of running periodic tasks like checking for updates and indexing content for search.') . '</p>',
  );
  $form['run'] = array(
    '#type' => 'submit',
    '#value' => t('Run cron'),
    '#submit' => array('system_run_cron_submit'),
  );
  $status = '<p>' . t('Last run: %cron-last ago.', array('%cron-last' => format_interval(REQUEST_TIME - variable_get('cron_last')),)) . '</p>';
  $form['status'] = array(
    '#markup' => $status,
  );

  $form['cron_url'] = array(
    '#markup' => '<p>' . t('To run cron from outside the site, go to <a href="!cron">!cron</a>', array('!cron' => url($base_url . '/cron.php', array('external' => TRUE, 'query' => array('cron_key' => variable_get('cron_key', 'drupal')))))) . '</p>',
  );

  $form['cron'] = array(
    '#type' => 'fieldset',
  );
  $form['cron']['cron_safe_threshold'] = array(
    '#type' => 'select',
    '#title' => t('Run cron every'),
    '#description' => t('More information about setting up scheduled tasks can be found by <a href="@url">reading the cron tutorial on drupal.org</a>.', array('@url' => url('http://drupal.org/cron'))),
    '#default_value' => variable_get('cron_safe_threshold', DRUPAL_CRON_DEFAULT_THRESHOLD),
    '#options' => array(0 => t('Never')) + drupal_map_assoc(array(3600, 10800, 21600, 43200, 86400, 604800), 'format_interval'),
  );
  $form['cron']['cron_detailed_logging'] = array(
    '#type' => 'checkbox',
    '#title' => t('Detailed cron logging'),
    '#default_value' => variable_get('cron_detailed_logging', DRUPAL_CRON_DETAILED_LOGGING),
    '#description' => t('Run times of individual cron jobs will be written to watchdog'),
  );

  return system_settings_form($form);
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
