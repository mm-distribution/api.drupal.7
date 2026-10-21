# statistics_settings_form()

- **Type:** Function
- **File:** [`modules/statistics/statistics.admin.inc`](_file.md), lines 276–320 · [local source](../../../../source/modules/statistics/statistics.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.admin.inc#L276-L320)
- **Module/theme:** statistics
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function statistics_settings_form()
```

## Documentation

```text
Form constructor for the statistics administration form.

@ingroup forms
@see system_settings_form()
```

## Code

```php
function statistics_settings_form() {
  // Access log settings.
  $form['access'] = array(
    '#type' => 'fieldset',
    '#title' => t('Access log settings'),
  );
  $form['access']['statistics_enable_access_log'] = array(
    '#type' => 'checkbox',
    '#title' => t('Enable access log'),
    '#default_value' => variable_get('statistics_enable_access_log', 0),
    '#description' => t('Log each page access. Required for referrer statistics.'),
  );
  $form['access']['statistics_flush_accesslog_timer'] = array(
    '#type' => 'select',
    '#title' => t('Discard access logs older than'),
    '#default_value' => variable_get('statistics_flush_accesslog_timer', 259200),
    '#options' => array(0 => t('Never')) + drupal_map_assoc(array(3600, 10800, 21600, 32400, 43200, 86400, 172800, 259200, 604800, 1209600, 2419200, 4838400, 9676800), 'format_interval'),
    '#description' => t('Older access log entries (including referrer statistics) will be automatically discarded. (Requires a correctly configured <a href="@cron">cron maintenance task</a>.)', array('@cron' => url('admin/reports/status'))),
  );

  // Content counter settings.
  $form['content'] = array(
    '#type' => 'fieldset',
    '#title' => t('Content viewing counter settings'),
  );
  $form['content']['statistics_count_content_views'] = array(
    '#type' => 'checkbox',
    '#title' => t('Count content views'),
    '#default_value' => variable_get('statistics_count_content_views', 0),
    '#description' => t('Increment a counter each time content is viewed.'),
  );
  $form['content']['statistics_count_content_views_ajax'] = array(
    '#type' => 'checkbox',
    '#title' => t('Use Ajax to increment the counter'),
    '#default_value' => variable_get('statistics_count_content_views_ajax', 0),
    '#description' => t('Perform the count asynchronously after page load rather than during page generation.'),
    '#states' => array(
      'disabled' => array(
        ':input[name="statistics_count_content_views"]' => array('checked' => FALSE),
      ),
    ),
  );

  return system_settings_form($form);
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
