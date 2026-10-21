# callback_filter_settings()

- **Type:** Function
- **File:** [`modules/filter/filter.api.php`](_file.md), lines 162–172 · [local source](../../../../source/modules/filter/filter.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.api.php#L162-L172)
- **Module/theme:** filter
- **Topics:** [callbacks](../../../topics/callbacks.md)

## Signature

```php
function callback_filter_settings($form, &$form_state, $filter, $format, $defaults, $filters)
```

## Documentation

```text
Provide a settings form for filter settings.

Callback for hook_filter_info().

This callback function is used to provide a settings form for filter
settings, for filters that need settings on a per-text-format basis. This
function should return the form elements for the settings; the filter
module will take care of saving the settings in the database.

If the filter's behavior depends on an extensive list and/or external data
(e.g. a list of smileys, a list of glossary terms), then the filter module
can choose to provide a separate, global configuration page rather than
per-text-format settings. In that case, the settings callback function
should provide a link to the separate settings page.

@param $form
  The prepopulated form array of the filter administration form.
@param $form_state
  The state of the (entire) configuration form.
@param $filter
  The filter object containing the current settings for the given format,
  in $filter->settings.
@param $format
  The format object being configured.
@param $defaults
  The default settings for the filter, as defined in 'default settings' in
  hook_filter_info(). These should be combined with $filter->settings to
  define the form element defaults.
@param $filters
  The complete list of filter objects that are enabled for the given format.

@return
  An array of form elements defining settings for the filter. Array keys
  should match the array keys in $filter->settings and $defaults.

@ingroup callbacks
```

## Code

```php
function callback_filter_settings($form, &$form_state, $filter, $format, $defaults, $filters) {
  $filter->settings += $defaults;

  $elements = array();
  $elements['nofollow'] = array(
    '#type' => 'checkbox',
    '#title' => t('Add rel="nofollow" to all links'),
    '#default_value' => $filter->settings['nofollow'],
  );
  return $elements;
}
```

---
_Drupal 7.103 · [modules/filter/filter.api.php](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
