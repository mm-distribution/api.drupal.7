# language_types_configurable()

- **Type:** Function
- **File:** [`includes/language.inc`](_file.md), lines 139–158 · [local source](../../../source/includes/language.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/language.inc#L139-L158)
- **Topics:** [language_negotiation](../../topics/language_negotiation.md)

## Signature

```php
function language_types_configurable($stored = TRUE)
```

## Documentation

```text
Returns only the configurable language types.

A language type maybe configurable or fixed. A fixed language type is a type
whose language negotiation providers are module-defined and not altered
through the user interface.

@param $stored
  Optional. By default retrieves values from the 'language_types' variable to
  avoid unnecessary hook invocations.
  If set to FALSE retrieves values from the actual language type definitions.
  This allows to react to alterations performed on the definitions by modules
  installed after the 'language_types' variable is set.

@return
  An array of language type names.
```

## Code

```php
function language_types_configurable($stored = TRUE) {
  $configurable = &drupal_static(__FUNCTION__);

  if ($stored && !isset($configurable)) {
    $types = variable_get('language_types', drupal_language_types());
    $configurable = array_keys(array_filter($types));
  }

  if (!$stored) {
    $result = array();
    foreach (language_types_info() as $type => $info) {
      if (!isset($info['fixed'])) {
        $result[] = $type;
      }
    }
    return $result;
  }

  return $configurable;
}
```

---
_Drupal 7.103 · [includes/language.inc](https://github.com/drupal/drupal/blob/7.103/includes/language.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
