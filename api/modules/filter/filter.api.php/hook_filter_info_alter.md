# hook_filter_info_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/filter/filter.api.php`](_file.md), lines 109–118 · [local source](../../../../source/modules/filter/filter.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.api.php#L109-L118)
- **Module/theme:** filter
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_filter_info_alter(&$info)
```

## Documentation

```text
Perform alterations on filter definitions.

@param $info
  Array of information on filters exposed by hook_filter_info()
  implementations.
```

## Code

```php
function hook_filter_info_alter(&$info) {
  // Replace the PHP evaluator process callback with an improved
  // PHP evaluator provided by a module.
  $info['php_code']['process callback'] = 'my_module_php_evaluator';

  // Alter the default settings of the URL filter provided by core.
  $info['filter_url']['default settings'] = array(
    'filter_url_length' => 100,
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_filter_info_alter()".

_None found._

---
_Drupal 7.103 · [modules/filter/filter.api.php](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
