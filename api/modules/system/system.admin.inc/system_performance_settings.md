# system_performance_settings()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 1703–1788 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L1703-L1788)
- **Module/theme:** system
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function system_performance_settings()
```

## Documentation

```text
Form builder; Configure site performance settings.

@ingroup forms
@see system_settings_form()
```

## Code

```php
function system_performance_settings() {
  drupal_add_js(drupal_get_path('module', 'system') . '/system.js');

  $form['clear_cache'] = array(
    '#type' => 'fieldset',
    '#title' => t('Clear cache'),
  );

  $form['clear_cache']['clear'] = array(
    '#type' => 'submit',
    '#value' => t('Clear all caches'),
    '#submit' => array('system_clear_cache_submit'),
  );

  $form['caching'] = array(
    '#type' => 'fieldset',
    '#title' => t('Caching'),
  );

  $cache = variable_get('cache', 0);
  $form['caching']['cache'] = array(
    '#type' => 'checkbox',
    '#title' => t('Cache pages for anonymous users'),
    '#default_value' => $cache,
    '#weight' => -2,
  );
  $period = drupal_map_assoc(array(0, 60, 180, 300, 600, 900, 1800, 2700, 3600, 10800, 21600, 32400, 43200, 86400), 'format_interval');
  $period[0] = '<' . t('none') . '>';
  $form['caching']['cache_lifetime'] = array(
    '#type' => 'select',
    '#title' => t('Minimum cache lifetime'),
    '#default_value' => variable_get('cache_lifetime', 0),
    '#options' => $period,
    '#description' => t('Cached pages will not be re-created until at least this much time has elapsed.')
  );
  $form['caching']['page_cache_maximum_age'] = array(
    '#type' => 'select',
    '#title' => t('Expiration of cached pages'),
    '#default_value' => variable_get('page_cache_maximum_age', 0),
    '#options' => $period,
    '#description' => t('The maximum time an external cache can use an old version of a page.')
  );

  $directory = 'public://';
  $is_writable = is_dir($directory) && is_writable($directory);
  $disabled = !$is_writable;
  $disabled_message = '';
  if (!$is_writable) {
    $disabled_message = ' ' . t('<strong class="error">Set up the <a href="!file-system">public files directory</a> to make these optimizations available.</strong>', array('!file-system' => url('admin/config/media/file-system')));
  }

  $form['bandwidth_optimization'] = array(
    '#type' => 'fieldset',
    '#title' => t('Bandwidth optimization'),
    '#description' => t('External resources can be optimized automatically, which can reduce both the size and number of requests made to your website.') . $disabled_message,
  );

  $js_hide = $cache ? '' : ' class="js-hide"';
  $form['bandwidth_optimization']['page_compression'] = array(
    '#type' => 'checkbox',
    '#title' => t('Compress cached pages.'),
    '#default_value' => variable_get('page_compression', TRUE),
    '#prefix' => '<div id="page-compression-wrapper"' . $js_hide . '>',
    '#suffix' => '</div>',
  );
  $form['bandwidth_optimization']['preprocess_css'] = array(
    '#type' => 'checkbox',
    '#title' => t('Aggregate and compress CSS files.'),
    '#default_value' => intval(variable_get('preprocess_css', 0) && $is_writable),
    '#disabled' => $disabled,
  );
  $form['bandwidth_optimization']['preprocess_js'] = array(
    '#type' => 'checkbox',
    '#title' => t('Aggregate JavaScript files.'),
    '#default_value' => intval(variable_get('preprocess_js', 0) && $is_writable),
    '#disabled' => $disabled,
  );

  $form['#submit'][] = 'drupal_clear_css_cache';
  $form['#submit'][] = 'drupal_clear_js_cache';
  // This form allows page compression settings to be changed, which can
  // invalidate the page cache, so it needs to be cleared on form submit.
  $form['#submit'][] = 'system_clear_page_cache_submit';

  return system_settings_form($form);
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
