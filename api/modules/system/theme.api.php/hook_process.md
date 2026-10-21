# hook_process()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/theme.api.php`](_file.md), lines 181–193 · [local source](../../../../source/modules/system/theme.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/theme.api.php#L181-L193)
- **Module/theme:** system

## Signature

```php
function hook_process(&$variables, $hook)
```

## Documentation

```text
Process theme variables for templates.

This hook allows modules to process theme variables for theme templates. It
is called for all theme hooks implemented as templates, but not for theme
hooks implemented as functions. hook_process_HOOK() can be used to process
variables for a specific theme hook, whether implemented as a template or
function.

For more detailed information, see theme().

@param $variables
  The variables array (modify in place).
@param $hook
  The name of the theme hook.
```

## Code

```php
function hook_process(&$variables, $hook) {
  // Wraps variables in RDF wrappers.
  if (!empty($variables['rdf_template_variable_attributes_array'])) {
    foreach ($variables['rdf_template_variable_attributes_array'] as $variable_name => $attributes) {
      $context = array(
        'hook' => $hook,
        'variable_name' => $variable_name,
        'variables' => $variables,
      );
      $variables[$variable_name] = theme('rdf_template_variable_wrapper', array('content' => $variables[$variable_name], 'attributes' => $attributes, 'context' => $context));
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_process()".

_None found._

---
_Drupal 7.103 · [modules/system/theme.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/theme.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
