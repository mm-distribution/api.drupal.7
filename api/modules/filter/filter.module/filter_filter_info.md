# filter_filter_info()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 1231–1270 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L1231-L1270)
- **Module/theme:** filter
- **Topics:** [standard_filters](../../../topics/standard_filters.md)
- **Implements:** [hook_filter_info()](../filter.api.php/hook_filter_info.md)

## Signature

```php
function filter_filter_info()
```

## Documentation

```text
Implements hook_filter_info().
```

## Code

```php
function filter_filter_info() {
  $filters['filter_html'] = array(
    'title' => t('Limit allowed HTML tags'),
    'process callback' => '_filter_html',
    'settings callback' => '_filter_html_settings',
    'default settings' => array(
      'allowed_html' => '<a> <em> <strong> <cite> <blockquote> <code> <ul> <ol> <li> <dl> <dt> <dd>',
      'filter_html_help' => 1,
      'filter_html_nofollow' => 0,
    ),
    'tips callback' => '_filter_html_tips',
    'weight' => -10,
  );
  $filters['filter_autop'] = array(
    'title' => t('Convert line breaks into HTML (i.e. <code>&lt;br&gt;</code> and <code>&lt;p&gt;</code>)'),
    'process callback' => '_filter_autop',
    'tips callback' => '_filter_autop_tips',
  );
  $filters['filter_url'] = array(
    'title' => t('Convert URLs into links'),
    'process callback' => '_filter_url',
    'settings callback' => '_filter_url_settings',
    'default settings' => array(
      'filter_url_length' => 72,
    ),
    'tips callback' => '_filter_url_tips',
  );
  $filters['filter_htmlcorrector'] = array(
    'title' =>  t('Correct faulty and chopped off HTML'),
    'process callback' => '_filter_htmlcorrector',
    'weight' => 10,
  );
  $filters['filter_html_escape'] = array(
    'title' => t('Display any HTML as plain text'),
    'process callback' => '_filter_html_escape',
    'tips callback' => '_filter_html_escape_tips',
    'weight' => -10,
  );
  return $filters;
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
