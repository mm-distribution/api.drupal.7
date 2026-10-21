# hook_preprocess_HOOK()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/theme.api.php`](_file.md), lines 159–163 · [local source](../../../../source/modules/system/theme.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/theme.api.php#L159-L163)
- **Module/theme:** system

## Signature

```php
function hook_preprocess_HOOK(&$variables)
```

## Documentation

```text
Preprocess theme variables for a specific theme hook.

This hook allows modules to preprocess theme variables for a specific theme
hook. It should only be used if a module needs to override or add to the
theme preprocessing for a theme hook it didn't define.

For more detailed information, see theme().

@param $variables
  The variables array (modify in place).
```

## Code

```php
function hook_preprocess_HOOK(&$variables) {
  // This example is from rdf_preprocess_image(). It adds an RDF attribute
  // to the image hook's variables.
  $variables['attributes']['typeof'] = array('foaf:Image');
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_preprocess_HOOK()".

_None found._

---
_Drupal 7.103 · [modules/system/theme.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/theme.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
