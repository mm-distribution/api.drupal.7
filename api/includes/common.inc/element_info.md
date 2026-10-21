# element_info()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 6648–6666 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L6648-L6666)

## Signature

```php
function element_info($type)
```

## Documentation

```text
Retrieves the default properties for the defined element type.

@param $type
  An element type as defined by hook_element_info().
```

## Code

```php
function element_info($type) {
  // Use the advanced drupal_static() pattern, since this is called very often.
  static $drupal_static_fast;
  if (!isset($drupal_static_fast)) {
    $drupal_static_fast['cache'] = &drupal_static(__FUNCTION__);
  }
  $cache = &$drupal_static_fast['cache'];

  if (!isset($cache)) {
    $cache = module_invoke_all('element_info');
    foreach ($cache as $element_type => $info) {
      $cache[$element_type]['#type'] = $element_type;
    }
    // Allow modules to alter the element type defaults.
    drupal_alter('element_info', $cache);
  }

  return isset($cache[$type]) ? $cache[$type] : array();
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
