# filter_element_info()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 76–83 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L76-L83)
- **Module/theme:** filter
- **Implements:** [hook_element_info()](../../system/system.api.php/hook_element_info.md)

## Signature

```php
function filter_element_info()
```

## Documentation

```text
Implements hook_element_info().

@see filter_process_format()
@see text_format_wrapper()
```

## Code

```php
function filter_element_info() {
  $type['text_format'] = array(
    '#process' => array('filter_process_format'),
    '#base_type' => 'textarea',
    '#theme_wrappers' => array('text_format_wrapper'),
  );
  return $type;
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
